from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer
from .models import User, Profile
from rest_framework import viewsets, permissions


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    serializer_class = UserSerializer
    queryset = User.objects.all()
