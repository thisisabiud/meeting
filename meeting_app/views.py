from rest_framework import generics, permissions

from .serializers import PostSerializer, TopicSerializer, CommentSerializer

from .models import Post, Topic, Comment


# class PostListView(generics.ListAPIView):
#     """List user posts"""
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Post.objects.filter(user_id=self.kwargs['user_id'])

class TopicListView(generics.ListCreateAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

# class ManageTopic(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TopicSerializer

 
   

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

