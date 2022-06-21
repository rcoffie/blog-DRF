from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from posts.models import Category, Comment, Post
from posts.serializers import CategorySerializer, CommentSerializer, PostSerializer
from .pagination import PostPageLimit

# Create your views here.


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "categories__name"]
    pagination_class = PostPageLimit


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreateComment(generics.CreateAPIView):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        post = Post.objects.get(pk=pk)
        serializer.save(post=post)


class PostCommentList(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Comment.objects.filter(post=pk)


class FilterCategoryList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        category = self.kwargs["category"]
        return Post.objects.filter(categories__name=category)
