from django.shortcuts import render
from posts. models import Post, Comment , Category
from posts.serializers import PostSerializer, CommentSerializer,CategorySerializer
from rest_framework import generics
# Create your views here.


class AuthorPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AuthorPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
