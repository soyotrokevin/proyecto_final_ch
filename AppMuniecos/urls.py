from django.urls import path
from AppMuniecos import views

urlpatterns = [
    path('', views.inicio, name="AppMuniecos"),
]