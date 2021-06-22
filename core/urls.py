from django.urls import path
from . import views 
#from .view import home, detalle, contacto

urlpatterns = [
    #path('', home, name="home" ),
    #path('', home, name="detalle" ),
    #path('', home, name="contacto" ),
    path("", views.base, name="base"),
    path("index/", views.index, name="index"),
    path("tejido/", views.tejido, name="tejido"),
    path("pinturas/", views.pinturas, name="pinturas"),
    path("miapi/", views.miapi, name="miapi"),
    path("iniciarsesion/", views.iniciarsesion, name="iniciarsesion"),
    path("registro/", views.registro, name="registro"),
    path("formvalidation/", views.formvalidation, name="formvalidation"),
    path("rutvalidador/", views.rutvalidador, name="rutvalidador"),
    path("appclima/", views.appclima, name="appclima"),
    path("iniciarsesionjs/", views.iniciarsesion, name="iniciarsesion"),
    path("miapijs/", views.miapijs, name="miapijs"),
    path("registrojs/", views.registrojs, name="registrojs"),
    ]