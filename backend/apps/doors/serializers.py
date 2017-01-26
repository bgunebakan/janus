from .models import Door
from identifiers.serializers import IdentifierTypeSerializer 
from rest_framework import serializers

class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        identifier_type = IdentifierTypeSerializer()
        fields = (
            'id', 'name', 'health', 'identifier_type', 'created_date', 'updated_date'
        ) 
