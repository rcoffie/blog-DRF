from django.shortcuts import render
from rest_framework import generics

from posts.models import Category, Comment, Post
from posts.serializers import CategorySerializer, CommentSerializer, PostSerializer

# Create your views here.


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
