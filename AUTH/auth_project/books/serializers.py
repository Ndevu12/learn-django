from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Book, User


# ── JWT Token Serializer (embeds role claim) ──


class MyTokenSerializer(TokenObtainPairSerializer):
    """Add username and role as extra claims in the JWT payload."""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['role'] = user.role
        return token


# ── Book Serializer ──


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'pages', 'pub_date', 'owner']
        read_only_fields = ['owner']


# ── User Serializer (admin-only listing) ──


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'date_joined']
        read_only_fields = ['id', 'date_joined']
