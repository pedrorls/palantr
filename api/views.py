from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
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
def topic_details(request, topic_name):
    try:
        topic = Topic.active_objects.get(name=topic_name)
    except:
        return Response({'status': 'Topic not available'}, status=HTTP_404_NOT_FOUND)
    serializer = TopicSerializer(topic, many=False)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def topic_posts(request, topic_name):
    try:
        topic = Topic.active_objects.get(name=topic_name)
        posts = topic.posts.all()
    except:
        return Response({'status': 'Posts not available'}, status=HTTP_404_NOT_FOUND)
    serializer = PostSerialzer(posts, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def post_details(request, topic_name, post_pk):
    try:
        topic = Topic.active_objects.get(name=topic_name)
        post = topic.posts.get(pk=post_pk)
    except:
        return Response({'status': 'Post does not exist or not available'}, status=HTTP_404_NOT_FOUND)
    serializer = PostSerialzer(post, many=False)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def create_post(request, topic_name):
    serializer = PostSerialzer(data=request.data)
    if serializer.is_valid():
        topic = Topic.active_objects.get(name=topic_name)
        serializer.validated_data['topic'] = topic
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_post(request, topic_name, post_pk):
    try:
        topic = Topic.active_objects.get(name=topic_name)
        post = topic.posts.get(pk=post_pk)
        post.delete()
    except:
        return Response(status=HTTP_400_BAD_REQUEST)    
    return Response(status=HTTP_204_NO_CONTENT)