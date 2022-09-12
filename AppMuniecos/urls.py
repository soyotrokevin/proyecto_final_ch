from django.urls import path

from AppMuniecos import views

urlpatterns = [
    path('', views.inicio, name="AppMuniecos"),
    
    path('muniecos/', views.muniecos, name="muniecos"),
    path('form_load_munieco/', views.load_munieco, name="form_load_munieco"),

    path('ropa/', views.ropa, name="ropa"),
    path('form_load_ropa/', views.load_ropa, name="form_load_ropa"),

    path('marcas/', views.marcas, name="marcas"),
    path('form_load_marcas/', views.load_marca, name="form_load_marcas"),
    path('form_search_marca/', views.busqueda_marca, name="form_search_marca"),
    path('busqueda-marca/', views.buscar, name="busqueda"),

]