from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import Message


class MessageSerializer(serializers.ModelSerializer):
    #sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    #receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['pk', 'sender', 'receiver', 'message', 'is_read', 'timestamp']
