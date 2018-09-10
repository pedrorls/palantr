from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from faker import Faker
from ..models import *
from ..views import *


class HomeViewTestCase(TestCase):

    def test_if_there_is_a_home_page(self):
        path = reverse('home')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_home_page_is_not_a_json(self):
        path = reverse('home')
        response = self.client.get(path)
        assert 'text/html' in response['content-type']


class TopicViewTestCase(APITestCase):

    def setUp(self):
        self.factory = Faker()
        self.topic = Topic.objects.create(name=self.factory.name())
        self.topic2 = Topic.objects.create(name=self.factory.name(), activate=False)

    def test_topic_respose_status_code(self):
        path = reverse('topics-list')
        response = self.client.get(path, format='json')
        assert response.status_code == 200

    def test_if_topic_returns_json(self):
        path = reverse('topics-list')
        response = self.client.get(path)
        assert 'json' in response['content-type']

    def test_if_can_retrieve_active_topic_details(self):
        path = reverse('topic-details', kwargs={'topic_name': self.topic.name})
        response = self.client.get(path)
        assert response.status_code == 200

    def test_if_returns_404_if_topic_does_not_exist(self):
        path = reverse('topic-details', kwargs={'topic_name': 'random'})
        response = self.client.get(path)
        assert response.status_code == 404
    
    def test_if_returns_404_for_not_active_topic_details(self):
        path = reverse('topic-details', kwargs={'topic_name': self.topic2.name})
        response = self.client.get(path)
        assert response.status_code == 404


class PostViewTestCase(APITestCase):
    
    def setUp(self):
        self.factory = Faker()
        self.topic = Topic.objects.create(name=self.factory.name())
        self.post = Post.objects.create(
            message=self.factory.sentence(),
            topic=self.topic,
            created_by=self.factory.name()
        )

    def test_response_of_posts_status_code(self):
        path = reverse('topic-posts', kwargs={'topic_name': self.topic.name})
        response = self.client.get(path)
        assert response.status_code == 200

    def test_if_post_returns_json(self):
        path = reverse('topic-posts', kwargs={'topic_name': self.topic.name})
        response = self.client.get(path, format='json')
        assert 'json' in response['content-type']

    def test_if_can_get_post_details(self):
        path = reverse('post-details', kwargs={'topic_name': self.topic.name, 'post_pk': self.post.id})
        response = self.client.get(path)
        assert response.status_code == 200

    def test_if_returns_404_for_unexistent_post(self):
        path = reverse('post-details', kwargs={'topic_name': self.topic.name, 'post_pk': 100})
        response = self.client.get(path)
        assert response.status_code == 404

    def test_if_can_create_post(self):
        path = reverse('create-post', kwargs={'topic_name': self.topic.name,})
        data = {'message': self.factory.sentence(), 'created_by': self.factory.name()}
        response = self.client.post(path, data, format='json')
        assert response.status_code == 201

    # def test_if_returns_404_if_not_found_posts(self):
    #     topic = Topic.objects.create(name=self.factory.name())
    #     path = reverse('topic-posts', kwargs={'topic_name': topic.name})
    #     response = self.client.get(path, format='json')
    #     assert response.status_code == 404
