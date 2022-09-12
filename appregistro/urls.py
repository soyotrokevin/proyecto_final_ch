from django.urls import path
from appregistro import views

urlpatterns = [
    path('registro/', views.register, name="registro"),

]