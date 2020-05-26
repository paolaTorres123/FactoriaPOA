from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from .models import Programa, Partida, MetaPrograma, MetaReal
from .forms import ProgramaForm, PartidaForm, MetaForm, MetaRealForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView


# Create your views here.
class NuevoPrograma(SuccessMessageMixin, CreateView):
    model = Programa
    form_class = ProgramaForm
    success_url = reverse_lazy('lista_programa')
    success_message = "Programa creado con éxito"
    extra_context = {'partida_form': PartidaForm(),
                     'metas_esperadas_form': MetaForm(auto_id="id_%s_mp"),
                     'metas_reales_form': MetaRealForm(auto_id="id_%s_mr"), }
    template_name = 'programas/programa_form.html'

    def form_valid(self, form):
        partida_form = PartidaForm(self.request.POST)
        metas_esperadas_form = MetaForm(self.request.POST, auto_id="id_%s_mp")
        metas_reales_form = MetaRealForm(self.request.POST, auto_id="id_%s_mr")
        if (partida_form.is_valid() and metas_esperadas_form.is_valid()
                and metas_reales_form.is_valid()):  # Añadir más forms aquí
            programa = form.save(commit=False)
            programa.save()

            partida = partida_form.save(commit=False)
            partida.programa = programa
            partida.save()

            metas_esperadas = metas_esperadas_form.save(commit=False)
            metas_esperadas.programa = programa
            metas_esperadas.meta_esperada = True
            metas_esperadas.save()

            metas_reales = metas_reales_form.save(commit=False)
            metas_reales.programa_r = programa
            metas_reales.meta_esperada_r = False
            metas_reales.save()

        else:
            return self.render_to_response(self.get_context_data(form=form,
                                           extra_context={partida_form,
                                                          metas_esperadas_form,
                                                          metas_reales_form}))

        self.object = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        partida_form = PartidaForm(self.request.POST)
        metas_esperadas_form = MetaForm(self.request.POST)
        metas_reales_form = MetaRealForm(self.request.POST)
        return self.render_to_response(self.get_context_data(form=form,
                                       extra_context={partida_form,
                                                      metas_esperadas_form,
                                                      metas_reales_form}))

    def get_context_data(self, **kwargs):
        if 'extra_context' in kwargs:
            lista = list(kwargs['extra_context'])
            self.extra_context = {
                'partida_form': lista[0],
                'metas_esperadas_form': lista[1],
                'metas_reales_form': lista[2]}
        return super().get_context_data(**kwargs)


class ActualizaPrograma(UpdateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'programas/programa_edit.html'
    success_url = reverse_lazy('lista_programa')


def editar_programa(request, id):
    programa = Programa.objects.get(pk=id)
    partida = Partida.objects.get(programa=id)
    metas_esperadas = MetaPrograma.objects.get(programa=id)
    metas_reales = MetaReal.objects.get(programa_r=id)

    if request.method == 'POST':

        programa_form = ProgramaForm(data=request.POST, instance=programa)
        partida_form_c = PartidaForm(data=request.POST, instance=partida)
        metas_esperadas_form = MetaForm(
            data=request.POST, instance=metas_esperadas)
        metas_reales_form = MetaRealForm(
            data=request.POST, instance=metas_reales)

        if (programa_form.is_valid() and partida_form_c.is_valid()
                and metas_reales_form.is_valid()
                and metas_esperadas_form.is_valid()):
            programa_f = programa_form.save(commit=False)
            programa_f.save()

            partida_f = partida_form_c.save(commit=False)
            partida_f.save()

            metas_esperadas_f = metas_esperadas_form.save(commit=False)
            metas_esperadas_f.save()

            metas_reales_f = metas_reales_form.save(commit=False)
            metas_reales_f.save()
            messages.success(request, 'Programa modificado exitosamente.')
            return redirect('lista_programa')
    else:
        programa_form = ProgramaForm(instance=programa)
        partida_form_c = PartidaForm(instance=partida)
        metas_esperadas_form = MetaForm(instance=metas_esperadas)
        metas_reales_form = MetaRealForm(instance=metas_reales)

    return render(request, 'programas/programa_edit.html', {
        'programa_form': programa_form,
        'partida_form_c': partida_form_c,
        'metas_esperadas_form': metas_esperadas_form,
        'metas_reales_form': metas_reales_form
    })


class ListaPrograma(ListView):
    model = Programa


def desactivar_programa(request, id):
    programa = Programa.objects.get(pk=id)
    if programa.status.upper() == 'ACT':
        programa.status = 'INA'
        programa.save()
        messages.success(
            request, 'Programa seleccionado se ha desactivado con éxito')
        return redirect('lista_programa')
    mensaje = 'No fue posible desactivar el programa en este momento,'
    mensaje += ' debido a un error interno. Favor de intentarlo más tarde.'
    messages.success(
        request,
        mensaje)
    return redirect('lista_programa')


def reactivar_programa(request, id):
    programa = Programa.objects.get(pk=id)
    if programa.status.upper() != 'ACT':
        programa.status = 'ACT'
        programa.save()
        messages.success(request, 'Programa seleccionado reactivado con éxito')
        return redirect('lista_programa')
    mensaje = 'No fue posible reactivar el programa en este momento,'
    mensaje += ' debido a un error interno. Favor de intentarlo más tarde.'
    messages.success(
        request, mensaje)
    return redirect('lista_programa')
