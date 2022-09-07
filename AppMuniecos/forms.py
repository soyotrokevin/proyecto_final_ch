from django import forms

class MarcaFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)