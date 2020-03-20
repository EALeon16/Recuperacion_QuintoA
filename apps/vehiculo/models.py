from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Vehiculo(models.Model):

    listaT =(
        ('Manual', 'Manual'),
        ('Automatica', 'Automatica'),
            
    )
        
    AireAcondicionado =(
        ('si', 'Si'),
        ('no', 'No'),
        
            
    )

    
    vehiculo_id = models.AutoField(primary_key = True)
    placa = models.CharField(max_length=75, unique = True, null=False)
    marca = models.CharField(max_length=50, null=False)
    modelo = models.CharField(max_length=50, null=False)
    transmision = models.CharField(max_length=35, choices = listaT, default= 'Manual', null=False)
    nro_puertas =  models.IntegerField(max_length=10, null=False)
    nro_asientos =  models.IntegerField(max_length=10, null=False)
    tipo_vehiculo =  models.CharField(max_length=50, null=False)
    aire_acondicionado = models.CharField(max_length=15,null=False, choices = AireAcondicionado)
    imagen = models.ImageField(upload_to="portadas", null=True)

class HorarioA(models.Model):
    horarioA_id = models.AutoField(primary_key = True)
    fecha_recogida =  models.DateField(auto_now = False, auto_now_add = False, null = True)
    hora_recogida =  models.TimeField(null=False)
    dias =  models.IntegerField(max_length=10, null=False)
    fecha_devolucion =  models.DateField(auto_now = False, auto_now_add = False, null = True)
    hora_recogida =  models.TimeField(null=False)
    precio_total = models.DecimalField(max_digits=10, decimal_places=3, null=False)
    vehiculo = models.ForeignKey(
        'Vehiculo', 
        on_delete = models.CASCADE,
    )    
