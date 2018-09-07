from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('/', home, name='home'),
    re_path(r'^topics/$', topics_list, name='topics-list'),
    re_path(r'^topics/(?P<topic_pk>\d+)/$', topic_details, name='topic-details'),
]