from rest_framework import viewsets

from .models import Door
from .serializers import DoorSerializer


class DoorViewSet(viewsets.ModelViewSet):
    serializer_class = DoorSerializer
    queryset = Door.objects.all()
    search_fields = ('name')
    filter_fields = ('id', 'name')
