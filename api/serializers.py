from rest_framework import serializers
from .models import *


class TopicSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Topic
        fields = ('id', 'name', 'activate', 'posts')
        read_only_fields = ('created_at', 'updated_at')


class PostSerialzer(serializers.ModelSerializer):
    topic = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'message', 'topic', 'created_by')
        read_only_fields = ('created_at', 'updated_at')