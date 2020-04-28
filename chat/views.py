from rest_framework import viewsets
from chat.models import Message
from chat.serializers import MessageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class MessageViewSet(viewsets.GenericViewSet):
    """
    List all required messages, or create a new message.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = self.queryset.filter(receiver=request.user, is_read=False)
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid() and request.user == serializer.validated_data['sender']:
            serializer.validated_data['is_read'] = False
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = self.queryset
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
        queryset = self.queryset.filter(receiver=request.user, sender=target_user)
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
