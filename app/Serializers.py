# cmsapp/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}, "email": {"required": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["likes_count"]

    def get_likes_count(self, obj):
        return obj.like_set.count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

    def validate(self, data):
        post = data.get("post")
        user = data.get("user")

        if Like.objects.filter(post=post, user=user).exists():
            raise serializers.ValidationError("You have already liked this post.")

        return data
