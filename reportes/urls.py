from django.urls import path
from reportes import views

urlpatterns = [
    path('', views.EscogeReporte.as_view(), name="escoge_reporte"),
    path('subprograma_lista_pdf', views.SubprogramasPDF.as_view(),
         name="subprograma_lista_pdf"),
    path('programa_lista_pdf', views.ProgramasPDF.as_view(),
         name="programa_lista_pdf"),
    path('proyecto_lista_pdf', views.ProyectosPDF.as_view(),
         name="proyecto_lista_pdf"),
]
