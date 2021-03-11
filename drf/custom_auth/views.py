from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import User, UserRole
from .serializers import UserSerializer, UserRoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post', 'put', 'patch']


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post']
