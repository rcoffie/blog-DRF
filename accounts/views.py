from django.contrib.auth.models import User
from django.shortcuts import render
from posts.models import Category, Comment, Post
from posts.serializers import (CategorySerializer, CommentSerializer,
                               PostSerializer)
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from accounts.permissions import AuthUserPost
from accounts.serializers import RegistrationSerializer

# Create your views here.


class AuthorPost(generics.ListCreateAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        return Post.objects.filter(author=user)




class AuthorPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthUserPost]


# NOTICE WILLL NEED TO RETURN USER TOKEN AFTER USER REGISTER
@api_view(
    [
        "POST",
    ]
)
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()

            Token.objects.get_or_create(user=account)
            return Response(serializer.data)


@api_view(
    [
        "POST",
    ]
)
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# class RegisterView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer


# creating post




class CreatePostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AddCategoryView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
