from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Simple


class SimpleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Simple


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User Serialization"""

    class Meta:
        model = User
        fields = ("url", "username", "email", "first_name", "last_name", "id")
