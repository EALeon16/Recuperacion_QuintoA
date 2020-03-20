# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioAlquiler
from apps.vehiculo.models import Vehiculo,HorarioA, Persona
import datetime

def alquiler(request):
    horario = request.GET.get('id')
    now = datetime.date.today()         
    p = Persona.objects.all()           

          

    context = {
        'p':p,
    }
    
    return render(request,'alquiler/alquilar_vehiculo.html', context)
