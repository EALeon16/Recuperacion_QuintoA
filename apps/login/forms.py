from django import forms
class FormularioLogin(forms.Form):
	email = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su direccion de correol'}),
								label='Usuario')
	clave = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese su contrasenia'}),
								label='Clave')
