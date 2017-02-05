from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^access$', views.can_access, name='access'),
    url(r'^health$', views.deneme, name='deneme'),
]
