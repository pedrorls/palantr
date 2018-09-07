from django.test import TestCase
from django.urls import reverse
from ..models import Topic


class TopicViewTestCase(TestCase):

    def test_topic_respose_status_code(self):
        response = self.client.get(reverse('topics-list'))
        assert response.status_code == 200

    def test_if_topic_returns_json(self):
        response = self.client.get(reverse('topics-list'))
        assert response['content-type'] == 'application/json'

    def test_if_can_retrieve_single_topic(self):
        query = Topic.objects.create(name='Developer')
        response = self.client.get(reverse('topic-details', args=[query.id]))
        assert response.status_code == 200

    def test_if_there_is_a_home_page(self):
        response = self.client.get(reverse('home'))
        assert response.status_code == 200

    def test_home_page_is_not_a_json(self):
        response = self.client.get(reverse('home'))
        content = response['content-type']
        assert content != 'application/json'
