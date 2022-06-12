from django.shortcuts import render
from posts. models import Post, Comment , Category
from posts.serializers import PostSerializer, CommentSerializer,CategorySerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import AuthUserPost
from rest_framework.decorators import api_view
from accounts.serializers import RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# Create your views here.


class AuthorPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class AuthorPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthUserPost]
#
@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()

            Token.objects.get_or_create(user=account)
            return Response(serializer.data)


@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

# class RegisterView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
