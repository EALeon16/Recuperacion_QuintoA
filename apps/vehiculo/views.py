

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages

def principal(request):
    
    return render(request,'principal.html')


def registrarVehiculo(request):
    

    return render(request,'vehiculo/registrar_vehiculo.html')   

    