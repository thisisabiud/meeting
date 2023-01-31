"""
User API views
"""
from rest_framework import (
    generics, authentication,
    permissions
)

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

class ObtainTokenAndUserDetails(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({'token': token.key, 'user': serializer.data})
