from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^topics/$', topics_list, name='topic-list'),
]