import datetime

from django.db import models
from django.utils import timezone

class Video(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250, blank=True)
    full_description = models.TextField(blank=True)
    link = models.CharField(max_length=250)
    published_at = models.DateTimeField('date published')
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=5)
