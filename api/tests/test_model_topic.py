from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Topic, Post


class ModelTestCase(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name='General')
        self.user = User.objects.create(username='pedro2', password='senha123')
        self.post = Post.objects.create(message='My super message', topic=self.topic, created_by=self.user)

    def test_string_representation(self):
        self.assertEqual(self.topic.__str__(), self.topic.name)

    def test_object_creation(self):
        self.assertTrue(isinstance(self.topic, Topic))

    def test_can_create_more_than_one_object(self):
        old = Topic.objects.all().count()
        topic2 = Topic.objects.create(name='Dev')
        new = Topic.objects.all().count()
        self.assertNotEqual(old, new)

    def test_can_retrieve_number_posts(self):
        posts_num = self.topic.get_posts_count()
        query = Post.objects.filter(topic=self.topic).count()
        self.assertEqual(posts_num, query)
