from django.urls import path

from AppMuniecos import views

urlpatterns = [
    path('', views.inicio, name="AppMuniecos"),
    path('muñecos/', views.muniecos, name="muñecos"),
    path('ropa/', views.ropa, name="ropa"),
    path('marcas/', views.marcas, name="marcas"),
    path('usuarios', views.usuarios, name="usuarios"),
]