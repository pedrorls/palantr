from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator


class Topic(models.Model):
    name = models.CharField(max_length=30, unique=True)
    activate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic=self).count()


class Post(models.Model):
    message = models.CharField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete='CASCADE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete='CASCADE')

    def __str__(self):
        truncated_msg = Truncator(self.message)
        return truncated_msg.chars(20)
