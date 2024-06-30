from django import forms
from .models import Cliente
from django.forms import ModelForm

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apaterno', 'amaterno', 'email', 'fono']