from rest_framework import serializers
from .models import *


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', 'flag')
        read_only_fields = ('created_at', 'updated_at')

