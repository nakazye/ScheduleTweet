from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from social.apps.django_app.default.models import UserSocialAuth
from requests_oauthlib import OAuth1Session
from ScheduleTweet.models import Posted
import ScheduleTweet.settings
import json
import re
import unicodedata

TWITTER_HOME_TL_URI = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
TWITTER_POST_URI = 'https://api.twitter.com/1.1/statuses/update.json'

PATTERN = re.compile('(([1-9])|(1[0-2]))(月|/)(([1-9])|(0[1-9])|([1-3][0-9]))')

def index(request):

    return render(request,
                  'index.html',
                  {'request': request,
                   'user': request.user,
                   'isLogin': request.user.is_authenticated()})
 

def check(request):

    twSessionForPost = OAuth1Session(ScheduleTweet.settings.SOCIAL_AUTH_TWITTER_KEY_FOR_POST,
                                     ScheduleTweet.settings.SOCIAL_AUTH_TWITTER_SECRET_FOR_POST,
                                     ScheduleTweet.settings.SOCIAL_AUTH_TWITTER_ACCESS_FOR_POST,
                                     ScheduleTweet.settings.SOCIAL_AUTH_TWITTER_ACCESS_SECRET_FOR_POST)
    
    for userData in UserSocialAuth.objects.all():

        userName = userData.extra_data['access_token']['screen_name']

        twSession = OAuth1Session(ScheduleTweet.settings.SOCIAL_AUTH_TWITTER_KEY,
                                ScheduleTweet.settings.SOCIAL_AUTH_TWITTER_SECRET,
                                userData.extra_data['access_token']['oauth_token'],
                                userData.extra_data['access_token']['oauth_token_secret'])

        twRequest = twSession.get(TWITTER_HOME_TL_URI, params={'count': 200})

        if twRequest.status_code == 200:
            timeline = json.loads(twRequest.text)
            for tweet in timeline:
                text = unicodedata.normalize('NFKC', tweet['text'])

                if PATTERN.search(text):
                    if Posted.objects.filter(user__exact=userName, tweet__exact=tweet['id_str']).count() == 0:
                        user = tweet['user']['screen_name']
                        url = 'https://twitter.com/' + tweet['user']['screen_name'] + '/status/' + tweet['id_str']
                        posttext = '@' + userName + ' ' + user \
                                   + 'さんが日付入ってるっぽいツイートしてるよ！気になる情報だったらカレンダー登録してね！誤爆だったらごめんね！　' \
                                   + url
                        twRequestForPost = twSessionForPost.post(TWITTER_POST_URI,
                                                                 params={'status': posttext})
                        if twRequestForPost.status_code == 200:
                            Posted(user=userName, tweet=tweet['id_str']).save()

    return HttpResponse('success')
