from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from ScheduleTweet import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ScheduleTweet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^$', views.index),
    url('^check/', views.check),
    url('^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social'))
) + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT)

