from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from .models import *
from app.Serializers import PostSerializer, LikeSerializer, UserSerializer
from app.Permissions import IsOwnerOrReadOnly, IsOwnerOrPublic


class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    message = "User registered successfully."

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data["message"] = self.message
        return response


from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrPublic]
    message_success = "Post operation successful."

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.context['message'] = self.message_success

    def perform_update(self, serializer):
        serializer.save()
        serializer.context["message"] = self.message_success

    def perform_destroy(self, instance):
        instance.delete()
        self.message_success = "Post deleted successfully."


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    message_success = "Like operation successful."

    def perform_create(self, serializer):
        serializer.save()
        serializer.context["message"] = self.message_success

    def perform_destroy(self, instance):
        instance.delete()
        self.message_success = "Like removed successfully."
