
from django.shortcuts import render, redirect
from .models import Proyectos, Actividades
from .forms import ProyectoForm, ActividadesForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

# Create your views here.


class NuevoProyecto(PermissionRequiredMixin, CreateView):
    permission_required = ('proyectos.add_proyectos')
    login_url = 'usuarios/login/'
    model = Proyectos
    form_class = ProyectoForm
    success_url = reverse_lazy('lista_proyectos')
    extra_context = {'actividad_form': ActividadesForm()}
    template_name = 'proyectos/proyectos_form.html'

    def form_valid(self, form):
        actividad_form = ActividadesForm(self.request.POST, self.request.FILES)
        if actividad_form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.is_active = False
            proyecto.save()

            actividad = actividad_form.save(commit=False)
            actividad.proyecto = proyecto
            actividad.save()
        else:
            return self.render_to_response(
                self.get_context_data(
                    form=form, extra_context=actividad_form))
        return super().form_valid(form)

    def form_invalid(self, form):
        actividad_form = ActividadesForm(self.request.POST, self.request.FILES)
        return self.render_to_response(
            self.get_context_data(
                form=form,
                extra_context=actividad_form))

    def get_context_data(self, **kwargs):
        if 'extra_context' in kwargs:
            self.extra_context = {'actividad_form': kwargs['extra_context']}
        return super().get_context_data(**kwargs)


@permission_required('proyectos.view_proyectos')
def DesactivarProyecto(request, id):
    proyectos = Proyectos.objects.get(pk=id)
    if proyectos.activo:
        proyectos.activo = False
        proyectos.save()
        messages.success(request, 'Proyecto desactivado con exito.')
        return redirect('lista_proyectos')
    messages.success(request, 'No es posible desactivar el proyecto')
    return redirect('lista_proyectos')


@permission_required('proyectos.view_proyectos')
def ReactivarProyecto(request, id):
    proyectos = Proyectos.objects.get(pk=id)
    if not proyectos.activo:
        proyectos.activo = True
        proyectos.save()
        messages.success(request, 'Proyecto activado con exito.')
        return redirect('lista_proyectos')
    messages.success(request, 'No es posible activar el proyecto')
    return redirect('lista_proyectos')


@permission_required('proyectos.change_proyectos')
def editar_proyecto(request, id):
    proyectos = Proyectos.objects.get(pk=id)
    if request.method == 'POST':
        proyecto_form = ProyectoForm(data=request.POST, instance=proyectos)
        if proyecto_form.is_valid():
            proyecto_form.save()
            messages.success(request, 'Proyecto modificado con exito.')
            return redirect('lista_proyectos')
    else:
        proyecto_form = ProyectoForm(instance=proyectos)
    return render(request, 'proyectos/proyectos_edit.html', {
        'proyecto_form': proyecto_form,
    })


class ListaProyecto(PermissionRequiredMixin, ListView):
    permission_required = ('proyectos.view_proyectos')
    login_url = 'usuarios/login/'
    model = Proyectos


def agregar_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_actividad')
    else:
        form = ProyectoForm()

    form = ProyectoForm()
    return render(request, 'nuevo.html', {'form': form})


@permission_required('proyectos.add_actividades')
def agregar_actividad(request):
    if request.method == 'POST':
        form = ActividadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_actividad')
    return render(request, 'nuevo.html', {'form': form})


@permission_required('proyectos.view_actividades')
def lista_actividad(request, id):
    Proyectos.objects.get(pk=id)
    actividad = Actividades.objects.filter(proyecto=id)
    context = {'actividades': actividad}

    return render(request, 'actividad/actividades_list.html', context)
