from django.http import JsonResponse
from .models import Topic
from .serializers import TopicSerializer


def topics_list(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return JsonResponse(serializer.data, safe=False)


