

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioVehiculo
from apps.vehiculo.models import Vehiculo

def principal(request):
    
    return render(request,'principal.html')

def registrarVehiculo(request):
    formulario = FormularioVehiculo(request.POST, request.FILES)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            vehiculo = Vehiculo()
            vehiculo.placa = datos.get('placa')
            vehiculo.marco = datos.get('marca')
            vehiculo.modelo = datos.get('modelo')
            vehiculo.transmision = datos.get('transmision')
            vehiculo.nro_puertas = datos.get('nro_puertas')
            vehiculo.nro_asientos = datos.get('nro_asientos')
            vehiculo.tipo_vehiculo = datos.get('tipo_vehiculo')
            vehiculo.aire_acondicionado = datos.get('aire_acondicionado')
            vehiculo.imagen = datos.get('imagen')
            vehiculo.save()
            messages.success(request, 'Vehiculo registrado correctamente')
            
        else:
            messages.error(request, 'Vehiculo con la placa ya registrado')
                 
    
        
    context = {
        'f': formulario 
    }

    return render(request,'vehiculo/registrar_vehiculo.html', context) 



def verVehiculo(request):
    lista = Vehiculo.objects.all()
    context={
        'l': lista,
    }
    return render(request,'vehiculo/ver_vehiculo.html', context) 


    