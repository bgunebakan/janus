from django.shortcuts import render
from rest_framework import viewsets
from .models import Identifier, Identifier_types

from .serializers import IdentifierSerializer, IdentifierTypeSerializer


class IdentifierViewSet(viewsets.ModelViewSet):
    serializer_class = IdentifierSerializer
    queryset = Identifier.objects.all()
    search_fields = ('name', 'key')
    filter_fields = ('id', 'name') 
    
class IdentifierTypesViewSet(viewsets.ModelViewSet):
    serializer_class = IdentifierTypeSerializer
    queryset = Identifier_types.objects.all()
    search_fields = ('name')
    filter_fields = ('id', 'name') 
