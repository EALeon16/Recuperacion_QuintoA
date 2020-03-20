from django import forms 
from apps.vehiculo.models import Vehiculo, HorarioA
class FormularioVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ["placa", "marca","modelo", "transmision", "nro_puertas","nro_asientos","tipo_vehiculo","aire_acondicionado","imagen"]
class FormularioHorario(forms.ModelForm):
    class Meta:
        model = HorarioA
        fields = ["fecha_recogida", "fecha_devolucion","dias",  "precio_total"]        







        





