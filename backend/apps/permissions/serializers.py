from .models import Permission, Permission_types
from identifiers.models import Identifier
from identifiers.serializers import IdentifierSerializer, PermIdentSerializer 
from doors.serializers import DoorSerializer 
from rest_framework import serializers

class PermissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission_types
        fields = (
            'id', 'name', 'created_date', 'updated_date'
        ) 

class PermissionSerializer(serializers.ModelSerializer):
#    permission = PermissionTypeSerializer()
#    door = DoorSerializer()
#    identifier = IdentifierSerializer()
    class Meta:
        model = Permission
        fields = (
            'id', 'identifier', 'door', 'permission', 'created_date', 'updated_date'
        ) 

class IdentSerializer(serializers.ModelSerializer):
   
    identifier = PermIdentSerializer()
    class Meta:
        model = Permission
        fields = (
            'id','identifier'
        ) 
 
