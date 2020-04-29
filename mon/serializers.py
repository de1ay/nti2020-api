from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


# Serializers define the API representation.
class MachineRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineRecord
        fields = '__all__'
