from django.urls import path
from appregistro import views

urlpatterns = [
    path('register/', views.registro),

]