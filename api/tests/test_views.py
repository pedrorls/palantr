from django.test import TestCase
from django.urls import reverse
from ..models import Topic


class TopicViewTestCase(TestCase):

    def test_respose_status_code(self):
        response = self.client.get(reverse('topics-list'))
        self.assertEquals(response.status_code, 200)

    def test_if_returns_json(self):
        response = self.client.get(reverse('topics-list'))
        self.assertEquals(response['content-type'], 'application/json')

    def test_if_can_retrieve_single_topic(self):
        query = Topic.objects.create(name='Developer')
        response = self.client.get(reverse('topic-details', args=[query.id]))
        self.assertEqual(response.status_code, 200)
