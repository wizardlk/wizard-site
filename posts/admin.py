from django.contrib import admin

from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'was_published_recently')
    list_filter = ['published_at']

admin.site.register(Video, VideoAdmin)
