from django.shortcuts import render
from posts. models import Post, Comment , Category
from posts.serializers import PostSerializer, CommentSerializer,CategorySerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import AuthUserPost
# Create your views here.


class AuthorPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class AuthorPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthUserPost]
