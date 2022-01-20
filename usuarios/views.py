from django.shortcuts import render, redirect
from .models import Usuario
from .forms import CreateUserForm


# Create your views here.

def usuariolist(request):
    usuarios = Usuario.objects.all()

    context = {
        'usuarios' : usuarios
    }

    return render(request, 'usuario/usuariolist.html' , context)


def createUser(request):    
    context ={
        'form' : CreateUserForm
    }
    if request.method == 'POST':
        formulario = CreateUserForm(context = request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to = 'home')
        else:
            context['form'] = formulario

    return render(request, 'usuario/createUser.html', context)