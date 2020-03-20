# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioAlquiler
from apps.vehiculo.models import Vehiculo,HorarioA, Persona, Alquiler
import datetime

def alquiler(request):
    horario = request.GET.get('id')
    now = datetime.date.today()         
    p = Persona.objects.all()
    horarios = HorarioA.objects.get(horarioA_id = horario)
    total_paid = list(Alquiler.objects.filter(horario_id = horario).values())[0]
    form = FormularioAlquiler(request.POST)
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



          

    context = {
        'p':p,
        'n':now,
    }
    
    return render(request,'alquiler/alquilar_vehiculo.html', context)

def allAlquileres(request):
    listaA = Alquiler.objects.all()
    context = {
        'al':listaA,
    }
    return render(request,'alquiler/all_historial.html', context)

