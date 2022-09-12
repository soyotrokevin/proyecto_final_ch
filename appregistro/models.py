from django.db import models
from django import forms
from AppMuniecos import forms

# Create your models here.
class User(models.Model):
    usuario = models.CharField()
    email = models.EmailField()

class UserCreationForm(forms.ModelForm):
    error_messages = {
        "password_mistmach": _("No concuerdan las Passwords"),
    }
    password1 = forms.CharField(
        label= ("Password"),
        strip= False,
        widget= forms.PasswordInput (attrs={"autocomplete": "new-password"}),
        #help_text =password_validation.password_validatos_help_text_html(),
    )

    password2 = forms.CharField(
        label= ("Confirmación Password"),
        widget= forms.PasswordInput (attrs={"autocomplete": "new-password"}),
        strip= False,
        help_text = ("Ingrese la Password nuevamente, para su verificación"),
    )

    class Meta:
        model = User
        fields = ("usuario",)
        #fields_classes = {"usuario": UsernameField}