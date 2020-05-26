from django.urls import reverse_lazy
from .models import Subprograma
from . import forms
from django.views.generic.edit import (
    CreateView, UpdateView,
)
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class ListaSubprogramaPDF(ListView):
    model = Subprograma


# class NuevoSubprugrama(
# LoginRequiredMixin,
# PermissionRequiredMixin,
# CreateView):
class NuevoSubprugrama(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = ('subprogramas.add_subprograma')
    login_url = 'usuarios/login/'
    success_message = "Subprograma agregado exitosamente"
    model = Subprograma
    form_class = forms.SubprogramaForm
    success_url = reverse_lazy('lista_subprograma')


class ListaSubprogramas(PermissionRequiredMixin, ListView):
    permission_required = ('subprogramas.view_subprograma')
    login_url = 'usuarios/login/'
    model = Subprograma


class VerSubprograma(PermissionRequiredMixin, DetailView):
    permission_required = ('subprogramas.view_subprograma')
    login_url = 'usuarios/login/'
    model = Subprograma


class EditarSubprograma(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = ('subprogramas.change_subprograma')
    login_url = 'usuarios/login/'
    form_class = forms.EdicionSubprogramaForm
    model = Subprograma
    success_message = "Datos del subprograma modificados correctamente"
    success_url = reverse_lazy('lista_subprograma')
