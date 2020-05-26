from .models import Subprograma
from django.forms import ModelForm, TextInput, Select, NumberInput


class SubprogramaForm(ModelForm):
    class Meta:
        model = Subprograma
        exclude = ['estatus']
        widgets = {
            'programa': Select(attrs={'class': 'form-control'}),
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'presupuesto': NumberInput(attrs={'class': 'form-control'}),
            'responsable': Select(attrs={'class': 'form-control'}),
        }


class EdicionSubprogramaForm(ModelForm):
    class Meta:
        model = Subprograma
        fields = "__all__"
        widgets = {
            'programa': Select(attrs={'class': 'form-control'}),
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'presupuesto': NumberInput(attrs={'class': 'form-control'}),
            'responsable': Select(attrs={'class': 'form-control'}),
            'estatus': Select(attrs={'class': 'form-control'}),
        }
