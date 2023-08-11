from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.post = Post.objects.create(
            title="Test Post",
            description="Test description",
            content="Test content",
            owner=self.user,
        )

    def test_post_creation(self):
        self.assertEqual(str(self.post), self.post.title)


class LikeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.post = Post.objects.create(
            title="Test Post",
            description="Test description",
            content="Test content",
            owner=self.user,
        )
        self.like = Like.objects.create(post=self.post, user=self.user)

    def test_like_creation(self):
        self.assertEqual(
            str(self.like), f"{self.user.username} likes {self.post.title}"
        )
