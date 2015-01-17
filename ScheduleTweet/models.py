from django.db import models

class Posted(models.Model):
    user = models.TextField()
    tweet = models.TextField()
