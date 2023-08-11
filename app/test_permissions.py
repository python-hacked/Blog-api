# cmsapp/tests/test_permissions.py

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .models import Post
from .permissions import IsOwnerOrPublic

class IsOwnerOrPublicPermissionTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', description='Test description', content='Test content', owner=self.user, is_public=False)

    def test_owner_permission(self):
        permission = IsOwnerOrPublic()
        request = self.client.get('/')
        request.user = self.user
        self.assertTrue(permission.has_object_permission(request, None, self.post))

    def test_public_permission(self):
        permission = IsOwnerOrPublic()
        request = self.client.get('/')
        self.assertTrue(permission.has_object_permission(request, None, self.post))
