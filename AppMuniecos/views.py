from typing import Dict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

from AppMuniecos.models import Ropa, Marca, Munieco
from AppMuniecos.forms import MarcaFormulario, MuniecoFormulario, RopaFormulario

# Create your views here.
def inicio(request):
    return render(request, "AppMuniecos/inicio.html")


def muniecos(request):
    muniecos = Munieco.objects.all()
    return render(request, "AppMuniecos/muniecos.html", {'muniecos': muniecos})

def load_munieco(request):
    if request.method == 'POST':
        formulario= MuniecoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            munieco = Munieco(tipo=data['tipo'], origen=data['origen'])
            munieco.save()
            return render(request, "AppMuniecos/inicio.html", {"exitoso": True})
    else:  
        formulario= MuniecoFormulario()  
    return render(request, "AppMuniecos/form_load_munieco.html", {"formulario": formulario})

def ropa(request):
    ropa = Ropa.objects.all()
    return render(request, "AppMuniecos/ropa.html")

def load_ropa(request):
    if request.method == 'POST':
        formulario= RopaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            ropa = Ropa(prenda=data['prenda'], talle=data['talle'])
            ropa.save()
            return render(request, "AppMuniecos/inicio.html", {"exitoso": True})
    else:  
        formulario= RopaFormulario()  
    return render(request, "AppMuniecos/form_load_ropa.html", {"formulario": formulario})


def marcas(request):
    marcas = Marca.objects.all()
    return render(request, "AppMuniecos/marcas.html", {'marcas': marcas})


def load_marca(request):
    if request.method == 'POST':
        formulario= MarcaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            marca = Marca(nombre=data['nombre'])
            marca.save()
            return render(request, "AppMuniecos/inicio.html", {"exitoso": True})
    else:  # GET
        formulario= MarcaFormulario() 
    return render(request, "AppMuniecos/form_load_marcas.html", {"formulario": formulario})


def busqueda_marca(request):
    return render (request, "AppMuniecos/form_search_marca.html")


def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        marcas = Marca.objects.filter(nombre__icontains=nombre)
        return render(request, "AppMuniecos/marcas.html", {'marcas': marcas})
    else:
        return render(request, "AppMuniecos/marcas.html", {'marcas': []})
