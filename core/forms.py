from django import forms
from .models import usuario,comentario


class registrousuaro(forms.ModelForm):
    class Meta : 
        model = usuario
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'nombre'}),
            'rut': forms.TextInput(attrs={'placeholder': 'rut'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'telefono'}),
            'email': forms.TextInput(attrs={'placeholder': 'email'}),
            'contraseña': forms.TextInput(attrs={'placeholder': 'contraseña'}),
        }

class addcomentario(forms.ModelForm):
    class Meta : 
        model = comentario
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'nombre'}),
            'email': forms.TextInput(attrs={'placeholder': 'email'}),
            'comentario': forms.TextInput(attrs={'placeholder': 'comentario'}),
        }