from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import FormularioLogin
from django.contrib import messages




def ingresar(request):
    if request.method == 'POST':
        formularioL = FormularioLogin(request.POST)
        if formularioL.is_valid():
            email = request.POST['email']
            clave = request.POST['clave']
            user = authenticate(username = email, password = clave)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('vehiculo'))
                else:
                    messages.success(request, 'Usuario desactivado')
            else:
                messages.error(request, 'Usuario y/o contrasenia incorrecto')
               
            
    else:
        formularioL = FormularioLogin()

    context = {
        'formularioL': formularioL,
            }
    return render (request, 'Login/iniciar_sesion.html', context)
