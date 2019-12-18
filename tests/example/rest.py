from django.contrib.auth.models import User
from .models import Simple
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    SimpleSerializer,
    UserSerializer,
)


class SimpleViewSet(ModelViewSet):
    """
    TODO restrict queryset to authorized contexts for user
    """

    queryset = Simple.objects.all()
    serializer_class = SimpleSerializer


class UserViewSet(ModelViewSet):
    """
    API which allows users to be viewed or edited.
    TODO restrict queryset to authorized contexts for user
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
