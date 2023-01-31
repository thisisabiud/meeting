from rest_framework import generics, permissions

from .serializers import (
    PostSerializer, TopicSerializer, 
    CommentSerializer, UserTopicSerializer
)

from .models import Post, Topic, Comment, UserTopic

from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class TopicListCreateView(generics.ListCreateAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

    

   
class TopicRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        topic = self.get_object()
        user = request.user
        UserTopic.objects.create(user=user, topic = topic)

        return Response({'message': 'UserTopic object created successfully'})


class PostCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        topic_pk = self.kwargs.get('topic_pk')
        return Post.objects.filter(topic = topic_pk)

    def perform_create(self, serializer):
        topic = get_object_or_404(Topic, pk=self.kwargs.get('topic_pk'))
        serializer.save(user=self.request.user, topic=topic)


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class CommentCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        post_pk = self.kwargs.get('post_pk')
        return Comment.objects.filter(post = post_pk)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        serializer.save(user=self.request.user, post=post)


class UserTopicView(generics.ListAPIView):
    queryset = UserTopic.objects.all()
    serializer_class = UserTopicSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        topics = UserTopic.objects.filter(user = self.request.user)

        return topics