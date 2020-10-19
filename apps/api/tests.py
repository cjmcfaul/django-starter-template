from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIRequestFactory, force_authenticate

from apps.users.models import User

from . import views


class UserAPITestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='example_user',
            first_name='Example',
            last_name='User',
            email='user@example.com',
            password='example123',
        )

    def test_user_detail_auth(self):
        rf = APIRequestFactory()
        request = rf.get(
            reverse('api:user_detail')
        )
        force_authenticate(request, user=self.user)
        response = views.UserDetail.as_view()(request, self.user.uuid)
        self.assertEqual(response.status_code, 200)

    def test_user_detail_anon(self):
        rf = APIRequestFactory()
        request = rf.get(
            reverse('api:user_detail')
        )
        response = views.UserDetail.as_view()(request, self.user.uuid)
        self.assertEqual(response.status_code, 401)
