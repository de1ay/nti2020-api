from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import UserInfo
from .serializers import UserInfoSerializer, UserSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404


# Create your views here.


# ViewSets define the view behavior.
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list','retrieve','user']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=False)
    def user(self, request, *args, **kwargs):
        if not 'target_id' in kwargs:
            return Response({"detail": "No data"}, status=400)
        target_user = int(kwargs['target_id'])
        queryset = get_object_or_404(self.queryset, user=target_user)
        serializer = UserInfoSerializer(queryset)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def me(self, request, pk=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list','retrieve','me']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
