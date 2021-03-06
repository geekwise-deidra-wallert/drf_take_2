from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from bank.serializers import UserSerializer, GroupSerializer

class UserViewSet ( viewsets.ReadOnlyModelViewSet ):
    """
        API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet ( viewsets.ReadOnlyModelViewSet ):
    """
        API endpoint that allows users to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
