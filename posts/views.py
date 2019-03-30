from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Video

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_video_list'

    def get_queryset(self):
        return Video.objects.order_by('-published_at')[:10]
