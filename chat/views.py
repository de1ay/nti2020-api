from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from webpush import send_user_notification


class MessageViewSet(viewsets.GenericViewSet):
    """
    List all required messages, or create a new message.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = self.get_queryset().filter(receiver=request.user, is_read=False)
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid() and request.user == serializer.validated_data['sender']:
            serializer.validated_data['is_read'] = False
            serializer.save()
            payload = {"head": "Medis Group LLC",
                       "body": f"Сообщение от пользователя {serializer.validated_data['sender']}",
                       #"icon": "https://i.imgur.com/dRDxiCQ.png",
                       "url": f"https://api.antares.nullteam.info/chat/messages/{serializer.instance.pk}"}
            send_user_notification(user=serializer.validated_data['receiver'], payload=payload, ttl=1000)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        msg = get_object_or_404(queryset, pk=pk)
        if not ((msg.receiver == request.user) or (msg.sender == request.user)) :
            return Response({"detail": "Not allowed"}, status=401)
        serializer = MessageSerializer(msg)
        return Response(serializer.data)


    @action(detail=False)
    def user(self, request, *args, **kwargs):
        if not 'target_id' in kwargs:
            return Response({"detail": "No data"}, status=400)
        target_user = int(kwargs['target_id'])
        queryset = self.get_queryset().filter(receiver=request.user, sender=target_user)
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)


    @action(detail=True)
    def mark_as_read(self, request, pk=None):
        message = self.get_object()
        if request.user != message.receiver:
            return Response({"detail": "Not allowed"}, status=401)
        message.is_read = True
        message.save()
        return Response({"detail":"success"})


class ChatGroupViewSet(viewsets.ModelViewSet):
    queryset = ChatGroup.objects.all()
    serializer_class = ChatGroupSerializer


class ChatUsersViewSet(viewsets.ModelViewSet):
    queryset = ChatUsers.objects.all()
    serializer_class = ChatUsersSerializer

    @action(detail=True, permission_classes = [IsAuthenticated])
    def enable_notifications(self, request, pk=None):
        record = self.get_object()
        if request.user != record.user:
            return Response({"detail": "Not allowed"}, status=401)
        record.receive_notifications = True
        record.save()
        return Response({"detail":"success"})

    @action(detail=True, permission_classes = [IsAuthenticated])
    def disable_notifications(self, request, pk=None):
        record = self.get_object()
        if request.user != record.user:
            return Response({"detail": "Not allowed"}, status=401)
        record.receive_notifications = False
        record.save()
        return Response({"detail":"success"})


class ChatMessageViewSet(viewsets.GenericViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        chat = get_object_or_404(ChatGroup.objects.all(), id=pk)
        get_object_or_404(ChatUsers.objects.filter(chat=chat), user=request.user)
        queryset = self.get_queryset().filter(chat=chat)
        serializer = ChatMessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid() and request.user == serializer.validated_data['sender']:
            get_object_or_404(ChatUsers.objects.filter(chat=serializer.validated_data['chat']), user=request.user)
            users = ChatUsers.objects.filter(chat=serializer.validated_data['chat'])
            serializer.save()
            for user in users:
                if not user.receive_notifications:
                    continue
                payload = {"head": "Medis Group LLC",
                           "body": f"Сообщение из чата {serializer.instance.chat.name}",
                           "url": f"https://api.antares.nullteam.info/chat/messages/{serializer.instance.pk}"}
                send_user_notification(user=user.user, payload=payload, ttl=1000)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
