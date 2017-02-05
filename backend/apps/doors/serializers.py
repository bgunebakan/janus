from .models import Door
from identifiers.serializers import IdentifierTypeSerializer 
from rest_framework import serializers

class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = (
            'id', 'name', 'antipassback', 'created_date', 'updated_date'
        ) 
