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
from .utils import voted


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
        posts = topic.posts.order_by('-updated_at')[:20]
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
        return Response({'status': 'Post not available'}, status=HTTP_404_NOT_FOUND)
    serializer = PostSerialzer(post, many=False)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def create_post(request, topic_name):
    try:
        topic = Topic.active_objects.get(name=topic_name)
        serializer = PostSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['topic'] = topic
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
    except:
        return Response({'status': 'Post does not exist!'}, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_vote(request, topic_name, post_pk, vote):
    try:
        post = Post.objects.get(pk=post_pk)
        post.votes += voted(vote)
        post.save()
        return Response({'status':'Thanks for voting!'}, status=HTTP_201_CREATED)
    except:
        return Response({'status': 'Sorry, vote could not be saved.'}, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_post(request, topic_name, post_pk):
    try:
        topic = Topic.active_objects.get(name=topic_name)
        post = topic.posts.get(pk=post_pk)
    except:
        return Response({'status': 'Post does not exist or already deleted.'}, status=HTTP_400_BAD_REQUEST)
    if post.votes > -5:
        return Response({'status': 'Post did not reach the minimum votes to be deleted.'}, HTTP_400_BAD_REQUEST)
    post.delete()
    return Response({'status': 'Post deleted!'}, status=HTTP_204_NO_CONTENT)