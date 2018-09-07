from django.test import TestCase
from django.urls import reverse
from faker import Faker
from ..models import Topic


class TopicViewTestCase(TestCase):

    def setUp(self):
        self.factory = Faker()
        self.topic = Topic.objects.create(name=self.factory.name())
        self.topic2 = Topic.objects.create(name=self.factory.name(), activate=False)

    def test_topic_respose_status_code(self):
        response = self.client.get(reverse('topics-list'))
        assert response.status_code == 200

    def test_if_topic_returns_json(self):
        response = self.client.get(reverse('topics-list'))
        assert response['content-type'] == 'application/json'

    def test_if_can_retrieve_single_active_topic(self):
        pk = self.topic.id
        response = self.client.get(reverse('topic-details', kwargs={'topic_pk': pk}))
        assert response.status_code == 200

    def test_if_returns_404_if_topic_does_not_exist(self):
        pk = self.topic.id
        response = self.client.get(reverse('topic-details', kwargs={'topic_pk': 100}))
        assert response.status_code == 404
    
    def test_if_returns_404_single_not_active_topic(self):
        pk = self.topic2.id
        response = self.client.get(reverse('topic-details', kwargs={'topic_pk': pk}))
        assert response.status_code == 404

    def test_if_there_is_a_home_page(self):
        response = self.client.get(reverse('home'))
        assert response.status_code == 200

    def test_home_page_is_not_a_json(self):
        response = self.client.get(reverse('home'))
        content = response['content-type']
        assert content != 'application/json'
