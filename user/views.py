"""
User API views
"""
from rest_framework import (
    generics, authentication,
    permissions
)

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import (
    UserSerializer, AuthTokenSerializer
    )

from .models import CustomUser

class CreateUserView(generics.CreateAPIView):
    """User creation endpoint."""
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    


class CreateTokenView(ObtainAuthToken):
    """User token creation view"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class =UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return authenticated user."""
        return self.request.user