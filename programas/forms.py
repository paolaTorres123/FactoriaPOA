from .models import (Programa, Partida, MetaPrograma,
                     MetaReal, LONGITUD_MAXIMA,
                     FORMATO_NUMERO_INCORRECTO)
from django.forms import ModelForm, TextInput, Select, NumberInput


class ProgramaForm(ModelForm):

    class Meta:
        model = Programa
        fields = "__all__"
        mensaje = 'El formato del recurso asignado es incorrecto,'
        mensaje += ' debe ser indicado con un número (indicando la cantidad)'

        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'anio_ejercicio_fiscal': NumberInput(attrs={
                'class': 'form-control'}),
            'recurso_asignado': NumberInput(attrs={'class': 'form-control'}),
            'fuente': TextInput(attrs={'class': 'form-control'}),
            'tipo': Select(attrs={'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-control'}),
            'tipo_programa_p': Select(attrs={'class': 'form-control'}),
        }

        error_messages = {
            'nombre': {'max_length': LONGITUD_MAXIMA,
                       'required': 'Se requiere dicho campo'},
            'anio_ejercicio_fiscal': {'invalid': FORMATO_NUMERO_INCORRECTO,
                                      'required': FORMATO_NUMERO_INCORRECTO},
            'recurso_asignado': {'max_digits': mensaje}
        }

    def save(self, commit=True):
        programa = super(ProgramaForm, self).save(commit=False)
        if commit:
            programa.save()
        return programa

# Pendiente Pruebas


class PartidaForm(ModelForm):

    class Meta:
        model = Partida
        exclude = ['programa']

        widgets = {
            'numero_partida': NumberInput(attrs={'class': 'form-control'}),
            'nombre_partida': TextInput(attrs={'class': 'form-control'}),
            'monto_partida': NumberInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        partida = super(PartidaForm, self).save(commit=False)
        if commit:
            partida.save()
        return partida

# Pendiente el de los modelos de Meta


class MetaForm(ModelForm):
    class Meta:
        model = MetaPrograma
        exclude = ['programa', 'meta_esperada']

        widgets = {
            'numero_actividades': NumberInput(attrs={'class': 'form-control'}),
            'numero_beneficiarios': NumberInput(attrs={
                                                'class': 'form-control'}),
            'numero_hombres': NumberInput(attrs={'class': 'form-control'}),
            'numero_mujeres': NumberInput(attrs={'class': 'form-control'}),
            'edad': Select(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        meta_prog = super(MetaForm, self).save(commit=False)
        if commit:
            meta_prog.save()
        return meta_prog


class MetaRealForm(ModelForm):
    class Meta:
        model = MetaReal
        exclude = ['programa_r', 'meta_esperada_r']

        widgets = {
            'numero_actividades_r': NumberInput(attrs={
                                                'class': 'form-control'}),
            'numero_beneficiarios_r': NumberInput(attrs={
                'class': 'form-control'}),
            'numero_hombres_r': NumberInput(attrs={'class': 'form-control'}),
            'numero_mujeres_r': NumberInput(attrs={'class': 'form-control'}),
            'edad_r': Select(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        meta_real = super(MetaRealForm, self).save(commit=False)
        if commit:
            meta_real.save()
        return meta_real
