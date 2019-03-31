import datetime

from django.db import models
from django.utils import timezone

class Video(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250, blank=True, default='')
    full_description = models.TextField(blank=True, default='')
    watch_link = models.CharField('video watch url', max_length=250, default='')
    embed_link = models.CharField('video embed url', max_length=250, default='')
    published_at = models.DateTimeField('date published', default=timezone.now)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', auto_now=True)

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.published_at >= timezone.now() - datetime.timedelta(days=5)
    
    was_published_recently.boolean = True
