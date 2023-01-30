"""
User API views
"""
from rest_framework import (
    generics, authentication,
    permissions,
    status
)

from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import (
    UserSerializer, AuthTokenSerializer,
    LoginSerializer
)

from .models import CustomUser



class CreateUserView(generics.CreateAPIView):
    """User creation endpoint."""
    serializer_class = UserSerializer
    


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


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)

        if(serializer.is_valid(raise_exception=True)):
            user = serializer.validated_data

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            return Response({'token':token}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)