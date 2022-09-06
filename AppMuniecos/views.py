from typing import Dict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppMuniecos.models import Ropa

# Create your views here.
def inicio(request):
    return render(request, "AppMuniecos/inicio.html")


def muniecos(request):
    muniecos = muniecos.objects.all()
    return render(request, "AppMuniecos/muniecos.html", {'Muñecos': muniecos})


def ropa(request):
    ropa = Ropa.objects.all()
    return render(request, "AppMuniecos/ropa.html")


def marcas(request):
    marcas = marcas.objects.all()
    return render(request, "AppMuniecos/marcas.html")

def usuarios(request):
    usuarios = usuarios.objects.all()
    return render(request, "AppCoder/usuarios.html")