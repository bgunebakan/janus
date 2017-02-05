from django.shortcuts import render
from django.http import HttpResponse
from doors.models import Door
from identifiers.models import Identifier
from permissions.models import Permission

def can_access(request):
    
    kapi=Door.objects.get(pk=request.GET.get('doorid'))
    ident=Identifier.objects.get(pk=request.GET.get('ident'))
   
    if Permission.objects.filter(identifier=ident.id, door=kapi.id).exists():
        return HttpResponse("True")
    else:
        return HttpResponse("False")

def deneme(request):
        return HttpResponse("True")

#def health(request):
    



