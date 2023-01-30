from django.urls import path

from . import views

urlpatterns = [
    path('posts/create/', views.PostListCreateAPIView.as_view(), name='create-post'),
    # path('posts/<int:user_id>', views.PostListCreateAPIView.as_view(), name='user-posts'),
    path('posts/<int:pk>', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post'),
    path('topics/', views.TopicListView.as_view(), name='topic-list'),
    # path('topics/manage/', views.ManageTopic.as_view(), name='topic-manage'),
]