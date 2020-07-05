from django.db import models
from django.conf import settings
# Create your models here.

class Feed(models.Model):
    name_f = models.CharField(max_length=15)
    contact_f = models.IntegerField()
    email_f = models.TextField()
    comment_f = models.CharField(max_length=200)
