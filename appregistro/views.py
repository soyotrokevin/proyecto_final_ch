from django.shortcuts import render
from appregistro.forms import UserRegisterForm

# Create your views here.
def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "appregistro/inicio.html", {"mensaje": "Registro Exitoso"})
        else:
            mensaje = 'Error en registro'
    formulario = UserRegisterForm()
    context = {
        'form': formulario,
        'mensaje': mensaje
    }

    return render(request, "appregistro/registro.html", context=context)