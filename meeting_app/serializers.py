from rest_framework import serializers

from .models import Post, Topic, Comment

from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'user','post', 'content', 'created_at')

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'user','title', 'content', 'is_verified','created_at', 'comments')


class TopicSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    class Meta:
        model = Topic
        fields = ('title', 'description', 'created_by', 'posts')

