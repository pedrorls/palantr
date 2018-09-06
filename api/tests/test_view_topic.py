from django.test import TestCase


class TopicViewTestCase(TestCase):
    def setUp(self):
        self.response = self.client.get('/api/topics/')

    def test_respose(self):
        self.assertEqual(self.response.status_code, 200)

    def test_if_returns_json(self):
        self.assertEqual(self.response['content-type'], 'application/json')
