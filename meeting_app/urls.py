from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostListCreateAPIView.as_view(), name='create-post'),
    path('posts/<int:pk>', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post'),
    path('posts/<int:post_pk>/comments/', 
            views.CommentCreateAPIView.as_view(),
             name='comment-list-create'
             ),
    path('topics/<int:topic_pk>/posts/', 
            views.PostCreateAPIView.as_view(),
             name='post-list-create'
             ),
    
    path('topics/', views.TopicListCreateView.as_view(), name='topic-list'),
    # path('topics/<int:pk>', views.TopicRetrieveUpdateDestroyAPIView.as_view(), name='topic'),
    # path('topics/<int:pk>/posts', views.TopicRetrieveUpdateDestroyAPIView.as_view(), name='topic'),
]