from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Topic
from .serializers import TopicSerializer


def home(request):
    return HttpResponse('<h1>API home page!<h1>')


def topics_list(request):
    topics = get_list_or_404(Topic, activate=True)
    serializer = TopicSerializer(topics, many=True)
    return JsonResponse(serializer.data, safe=False)


def topic_details(request, topic_pk):
    topic = get_object_or_404(Topic, pk=topic_pk)
    if not topic.activate:
        return JsonResponse(status=404, data={'status': 'topic not available'})
    serializer = TopicSerializer(topic, many=False)
    return JsonResponse(serializer.data, safe=False)
