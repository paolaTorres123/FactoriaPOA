from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaPrograma.as_view(), name='lista_programa'),
    path('nuevo', views.NuevoPrograma.as_view(), name="nuevo_programa"),
    path('editar/<int:id>', views.editar_programa, name='editar_programa'),
    path('desactivar/<int:id>', views.desactivar_programa,
         name='desactivar_programa'),
    path('reactivar/<int:id>', views.reactivar_programa,
         name='reactivar_programa'),
]
