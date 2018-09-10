from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('topics/', topics_list, name='topics-list'),
    path('topics/<str:topic_name>/', topic_details, name='topic-details'),
    path('topics/<str:topic_name>/posts/', topic_posts, name='topic-posts'),
    path('topics/<str:topic_name>/posts/create/', create_post, name='create-post'),
    path('topics/<str:topic_name>/posts/<int:post_pk>/', post_details, name='post-details'),
]