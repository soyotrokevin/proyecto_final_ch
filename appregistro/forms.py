from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    error_messages = {
        "password_mistmach": _("No concuerdan las Passwords"),
    }
    password1 = forms.CharField(
        label= ("Password"),
        strip= False,
        widget= forms.PasswordInput (attrs={"autocomplete": "new-password"}),
        help_text =password_validation.password_validatos_help_text_html(),
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
        fields_classes = {"usuario": UsernameField}

class UserRegisterForm(UserCreationForm):
    usuario = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']