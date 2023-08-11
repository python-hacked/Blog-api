
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .models import Post
from .Serializers import PostSerializer

class PostSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', description='Test description', content='Test content', owner=self.user)

    def test_post_serializer(self):
        serializer = PostSerializer(instance=self.post)
        self.assertEqual(serializer.data['title'], 'Test Post')
