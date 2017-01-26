from .models import Identifier, Identifier_types
from users.serializers import UserSerializer 
from rest_framework import serializers

class IdentifierTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier_types
        fields = (
            'id', 'name', 'created_date', 'updated_date'
        ) 

class IdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier
        identifier_type = IdentifierTypeSerializer()
        user = UserSerializer()
        fields = (
            'id', 'name', 'key', 'user', 'is_active',
            'identifier_type', 'created_date', 'updated_date'
        ) 
 
