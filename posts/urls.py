from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('list', views.PostsListView.as_view(), name='list'),
    path('subscriber', views.addSubscriber, name='add-subscriber'),
]