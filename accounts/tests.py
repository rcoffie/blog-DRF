# from django.test import TestCase
from django.urls import reverse, include, path
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, URLPatternsTestCase
# Create your tests here.

class RegisterTestCase(APITestCase):
    def test_registration(self):
        data = {
        "username":"username",
        "email":"email",
        "password":"password",
        "password2":"password"
        }
        # url = reverse('accounts:register')
        url = '/accounts/register/'
        response = self.client.post(url,data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
