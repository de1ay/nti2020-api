from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class MachineRecord(models.Model):
    machine_id = models.PositiveSmallIntegerField()
    date_captured = models.DateTimeField()
    date_received = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    vibration = models.FloatField()
    power = models.FloatField()
    system_load = models.FloatField()
    work_time = models.PositiveIntegerField()

    def __str__(self):
        return self.date_captured.isoformat()

    class Meta:
        ordering = ('date_captured',)


class ReceiveNotifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    def __str__(self):
        return self.user.username
