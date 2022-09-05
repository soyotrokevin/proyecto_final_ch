from django import forms


class marcas_Formulario(forms.Form):
    nombre = forms.CharField(max_length=128)