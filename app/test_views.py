# cmsapp/tests/test_views.py

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post

class PostViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', description='Test description', content='Test content', owner=self.user)

    def test_post_list(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create(self):
        data = {'title': 'New Post', 'description': 'New description', 'content': 'New content', 'owner': self.user.id}
        response = self.client.post('/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_detail(self):
        response = self.client.get(f'/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_update(self):
        data = {'title': 'Updated Post', 'description': 'Updated description'}
        response = self.client.put(f'/posts/{self.post.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_delete(self):
        response = self.client.delete(f'/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
