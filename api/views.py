from django.http import JsonResponse, HttpResponse
from .models import Topic
from .serializers import TopicSerializer


def home(request):
    return HttpResponse('<h1>API home page!<h1>')


def topics_list(request):
    topics = Topic.active_objects.all()
    serializer = TopicSerializer(topics, many=True)
    return JsonResponse(serializer.data, safe=False)


def topic_details(request, topic_pk):
    try:
        topic = Topic.active_objects.get(pk=topic_pk)
    except:
        return JsonResponse({'status': 'topic not available'}, status=404)
    serializer = TopicSerializer(topic, many=False)
    return JsonResponse(serializer.data, safe=False)
