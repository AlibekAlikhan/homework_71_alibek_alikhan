from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from api.serializers import PostSerializer
from posts.models import Post
from django.views.decorators.csrf import csrf_exempt


class IsUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated


class IsCurrent(BasePermission):
    def has_permission(self, request, view, obj):
        return obj.author == request.user


class PostSimpleView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsCurrent]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def like_api(request, *args, **kwargs):
    if request.method == "GET":
        user = request.user
        post = Post.objects.get(pk=kwargs.get("pk"))
        if post not in user.liked_posts.all():
            user.liked_posts.add(post)
            post.plus()
        else:
            user.liked_posts.remove(post)
            post.minus()
        return JsonResponse({"": ""})
