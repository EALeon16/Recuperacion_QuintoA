from django import forms 
from apps.vehiculo.models import Alquiler
class FormularioAlquiler(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ["fecha_alquiler", "hora_recogida"]







        





