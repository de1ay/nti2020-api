from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import UserInfo
from .serializers import UserInfoSerializer, UserSerializer, PasswordSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404, render
#from webpush import send_user_notification


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
        user = get_object_or_404(User.objects.all(), id=pk)
        if serializer.is_valid():
            #if not request.user.check_password(serializer.data.get('old_password')):
            #    return Response({'old_password': ['Wrong password.']},
            #                    status=400)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({'status': 'password set'}, status=200)

        return Response(serializer.errors,
                        status=400)


def subscribe(request):
    #payload = {"head": "Welcome!", "body": "Hello World", "icon": "https://i.imgur.com/dRDxiCQ.png", "url": "http://localhost/api/users"}
    #send_user_notification(user=request.user, payload=payload, ttl=1000)
    return render(request, 'subscribe.html')


def main(request):
    return render(request, 'index.html')