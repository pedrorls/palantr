from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('topics/', topics_list, name='topics-list'),
    path('topics/<int:topic_pk>/', topic_details, name='topic-details'),
    path('topics/<int:topic_pk>/posts/', topic_posts, name='topic-posts'),
]