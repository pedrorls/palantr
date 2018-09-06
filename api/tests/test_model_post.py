from django.test import TestCase
from django.contrib.auth.models import User
from ..models import *


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='pedro', password='senha123')
        self.topic = Topic.objects.create(name='Dev')
        self.post = Post.objects.create(message='my brand new message', topic=self.topic, created_by=self.user)


    def test_object_creation(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_string_representation(self):
        self.assertEqual(self.post.__str__(), self.post.message[:20])