# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioAlquiler
from apps.vehiculo.models import Vehiculo,HorarioA, Persona, Alquiler
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def alquiler(request):
    horario = request.GET.get('id')
    now = datetime.date.today()         
    p = Persona.objects.all()
    horarios = HorarioA.objects.get(horarioA_id = horario)
    form = FormularioAlquiler(request.POST)
    usuario = request.user#peticion que es procesada x el frmawor agrega el usuario
    if usuario.groups.filter(name = 'atencion_cliente').exists():
        if request.method == 'POST':
            if form.is_valid():
                alquiler = Alquiler()
                datos = form.cleaned_data
                alquiler.hora_recogida = datos.get('hora_recogida')
                alquiler.persona = datos.get('persona')
                alquiler.horario = horarios
                alquiler.save()
                messages.success(request, 'Vehixulo alquilado correctamente')
                
            else:
                messages.error(request, 'Error al registrar alquiler')
    else:
        messages.warning(request, 'No tienes acceso a estas funciones')
        return redirect('/')



          

    context = {
        'p':p,
        'n':now,
    }
    
    return render(request,'alquiler/alquilar_vehiculo.html', context)
@login_required
def allAlquileres(request):
    usuario = request.user#peticion que es procesada x el frmawor agrega el usuario
    if usuario.groups.filter(name = 'gerente').exists():
        listaA = Alquiler.objects.all()
    else:
        messages.warning(request, 'No tienes acceso a estas funciones')
        return redirect('/')

    context = {
        'al':listaA,
    }
    return render(request,'alquiler/all_historial.html', context)

