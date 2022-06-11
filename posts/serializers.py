from rest_framework import serializers
from posts.models import Post, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','author','body','categories']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author','body','post']
