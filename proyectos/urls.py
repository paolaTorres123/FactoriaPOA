from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('nuevo', permission_required('proyectos.add_proyectos')
         (views.NuevoProyecto.as_view()),
         name='nuevo_proyecto'),
    path('', permission_required('proyectos.view_proyectos')
         (views.ListaProyecto.as_view()),
         name='lista_proyectos'),
    path('actividades/<int:id>',
         permission_required('proyectos.view_actividades')
         (views.lista_actividad),
         name='lista_actividad'),
    path('desactivar/<int:id>', permission_required('proyectos.view_proyectos')
         (views.DesactivarProyecto),
         name='desactivar_proyectos'),
    path('activar/<int:id>', permission_required('proyectos.view_proyectos')
         (views.ReactivarProyecto),
         name='activar_proyectos'),
    path('', permission_required('proyectos.add_actividades')
         (views.agregar_actividad),
         name='agregar_actividad'),
    path('editar/<int:id>', permission_required('proyectos.change_proyectos')
         (views.editar_proyecto),
         name='editar_proyectos'),

]
