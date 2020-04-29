from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class MessageSerializer(serializers.ModelSerializer):
    #sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    #receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['pk', 'sender', 'receiver', 'message', 'is_read', 'timestamp']


class ChatGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatGroup
        fields = '__all__'


class ChatUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatUsers
        fields = '__all__'


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'
