from django.contrib import admin

from .models import Video, Subscriber

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'was_published_recently')
    list_filter = ['published_at']

admin.site.register(Video, VideoAdmin)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'supscribed_at', 'is_active')
    list_filter = ['supscribed_at']

admin.site.register(Subscriber, SubscriberAdmin)
