from django import forms 
from apps.vehiculo.models import Vehiculo
class FormularioVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ["placa", "marca","modelo", "transmision", "nro_puertas","nro_asientos","tipo_vehiculo","aire_acondicionado","imagen"]







        





