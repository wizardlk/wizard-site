from django.http import JsonResponse
from django.core.validators import validate_email
from django.http import Http404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.core.mail import send_mail

from .models import Video, Subscriber


class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_video_list'

    def get_queryset(self):
        return Video.objects.order_by('-published_at')[:6]

class PostsListView(generic.ListView):
    template_name = 'posts/posts-list.html'
    context_object_name = 'latest_video_list'

    def get_queryset(self):
        return Video.objects.order_by('-published_at')


def addSubscriber(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        terms = request.POST.get('terms', False)

        try:
            validate_email(email)

            # add new subscriber
            subscriber = Subscriber()
            subscriber.email = email
            subscriber.save()

            return JsonResponse({'error':False}, safe=False)

        except validate_email.ValidationError:
            return JsonResponse({'error':True, 'msg':'Invalid email address'}, safe=False)

    else:
        raise Http404


def sendSubscribeMail(email):
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        [ email ],
        fail_silently=False,
    )