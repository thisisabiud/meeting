from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('create/profile/', views.ProfileCreateAPIView.as_view(), name='create-profile'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('token/details/<str:email>', views.UserDetailView.as_view(), name='token-details'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
