from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Administrativo
from .forms import UserForm, LoginForm, AdministrativoForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group


class NuevoUsuario(PermissionRequiredMixin, CreateView):
    permission_required = ('auth.add_user')
    login_url = 'usuarios/login/'
    model = User
    form_class = UserForm
    extra_context = {'administrativo_form': AdministrativoForm()}
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('lista_usuarios')

    def form_valid(self, form):
        administrativo_form = AdministrativoForm(
            self.request.POST, self.request.FILES)
        if administrativo_form.is_valid() and form.is_valid():
            user = form.save(commit=False)
            user.save()
            if user.is_superuser:
                group = Group.objects.get(name='director_operativo')
            else:
                group = Group.objects.get(name='encargado_subprograma')
            user.groups.add(group)
            administrativo = administrativo_form.save(commit=False)
            administrativo.usuario = user
            administrativo.save()
        else:
            return self.render_to_response(
                self.get_context_data(
                    form=form, extra_context=administrativo_form))

        self.object = form.save()
        messages.success(
            self.request, 'Cuenta creada con éxito, el propietario de la '
                          + 'cuenta debe verificar su correo electrónico para'
                          + ' activar su cuenta.')
        return super().form_valid(form)

    def form_invalid(self, form):
        administrativo_form = AdministrativoForm(
            self.request.POST, self.request.FILES)
        return self.render_to_response(
            self.get_context_data(
                form=form, extra_context=administrativo_form))

    def get_context_data(self, **kwargs):
        if 'extra_context' in kwargs:
            self.extra_context = {
                'administrativo_form': kwargs['extra_context']}
        return super().get_context_data(**kwargs)


class ListaUsuarios(PermissionRequiredMixin, ListView):
    permission_required = ('auth.view_user')
    login_url = 'usuarios/login/'
    model = Administrativo
    template_name = 'usuarios/usuarios.html'

    def get(self, request, *args, **kwargs):
        administrativos = Administrativo.objects.all()
        admins = []
        for admin in administrativos:
            admins.append({'admin': admin, 'usuario': admin.usuario})
        self.object_list = admins
        context = self.get_context_data()
        return self.render_to_response(context)


class Login(LoginView):
    template_name = "usuarios/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('lista_usuarios')


def editar_usuario(request, id):
    administrativo = Administrativo.objects.get(usuario=id)
    if request.method == 'POST':
        admin_form = AdministrativoForm(
            data=request.POST, instance=administrativo)
        if admin_form.is_valid():
            admin_form.save()
            messages.success(
                request, 'Perfil de usuario modificado exitosamente.')
            return redirect('lista_usuarios')
    else:
        admin_form = AdministrativoForm(instance=administrativo)
    return render(
        request, 'usuarios/editar_usuario.html', {'admin_form': admin_form})


@permission_required('auth.view_user')
def desactivar_usuario(request, id):
    user = User.objects.get(pk=id)
    if user.is_active:
        user.is_active = False
        user.save()
        messages.success(request, 'Cuenta desactivada con éxito.')
        return redirect('lista_usuarios')
    messages.success(
        request, 'No es posible desactivar la cuenta. Intente más tarde.')
    return redirect('lista_usuarios')


@permission_required('auth.view_user')
def activar_usuario(request, id):
    user = User.objects.get(pk=id)
    if not user.is_active:
        user.is_active = True
        user.save()
        messages.success(request, 'Cuenta activada con éxito.')
        return redirect('lista_usuarios')
    messages.success(
        request, 'No es posible activar la cuenta. Intente más tarde.')
    return redirect('lista_usuarios')
