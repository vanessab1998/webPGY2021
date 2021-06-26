from django.urls import path
from . import views 
#from .view import home, detalle, contacto

urlpatterns = [
    #path('', home, name="home" ),
    #path('', home, name="detalle" ),
    #path('', home, name="contacto" ),
    path("base", views.base, name="base"),
    path("", views.index, name="index"),
    path("tejido/", views.tejido, name="tejido"),
    path("pinturas/", views.pinturas, name="pinturas"),
    path("miapi/", views.miapi, name="miapi"),
    path("iniciarsesion/", views.iniciarsesion, name="iniciarsesion"),
    path("registro/", views.registro, name="registro"),
    path("crudusuario/", views.crudusuario, name="crudusuario"),
    path("borrarusuario/<email>/", views.borrarusuario, name="borrarusuario"),
    path('editarusuario/<iduser>/', views.editarusuario, name="editarusuario"),
    #comentario
    path('crudcomentario/', views.crudcomentario, name="crudcomentario"),
    path('editarcomentario/<idcomen>/', views.editarcomentario, name="editarcomentario"),
    path("borrarcomentario/<idcomen>/", views.borrarcomentario, name="borrarcomentario"),
    ]
