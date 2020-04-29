from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import datetime


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)


class ChatGroup(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', blank=False)
    name = models.CharField(max_length=200, blank=False)


class ChatUsers(models.Model):
    chat = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    receive_notifications = models.BooleanField(default=True, blank=False)


class ChatMessage(models.Model):
    chat = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, blank=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    message = models.CharField(max_length=1200, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)
