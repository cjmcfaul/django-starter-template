from django.test import TestCase, Client
from django.urls import reverse


class MainTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        url = reverse('index')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_about_view(self):
        url = reverse('about')
        resp = self.client(url)
        self.assertEqual(resp.status_code, 200)

    def test_contact_us_view(self):
        url = reverse('contact_us')
        resp = self.client(url)
        self.assertEqual(resp.status_code, 200)

    def test_privacy_policy_view(self):
        url = reverse('privacy_policy')
        resp = self.client(url)
        self.assertEqual(resp.status_code, 200)

    def test_terms_and_conditions_view(self):
        url = reverse('terms_and_conditions')
        resp = self.client(url)
        self.assertEqual(resp.status_code, 200)