from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('', permission_required('auth.view_user')(
        views.ListaUsuarios.as_view()), name='lista_usuarios'),
    path('nuevo', permission_required('auth.add_user')(
        views.NuevoUsuario.as_view()), name='nuevo_usuario'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('editar/<int:id>', views.editar_usuario, name='editar_usuario'),
    path('desactivar/<int:id>', permission_required('auth.view_user')
         (views.desactivar_usuario), name='desactivar_usuario'),
    path('reactivar/<int:id>', permission_required('auth.view_user')
         (views.activar_usuario), name='reactivar_usuario'),
]
