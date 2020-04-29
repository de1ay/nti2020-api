from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class MachineViewSet(viewsets.GenericViewSet):
    """
    List all records on machine.
    """
    queryset = MachineRecord.objects.all()
    serializer_class = MachineRecordSerializer

    def retrieve(self, request, pk=None):
        queryset = self.queryset.filter(machine_id=pk)
        serializer = MachineRecordSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MachineRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # TODO: Check place
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RecordViewSet(viewsets.ModelViewSet):
    """
    List all record, useful for debugging
    """
    queryset = MachineRecord.objects.all()
    serializer_class = MachineRecordSerializer
