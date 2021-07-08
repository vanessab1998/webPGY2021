from rest_framework import serializers
from core.models import usuario


class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ['nombre','rut','email','telefono','contraseña']