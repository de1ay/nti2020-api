from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from .models import *
from .serializers import *
from .critical import *

# Create your views here.


class RecordFilter(filters.FilterSet):
    min_date_captured = filters.IsoDateTimeFilter(field_name="date_captured", lookup_expr='gte')
    max_date_captured = filters.IsoDateTimeFilter(field_name="date_captured", lookup_expr='lte')
    min_date_received = filters.IsoDateTimeFilter(field_name="date_received", lookup_expr='gte')
    max_date_received = filters.IsoDateTimeFilter(field_name="date_received", lookup_expr='lte')
    min_temperature = filters.NumberFilter(field_name="temperature", lookup_expr='gte')
    max_temperature = filters.NumberFilter(field_name="temperature", lookup_expr='lte')
    min_vibration = filters.NumberFilter(field_name="vibration", lookup_expr='gte')
    max_vibration = filters.NumberFilter(field_name="vibration", lookup_expr='lte')
    min_power = filters.NumberFilter(field_name="power", lookup_expr='gte')
    max_power = filters.NumberFilter(field_name="power", lookup_expr='lte')
    min_system_load = filters.NumberFilter(field_name="system_load", lookup_expr='gte')
    max_system_load = filters.NumberFilter(field_name="system_load", lookup_expr='lte')
    min_work_time = filters.NumberFilter(field_name="work_time", lookup_expr='gte')
    max_work_time = filters.NumberFilter(field_name="work_time", lookup_expr='lte')

    class Meta:
        model = MachineRecord
        fields = ['machine_id',
                  'date_captured', 'min_date_captured','max_date_captured',
                  'date_received', 'min_date_received','max_date_received',
                  'min_temperature','max_temperature',
                  'min_vibration','max_vibration',
                  'min_power','max_power',
                  'min_system_load','max_system_load',
                  'min_work_time','max_work_time',]


class RecordViewSet(viewsets.ModelViewSet):
    """
    List all record, useful for graphics
    """
    queryset = MachineRecord.objects.all()
    serializer_class = MachineRecordSerializer
    filterset_class = RecordFilter

    def create(self, request):
        serializer = MachineRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.instance
            check_data(data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=False)
    def get_last_info(self, request, pk=None):
        machines_num = 12
        queryset = []
        for mach in range(1, machines_num+1):
            queryset.append(MachineRecord.objects.filter(machine_id=mach).order_by('-date_captured')[0])
        serializer = MachineRecordSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


class ReceiveNotifications(viewsets.ModelViewSet):
    """
    Users, who will get notifications on monitoring
    """
    queryset = ReceiveNotifications.objects.all()
    serializer_class = ReceiveNotificationsSerializer
