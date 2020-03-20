from django import forms 
from apps.vehiculo.models import Alquiler
class FormularioAlquiler(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = [ "hora_recogida", "persona"]







        





