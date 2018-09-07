from django.http import JsonResponse, HttpResponse
from .models import Topic
from .serializers import TopicSerializer


def topics_list(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return JsonResponse(serializer.data, safe=False)


def topic_details(request, topic_pk):
    topic = Topic.objects.get(pk=topic_pk)
    serializer = TopicSerializer(topic, many=False)
    return JsonResponse(serializer.data, safe=False)
