from .models import Controller
from identifiers.serializers import IdentifierTypeSerializer 
from rest_framework import serializers

class ControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controller
        fields = (
            'id', 'mac', 'ip_address', 'direction', 'health', 'identifier_type', 'door', 'created_date', 'updated_date'
        )
