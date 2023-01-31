"""
User API views
"""
from rest_framework import (
    generics, authentication,
    permissions
)

from django.contrib.auth import get_user_model

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import (
    UserSerializer, AuthTokenSerializer
    )

class CreateUserView(generics.CreateAPIView):
    """User creation endpoint."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """User token creation view"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return authenticated user."""
        return self.request.user

class UserDetailView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    lookup_field = 'email'

    # def get_queryset(self):
    #     return get_user_model().objects.filter()
    
