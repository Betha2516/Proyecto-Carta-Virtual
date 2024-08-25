from django.shortcuts import render, HttpResponse
from .models import Entrada, Bebida, PlatoF, Postre, Ubicaciones
# Create your views here.
#request -> response

def home(request):
    return render(request, "home.html")

def carta(request):
    entradas = Entrada.objects.all()
    platosf = PlatoF.objects.all()
    bebidas = Bebida.objects.all()
    postres = Postre.objects.all()
    return render(request, "carta.html", {"entradas": entradas, "platosf": platosf, "bebidas": bebidas, "postres": postres})

def ubicaciones(request):
    ubicaciones = Ubicaciones.objects.all()
    return render(request, "ubicaciones.html", {"ubicaciones": ubicaciones})

def registro(request):
    return render(request, "registro.html")
