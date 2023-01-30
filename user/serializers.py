from rest_framework import serializers

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model, authenticate


class UserSerializer(serializers.ModelSerializer):
    """User serializer class"""

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password':{'write_only':True, 'min_length':8}}

    def create(self, validated_data):
        """Create user using validated data"""
        return get_user_model().objects.create_user(validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace = False,
    )

    def validate(self, attrs):
        """Validate the authenticated user."""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username = email,
            password=password,
        )

        if not user:
            message = _('Unable to authenticate user with provided credentials.')
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs
