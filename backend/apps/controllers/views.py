from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from django.utils import timezone

from .models import Controller
from identifiers.models import Identifier
from permissions.models import Permission

from .serializers import ControllerSerializer
from permissions.serializers import IdentSerializer

class ControllerViewSet(viewsets.ModelViewSet):
    serializer_class = ControllerSerializer
    lookup_field = 'mac'
    queryset = Controller.objects.all()
    search_fields = ('mac')
    filter_fields = ('id', 'mac')
    
    permission_classes_by_action = {
            'health': [AllowAny],
            'identifiers': [AllowAny],
            'access': [AllowAny],
            }

    @detail_route(methods=['get'])
    def health(self, request, mac=None):

    #getting ip address of client
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    	if x_forwarded_for:
    		client_ip = x_forwarded_for.split(',')[0]
    	else:
       		client_ip = request.META.get('REMOTE_ADDR')
        
    #check mac and ip adress are matching
 
	controller = self.get_object()  
	if controller.ip_address == client_ip:
            controller.updated_time = timezone.now
            controller.health=True 
            controller.save()
            return Response({"message":"OK!"})   
	else:
	    return Response({"message":"NOK!"})	


   
    @detail_route(methods=['get'])
    def identifiers(self, request, mac=None):
        controller = self.get_object()
        permissions_list = controller.door.permission_set

        serializer = IdentSerializer(permissions_list, many=True)
        
        return Response(serializer.data)

    @detail_route(methods=['post'])
    def access(self, request, mac):
        controller = self.get_object()
        
    #getting ip address of client
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    	if x_forwarded_for:
    		client_ip = x_forwarded_for.split(',')[0]
    	else:
       		client_ip = request.META.get('REMOTE_ADDR')
        
    #check mac and ip adress are matching
 
        if controller.ip_address == client_ip:
            
            identifier_key = request.POST.get('identifier_key', '')
           
            if identifier_key != None:

                ident = Identifier.objects.filter(key=identifier_key)
                
                if Permission.objects.filter(identifier=ident, door=controller.door).exists():
                    return Response({"access":"OK!"})
                else:
                    return Response({"access":"NOK!"})
            else:
                return Response({"message":"ERROR! Missing parameter, identifier_key"})
        else:
            return Response({"message":"ERROR! Credentials not valid"})





    def get_permissions(self):
      try:
         # return permission_classes depending on `action`
        return [permission() for permission in self.permission_classes_by_action[self.action]]
      except KeyError:
        # action is not set return default permission_classes
        return [permission() for permission in self.permission_classes]
