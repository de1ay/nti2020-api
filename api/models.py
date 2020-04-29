from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    position = models.CharField(max_length=100)
    experience = models.PositiveSmallIntegerField()
    avatar = models.ImageField()

    def __str__(self):
        return self.user.username
