from django.urls import path
from rest_api.views import usuarios,detalle_usuario
from .viewsLogin import login

urlpatterns = [
    path('usuarios/', usuarios, name='usuarios'),
    path('usuario/<em>', detalle_usuario, name="usuario"),
    path('login/', login, name='login'),

]