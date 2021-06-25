from core.models import usuario
from django.shortcuts import render,redirect
from .forms import registrousuaro
from django.contrib import messages

# Create your views here.

def base(request):
    return render(request, 'web/base.html')

def index(request):
    return render(request, 'web/index.html')

def tejido(request):
    return render(request, 'web/tejido.html')

def pinturas(request):
    return render(request, 'web/pinturas.html')

def miapi(request):
    return render(request, 'web/miapi.html')

def registro(request):
    regusuario = registrousuaro()
    data = {'form' : regusuario}
    if request.method == 'POST':
        regusuario = registrousuaro(data = request.POST) 
        if regusuario.is_valid():
            regusuario.save()
            print("Usuario Creado Correctamente")
            mensaje = "Usuario Creado Correctamente"
            messages.success(request, mensaje)
            return redirect('index')
        else:
            data["form"] = regusuario;  
    else:
        print("No se puedo crear el usuario, revisa los datos")
        mensaje = "No se puedo crear el usuario, revisa los datos"
        messages.error(request, mensaje)

    return render(request, 'web/registro.html',data)

def iniciarsesion(request):
    return render(request, 'web/iniciarsesion.html')

def crudusuario(request):
    usuarios=usuario.objects.all()
    data={'usuarios':usuarios}
    return render(request, 'web/crudusuario.html',data)

def borrarusuario(request, email):
    usuarios = usuario.objects.get(email = email)
    usuarios.delete()
    return redirect(to="crudusuario")

def editarusuario(request, iduser):
    usuarios = usuario.objects.get(id=iduser)
    datos = {
        'form': registrousuaro(instance=usuarios) 
        }
    if request.method == 'POST':
        formulario_edit = registrousuaro(data=request.POST, instance=usuarios)
        if formulario_edit.is_valid:
            formulario_edit.save()
            datos['mensaje'] = "Usuario editado Correctamente"
            return redirect('crudusuario')
    return render(request, 'web/editarusuario.html', datos)