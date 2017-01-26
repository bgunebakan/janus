from django.shortcuts import render
from rest_framework import viewsets
from .models import Permission, Permission_types
from .serializers import PermissionSerializer, PermissionTypeSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    search_fields = ('identifier', 'door')
    filter_fields = ('id', 'identifier') 
    
class PermissionTypesViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionTypeSerializer
    queryset = Permission_types.objects.all()
    search_fields = ('name')
    filter_fields = ('id', 'name')
