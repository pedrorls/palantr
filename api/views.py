from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
)
from .models import Topic
from .serializers import *


def home(request):
    return HttpResponse('<h1>API home page!<h1>')


@api_view(['GET'])
def topics_list(request):
    topics = Topic.active_objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def topic_details(request, topic_pk):
    try:
        topic = Topic.active_objects.get(pk=topic_pk)
    except:
        return Response({'status': 'Topic not available'}, status=HTTP_404_NOT_FOUND)
    serializer = TopicSerializer(topic, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def topic_posts(request, topic_pk):
    topic = Topic.active_objects.get(pk=topic_pk)
    posts = topic.posts.all()
    serializer = PostSerialzer(posts, many=True)
    return Response(serializer.data)
