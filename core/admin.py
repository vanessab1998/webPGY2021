from django.contrib import admin
from .models import usuario,comentario

# Register your models here.

class adminuser(admin.ModelAdmin):
    list_display = ["nombre", "rut", "email", "telefono", "contraseña"]

admin.site.register(usuario, adminuser)

class adminuser(admin.ModelAdmin):
    list_display = ["nombre", "email", "comentario"]

admin.site.register(comentario, adminuser)

