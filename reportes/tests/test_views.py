from django.test import TestCase
from django.urls import reverse


class SubprogramaViewTests(TestCase):

    """
    Vista Agregar subprograma
    """

    def test_vistaEscogerPDF_url(self):
        response = self.client.get('/reportes/')
        self.assertEqual(response.status_code, 200)

    def test_vistaEscogerPDF_nombre_url(self):
        response = self.client.get(reverse('escoge_reporte'))
        self.assertEqual(response.status_code, 200)

    def test_vistaEscogerPDF_html_correcto(self):
        response = self.client.get('/reportes/')
        self.assertTemplateUsed(response, 'reportes/reportes.html')

    def test_vistaSubprograma_PDF_carga_datos(self):
        response = self.client.get(reverse('escoge_reporte'))
        self.assertIn('modulos', response.context)

    '''
    Vista Programa PDF
    '''

    def test_vistaProgramas_PDF_url(self):
        response = self.client.get(f'/reportes/programa_lista_pdf')
        self.assertEqual(response.status_code, 200)

    def test_vistaProgramas_PDFr_nombre_url(self):
        response = self.client.get(reverse('programa_lista_pdf'))
        self.assertEqual(response.status_code, 200)

    def test_vistaProgramas_PDF_html_correcto(self):
        response = self.client.get(reverse('programa_lista_pdf'))
        self.assertTemplateUsed(response, 'reportes/ListaProgramaPDF.html')

    def test_vistaPrograma_PDF_carga_datos(self):
        response = self.client.get(reverse('programa_lista_pdf'))
        self.assertIn('object_list', response.context)

    '''
    Vista Subprograma PDF
    '''

    def test_vistaSubprogramas_PDF_url(self):
        response = self.client.get(f'/reportes/subprograma_lista_pdf')
        self.assertEqual(response.status_code, 200)

    def test_vistaSubprogramas_PDF_nombre_url(self):
        response = self.client.get(reverse('subprograma_lista_pdf'))
        self.assertEqual(response.status_code, 200)

    def test_vistaSubprogramas_PDF_html_correcto(self):
        response = self.client.get(reverse('subprograma_lista_pdf'))
        self.assertTemplateUsed(response, 'reportes/ListaSubprogramaPDF.html')

    def test_vistaSubprograma_PDF_carga_datos(self):
        response = self.client.get(reverse('subprograma_lista_pdf'))
        self.assertIn('object_list', response.context)

    '''
    Vista Proyecto PDF
    '''

    def test_vistaProyectos_PDF_url(self):
        response = self.client.get(f'/reportes/proyecto_lista_pdf')
        self.assertEqual(response.status_code, 200)

    def test_vistaProyectos_PDF_nombre_url(self):
        response = self.client.get(reverse('proyecto_lista_pdf'))
        self.assertEqual(response.status_code, 200)

    def test_vistaProyectos_PDF_html_correcto(self):
        response = self.client.get(reverse('proyecto_lista_pdf'))
        self.assertTemplateUsed(response, 'reportes/ListaProyectoPDF.html')

    def test_vistaProyectos_PDF_carga_datos(self):
        response = self.client.get(reverse('proyecto_lista_pdf'))
        self.assertIn('object_list', response.context)
