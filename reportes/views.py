from subprogramas.models import Subprograma
from programas.models import Programa
from proyectos.models import Proyectos
from django.views.generic import ListView, TemplateView
from django_weasyprint import WeasyTemplateResponseMixin
from django.conf import settings


class EscogeReporte(TemplateView):
    template_name = "reportes/reportes.html"
    modulos = [
        {'tipo_modulo': 'Programas', 'url_name': 'programa_lista_pdf'},
        {'tipo_modulo': 'Subprogramas', 'url_name': 'subprograma_lista_pdf'},
        {'tipo_modulo': 'Proyectos', 'url_name': 'proyecto_lista_pdf'}, ]
    extra_context = {'modulos': modulos}


# --------------------------------SUBPROGRAMAS
class ListaSubprogramaPDF(ListView):
    model = Subprograma
    template_name = 'reportes/ListaSubprogramaPDF.html'


class SubprogramasPDF(WeasyTemplateResponseMixin, ListaSubprogramaPDF):
    pdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + 'css/bootstrap.min.css',
    ]
    pdf_attachment = False
    pdf_filename = 'subprogramas.pdf'


# --------------------------------PROGRAMAS
class ListaProgramaPDF(ListView):
    model = Programa
    template_name = 'reportes/ListaProgramaPDF.html'


class ProgramasPDF(WeasyTemplateResponseMixin, ListaProgramaPDF):
    pdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + 'css/bootstrap.min.css',
    ]
    pdf_attachment = False
    pdf_filename = 'programas.pdf'


# --------------------------------PROYECTOS
class ListaProyectosPDF(ListView):
    model = Proyectos
    template_name = 'reportes/ListaProyectoPDF.html'


class ProyectosPDF(WeasyTemplateResponseMixin, ListaProyectosPDF):
    pdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + 'css/bootstrap.min.css',
    ]
    pdf_attachment = False
    pdf_filename = 'proyectos.pdf'
