from django.shortcuts import render


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
    return render(request, 'web/registro.html')

def iniciarsesion(request):
    return render(request, 'web/iniciarsesion.html')

