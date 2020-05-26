from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('nuevo', permission_required('subprogramas.add_subprograma')(
        views.NuevoSubprugrama.as_view()), name="nuevo_subprograma"),
    path('', permission_required('subprogramas.view_subprograma')(
        views.ListaSubprogramas.as_view()), name="lista_subprograma"),
    path('editar/<int:pk>', 
        permission_required('subprogramas.change_subprograma')
        (views.EditarSubprograma.as_view()),
        name="editar_subprograma"),
    path(
        'ver/<int:pk>',
        permission_required('subprogramas.view_subprograma')(
            views.VerSubprograma.as_view()),
        name="ver_subprograma"),
]
