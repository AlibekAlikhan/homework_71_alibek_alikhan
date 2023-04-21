from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "description", "image", "author", "likes", "comment")
        read_only = ("id", "likes", "comment", "author")
