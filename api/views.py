from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import UserInfo
from .serializers import UserInfoSerializer, UserSerializer, PasswordSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404


# Create your views here.


# ViewSets define the view behavior.
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

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

    @action(detail=True, methods=['put'], permission_classes=(permissions.IsAdminUser,), serializer_class=PasswordSerializer)
    def change_password(self, request, pk=None):
        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid():
            #if not request.user.check_password(serializer.data.get('old_password')):
            #    return Response({'old_password': ['Wrong password.']},
            #                    status=400)
            # set_password also hashes the password that the user will get
            request.user.set_password(serializer.data.get('new_password'))
            request.user.save()
            return Response({'status': 'password set'}, status=200)

        return Response(serializer.errors,
                        status=400)
