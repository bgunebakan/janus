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
    identifier_type = IdentifierTypeSerializer()
    user = UserSerializer()
    class Meta:
        model = Identifier
        fields = (
            'id', 'name', 'key', 'user', 'is_active',
            'identifier_type', 'created_date', 'updated_date'
        ) 
 
class PermIdentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier
        fields = (
            'key','is_active' 
        )
