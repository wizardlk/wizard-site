import datetime

from django.db import models
from django.utils import timezone

class Video(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250, blank=True, default='')
    full_description = models.TextField(blank=True, default='')
    video_id = models.CharField('Youtube video id', max_length=50, default='')
    dummy_image = models.ImageField(upload_to='uploads/videos/images/', default='')
    published_at = models.DateTimeField('date published', default=timezone.now)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', auto_now=True)

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.published_at >= timezone.now() - datetime.timedelta(days=5)
    
    was_published_recently.boolean = True


class Subscriber(models.Model):
    email = models.EmailField(max_length=254)
    supscribed_at = models.DateTimeField('date supscribed', auto_now_add=True)
    is_active = models.BooleanField('is active subscriber', default=True)
