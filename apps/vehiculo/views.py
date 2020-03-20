

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioVehiculo, FormularioHorario
from apps.vehiculo.models import Vehiculo,HorarioA
import datetime

def principal(request):
    listaHorario = HorarioA.objects.all()
    context={
        'lh': listaHorario,
    }
    
    return render(request,'principal.html', context)

def registrarVehiculo(request):
    usuario = request.user#peticion que es procesada x el frmawor agrega el usuario
    if usuario.groups.filter(name = 'administrativo').exists():
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
    else:
        messages.warning(request, 'No tienes acceso a estas funciones')
        return redirect('/')                 
    
        
    context = {
        'f': formulario 
    }

    return render(request,'vehiculo/registrar_vehiculo.html', context),usuario.groups.filter(name = 'administrativo').exists() 



def verVehiculo(request):
    lista = Vehiculo.objects.all()
    context={
        'l': lista,
    }
    return render(request,'vehiculo/ver_vehiculo.html', context) 

def agregarHorario(request):
    placaA = request.GET.get('dato')
    now = datetime.date.today()
    vehiculos = Vehiculo.objects.filter(vehiculo_id = placaA)
    formularioH = FormularioHorario(request.POST)
    if request.method == 'POST':
        if formularioH.is_valid():
            datos = formularioH.cleaned_data
            if  datos.get('fecha_recogida') >= now:
                horario = HorarioA()
                horario.fecha_recogida = datos.get('fecha_recogida')
                horario.fecha_devolucion = datos.get('fecha_devolucion')
                horario.hora_recogida = datos.get('hora_recogida')
                horario.precio_total = datos.get('precio_total')
                horario.dias = datos.get('dias')
                horario.vehiculo = Vehiculo.objects.get(vehiculo_id = placaA)
                horario.save()
                messages.success(request, 'Horario registrado correctamente')
                return redirect('/verHorario')
            else:
                messages.error(request, 'La fecha debe ser mayor a hoy')
    context={
        'f': formularioH,
        'v':vehiculos,
    }
 
    return render(request,'vehiculo/agregar_alquiler.html', context)

def verHorario(request):
    listaH = HorarioA.objects.all()
    context={
        'h':listaH,
    }
    return render(request,'vehiculo/listar_horario.html', context)




    