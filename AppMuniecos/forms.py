from django import forms

class MarcaFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)

class MuniecoFormulario(forms.Form):
    tipo = forms.CharField(max_length=128)
    origen = forms.CharField(max_length=64)
   
class RopaFormulario(forms.Form):
    prenda = forms.CharField(max_length=64)
    talle = forms.IntegerField()    

