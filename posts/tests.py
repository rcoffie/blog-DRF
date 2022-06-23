# from django.test import TestCase
from django.urls import reverse, include, path
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, URLPatternsTestCase

# Create your tests here.

class ListPost(APITestCase, URLPatternsTestCase):
    urlpatterns = [
    path('', include('posts.urls', ))
    ]

    def test_list_post(self):
        url = '/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
