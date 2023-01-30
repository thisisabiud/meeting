from rest_framework import generics, permissions

from .serializers import PostSerializer, TopicSerializer, CommentSerializer

from .models import Post, Topic, Comment

from django.shortcuts import get_object_or_404



class TopicListCreateView(generics.ListCreateAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
   
class TopicRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


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
