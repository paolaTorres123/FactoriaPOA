from .models import (Proyectos, Actividades, LONGUITUD_MAXIMA,
                     FORMATO_CARACTER_INCORRECTO, FORMATO_NUMERO_INCORRECTO,
                     VALOR_MAXIMO, VALOR_MINIMO, VALOR_MAXIMO_CAN,
                     LONGUITUD_MAXIMA_SALDO)
from django.forms import ModelForm, TextInput, Select, NumberInput


class ProyectoForm(ModelForm):
    class Meta:
        model = Proyectos
        exclude = ['activo']

        widgets = {
            'nombre_proyecto': TextInput(attrs={'class': 'form-control'}),
        }

        error_messages = {
            'nombre_proyecto': {'max_length': LONGUITUD_MAXIMA,
                                'required': 'Campo requerido',
                                'invalid': FORMATO_CARACTER_INCORRECTO
                                },
        }

    def save(self, commit=True):
        actividades = super(ProyectoForm, self).save(commit=False)
        if commit:
            actividades.save()
        return actividades


class ActividadesForm(ModelForm):
    class Meta:
        model = Actividades
        exclude = ['proyecto']

        widgets = {
            'nombre_actividad': TextInput(attrs={'class': 'form-control'}),
            'unidad_medida': Select(attrs={'class': 'form-control'}),
            'cantidad': NumberInput(attrs={'class': 'form-control'}),
            'saldo': NumberInput(attrs={'class': 'form-control'}),

        }
        error_messages = {
            'nombre_actividad': {
                'max_length': LONGUITUD_MAXIMA,
                'required': 'Requerido',
                'invalid': FORMATO_CARACTER_INCORRECTO
            },
            'unidad_medida': {
                'max_length': LONGUITUD_MAXIMA,
                'required': 'Requerido'
            },
            'cantidad': {
                'max_length': LONGUITUD_MAXIMA,
                'required': 'Requerido',
                'invalid': FORMATO_NUMERO_INCORRECTO,
                'invalid': VALOR_MAXIMO_CAN,
                'invalid': VALOR_MINIMO
            },
            'saldo': {
                'max_digits': LONGUITUD_MAXIMA_SALDO,
                'required': 'Requerido',
                'invalid': FORMATO_NUMERO_INCORRECTO,
                'invalid': VALOR_MAXIMO,
                'invalid': VALOR_MINIMO
            }
        }
