from django.urls import path

from AppMuniecos import views

urlpatterns = [
    path('', views.inicio, name="AppMuniecos"),
    path('muniecos/', views.muniecos, name="muniecos"),
    path('ropa/', views.ropa, name="ropa"),
    path('marcas/', views.marcas, name="marcas"),
    path('usuarios', views.usuarios, name="usuarios"),
]