from django.test import TestCase, RequestFactory
from django.urls import reverse
from faker import Faker
from ..models import Topic
from ..views import *


def make_request(path):
    return RequestFactory().get(path)

class TopicViewTestCase(TestCase):

    def setUp(self):
        self.factory = Faker()
        self.topic = Topic.objects.create(name=self.factory.name())
        self.topic2 = Topic.objects.create(name=self.factory.name(), activate=False)

    def test_topic_respose_status_code(self):
        path = reverse('topics-list')
        request = make_request(path)
        response = topics_list(request)
        assert response.status_code == 200

    def test_if_topic_returns_json(self):
        path = reverse('topics-list')
        request = make_request(path)
        response = topics_list(request)
        assert response['content-type'] == 'application/json'

    def test_if_can_retrieve_single_active_topic(self):
        path = reverse('topic-details', kwargs={'topic_pk': self.topic.id})
        request = make_request(path)
        response = topic_details(request, self.topic.id)
        assert response.status_code == 200

    def test_if_returns_404_if_topic_does_not_exist(self):
        path = reverse('topic-details', kwargs={'topic_pk': 100})
        request = make_request(path)
        response = topic_details(request, 100)
        assert response.status_code == 404
    
    def test_if_returns_404_single_not_active_topic(self):
        path = reverse('topic-details', kwargs={'topic_pk': self.topic2.id})
        request = make_request(path)
        response = topic_details(request, self.topic2.id)
        assert response.status_code == 404

    def test_if_there_is_a_home_page(self):
        path = reverse('home')
        request = make_request(path)
        response = home(request)
        assert response.status_code == 200

    def test_home_page_is_not_a_json(self):
        path = reverse('home')
        request = make_request(path)
        response = home(request)
        assert 'text/html' in response['content-type']



# def PostViewTestCase(TestCase):
    
#     def setUp(self):
#         self.factory = Faker()
#         self.topic = Topic.objects.create(name=self.factory.name())
#         self.user = User.objects.create(username=self.factory.username(), password=self.factory.password())
#         self.post = Post.objects.create(message=self.factory.message(), topic=self.topic, created_by=self.user)

#     def test_if_returns_list_of_posts_of_specific_topic(self):
#         response = self.client.get(reverse('topic_posts', kwargs={'topic_pk': self.topic.id, 'post:'}))