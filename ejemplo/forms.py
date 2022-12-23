from django import forms
from ejemplo.models import Familiar
from ejemplo.models import Mascotas

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Busque algo...'})) #queda un mensaje clarito en el box

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']
