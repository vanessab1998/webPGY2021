from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre=models.CharField(max_length=100)
    rut=models.CharField(max_length=10)
    email=models.EmailField(('email address'),unique=True)
    telefono=models.IntegerField()
    contraseña=models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    
class comentario(models.Model):
    nombre=models.CharField(max_length=100)
    email=models.EmailField('email address')
    comentario=models.CharField(max_length=300)

    def __str__(self):
        return self.nombre

