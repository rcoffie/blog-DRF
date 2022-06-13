from rest_framework import serializers

from posts.models import Category, Comment, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title", "author", "body", "categories"]

        extra_kwargs = {
        'author': {'read_only': True},
        'id': {'read_only': True}
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["author", "body", "post"]

# 
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'
#         read_only_fields = ('id','author','create_on','last_modified')
