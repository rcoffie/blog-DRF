from django.shortcuts import render
from posts .models import Post, Comment, Category
from posts .serializers import CommentSerializer, PostSerializer, CategorySerializer
from rest_framework import generics
# Create your views here.


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
