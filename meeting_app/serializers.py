from rest_framework import serializers

from .models import Post, Topic, Comment

from django.contrib.auth import get_user_model


# class CommentSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.username')

#     class Meta:
#         model = Comment
#         fields = ('post','user', 'content', 'created_at')

#     def create(self, validated_data):
#         post = self.context['post']
#         validated_data['post'] = post
#         return Comment.objects.create(**validated_data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'user', 'post']
        read_only_fields = ['user', 'post']


class PostSerializer(serializers.ModelSerializer):
    queryset = Post.objects.all()
    user = serializers.ReadOnlyField(source='user.username')
    # comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'user','title', 'content', 'is_verified','created_at')
    
    def __init__(self, *args, **kwargs):
        topic = kwargs.pop('topic', None)
        super().__init__(*args, **kwargs)

        if topic:
            self.queryset = self.queryset.filter(topic=topic)


class TopicSerializer(serializers.ModelSerializer):
    # posts = PostSerializer(many=True, topic = serializers.SerializerMethodField('get_topic'))
    class Meta:
        model = Topic
        fields = ('id','title', 'description', 'created_by')

    # def get_topic(self, obj):
    #     return obj

