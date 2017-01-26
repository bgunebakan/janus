from .models import Permission, Permission_types
from identifiers.serializers import IdentifierSerializer 
from doors.serializers import DoorSerializer 
from rest_framework import serializers

class PermissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission_types
        fields = (
            'id', 'name', 'created_date', 'updated_date'
        ) 

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        permission = PermissionTypeSerializer()
        door = DoorSerializer()
        identifier = IdentifierSerializer()
        fields = (
            'id', 'identifier', 'door', 'permission', 'created_date', 'updated_date'
        ) 
 
