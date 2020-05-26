from django.test import TestCase
from programas.models import (Programa, LONGITUD_MAXIMA,
                              LONGITUD_MINIMA, VALOR_MINIMO, VALOR_MAXIMO,
                              FORMATO_NUMERO_INCORRECTO)
from programas.forms import ProgramaForm, PartidaForm, MetaForm, MetaRealForm


class TestForms(TestCase):

    def setUp(self, nombre="Programa para Jóvenes Zacatecanos",
              anio_ejercicio_fiscal=2019,
              recurso_asignado=600000,
              fuente='Trimestral'):

        self.programa = Programa(
            nombre='Programa para Jóvenes Zacatecanos',
            anio_ejercicio_fiscal=2019,
            recurso_asignado=600000,
            fuente='Gobierno',
            tipo='MEN',
            status='ACT',
            tipo_programa_p='APO',
        )

        self.programa_data = {
            'nombre': nombre,
            'anio_ejercicio_fiscal': anio_ejercicio_fiscal,
            'recurso_asignado': recurso_asignado,
            'fuente': fuente,
            'tipo': 'MEN',
            'status': 'ACT',
            'tipo_programa_p': 'APO'
        }

        self.data = {
            'nombre': nombre,
            'anio_ejercicio_fiscal': anio_ejercicio_fiscal,
            'recurso_asignado': recurso_asignado,
            'fuente': fuente,
            'tipo': 'MEN',
            'status': 'ACT',
            'numero_actividades_mp': 6,
            'numero_beneficiarios_mp': 500,
            'numero_hombres_mp': 250,
            'numero_mujeres_mp': 250,
            'edad_mp': 'ADU',
            'numero_actividades_mr': 5,
            'numero_beneficiarios_mr': 5200,
            'numero_hombres_mr': 950,
            'numero_mujeres_mr': 111,
            'edad_mr': 'ADU',
            'tipo_programa_p': 'APO'
        }

        self.data_partida = {
            'numero_partida': 3000,
            'nombre_partida': 'Partida tres mil',
            'monto_partida': 6700.00,
            'programa': self.programa.id
        }

        self.data_meta = {
            'numero_actividades': 5,
            'numero_beneficiarios': 490,
            'numero_hombres': 245,
            'numero_mujeres': 245,
            'edad': 'JOV',
            'programa': self.programa.id
        }

        self.data_meta_real = {
            'numero_actividades_r': 10,
            'numero_beneficiarios_r': 1490,
            'numero_hombres_r': 2451,
            'numero_mujeres_r': 2452,
            'edad_r': 'JOV',
            'programa_r': self.programa.id
        }

    def test_si_el_formulario_de_programa_es_valido(self):
        form = ProgramaForm(
            self.data
        )
        self.assertTrue(form.is_valid())

    def test_si_el_formulario_de_partida_es_valido(self):
        form = PartidaForm(
            self.data_partida
        )
        self.assertTrue(form.is_valid())

    def test_si_el_formulario_de_metas_es_valido(self):
        form = MetaForm(
            self.data_meta
        )
        self.assertTrue(form.is_valid())

    def test_si_el_formulario_de_programa_es_invalido(self):
        self.data['nombre'] = 'funcione cada vez más'*15
        form = ProgramaForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_si_el_formulario_de_partidas_es_invalido(self):
        self.data_partida['numero_partida'] = 'Esto no es un número'
        form = PartidaForm(self.data_partida)
        self.assertFalse(form.is_valid())

    def test_max_longitud_nombre(self):
        self.data['nombre'] = 'Este es un nombre que es demasiado largo'*15
        form = ProgramaForm(
            self.data
        )
        self.assertEqual(form.errors['nombre'], [LONGITUD_MAXIMA])

    def test_nombre_programa_vacio(self):
        self.data['nombre'] = ''
        form = ProgramaForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_min_longitud_nombre(self):
        self.data['nombre'] = 'Este'
        form = ProgramaForm(
            self.data
        )
        self.assertEqual(form.errors['nombre'], [LONGITUD_MINIMA])

    def test_anio_ejercicio_fiscal_vacio(self):
        self.data['anio_ejercicio_fiscal'] = ''
        form = ProgramaForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_anio_ejercicio_fiscal_valor_numerico(self):
        self.data['anio_ejercicio_fiscal'] = 'letra'
        form = ProgramaForm(
            self.data
        )
        self.assertEqual(form.errors['anio_ejercicio_fiscal'], [
                         FORMATO_NUMERO_INCORRECTO])

    def test_recurso_asignado_vacio(self):
        self.data['recurso_asignado'] = None
        form = ProgramaForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_valor_minimo_recurso_asignado(self):
        self.data['recurso_asignado'] = -10
        form = ProgramaForm(
            self.data
        )
        self.assertEqual(form.errors['recurso_asignado'], [VALOR_MINIMO])

    def test_valor_maximo_recurso_asignado(self):
        self.data['recurso_asignado'] = 6000001
        form = ProgramaForm(
            self.data
        )
        self.assertEqual(form.errors['recurso_asignado'], [VALOR_MAXIMO])

    def test_formulario_tiene_label_de_nombre_de_programa(self):
        form = ProgramaForm()
        self.assertIn('<label for="id_nombre">', form.as_p())

    # Test para formulario de programa

    def test_programa_form_valido(self):
        form = ProgramaForm(self.programa_data)
        self.assertTrue(form.is_valid())

    def test_programa_nombre_vacio(self):
        self.programa_data['nombre'] = ''
        form = ProgramaForm(self.programa_data)
        self.assertFalse(form.is_valid())

    def test_programa_anio_ejercicio_no_de_4_digitos(self):
        self.programa_data['anio_ejercicio_fiscal'] = 16
        form = ProgramaForm(self.programa_data)
        self.assertFalse(form.is_valid())

    def test_programa_recurso_asignado_fuera_de_rango(self):
        self.programa_data['recurso_asignado'] = -6000005
        form = ProgramaForm(self.programa_data)
        self.assertFalse(form.is_valid())

    def test_programa_fuente_sobrepasa_caracteres(self):
        self.programa_data['fuente'] = 'fuente'*19
        form = ProgramaForm(self.programa_data)
        self.assertFalse(form.is_valid())

    def test_programa_tipo_invalido(self):
        self.programa_data['tipo'] = 'Este tipo es inválido'
        form = ProgramaForm(self.programa_data)
        self.assertFalse(form.is_valid())

    def test_programa_status_no_requerido(self):
        self.programa_data['status'] = ''
        form = ProgramaForm(self.programa_data)
        self.assertFalse(form.is_valid())

    def test_programa_tipo_programa_invalido(self):
        self.programa_data['tipo_programa_p'] = 'Yo no existo'
        form = ProgramaForm(self.programa_data)
        self.assertFalse(form.is_valid())

    # Test para formulario de partida
    def test_partida_form_es_valido(self):
        self.programa.save()
        form = PartidaForm(self.data_partida)
        self.assertTrue(form.is_valid())

    def test_partida_numero_partida_no_es_numero(self):
        self.programa.save()
        self.data_partida['numero_partida'] = 'No soy un número'
        form = PartidaForm(self.data_partida)
        self.assertFalse(form.is_valid())

    def test_partida_nombre_partida_es_invalido(self):
        self.programa.save()
        self.data_partida['nombre_partida'] = 'Partida de 3000'
        form = PartidaForm(self.data_partida)
        self.assertFalse(form.is_valid())

    def test_partida_monto_partida_esta_vacio(self):
        self.programa.save()
        self.data_partida['monto_partida'] = ''
        form = PartidaForm(self.data_partida)
        self.assertFalse(form.is_valid())

    # Test para formulario de metas programadas
    def test_meta_programada_form_es_valido(self):
        self.programa.save()
        form = MetaForm(self.data_meta)
        self.assertTrue(form.is_valid())

    def test_meta_programada_act_no_es_numero(self):
        self.programa.save()
        self.data_meta['numero_actividades'] = 'No soy un número'
        form = MetaForm(self.data_meta)
        self.assertFalse(form.is_valid())

    def test_meta_programada_ben_esta_vacio(self):
        self.programa.save()
        self.data_meta['numero_beneficiarios'] = ''
        form = MetaForm(self.data_meta)
        self.assertFalse(form.is_valid())

    def test_meta_programada_hom_no_alcanza_limite_minimo(self):
        self.programa.save()
        self.data_meta['numero_hombres'] = -12
        form = MetaForm(self.data_meta)
        self.assertFalse(form.is_valid())

    def test_meta_programada_muj_vacio(self):
        self.programa.save()
        self.data_meta['numero_mujeres'] = ''
        form = MetaForm(self.data_meta)
        self.assertFalse(form.is_valid())

    def test_meta_programada_rango_edad_no_valida(self):
        self.programa.save()
        self.data_meta['edad'] = 'No soy una opción válida'
        form = MetaForm(self.data_meta)
        self.assertFalse(form.is_valid())

    # Test para formulario de metas reales
    def test_meta_real_form_es_valido(self):
        self.programa.save()
        form = MetaRealForm(self.data_meta_real)
        self.assertTrue(form.is_valid())

    def test_meta_real_act_no_es_numero(self):
        self.programa.save()
        self.data_meta_real['numero_actividades_r'] = 'No soy un número'
        form = MetaRealForm(self.data_meta_real)
        self.assertFalse(form.is_valid())

    def test_meta_real_ben_esta_vacio(self):
        self.programa.save()
        self.data_meta_real['numero_beneficiarios_r'] = ''
        form = MetaRealForm(self.data_meta_real)
        self.assertFalse(form.is_valid())

    def test_meta_real_hom_no_alcanza_limite_minimo(self):
        self.programa.save()
        self.data_meta_real['numero_hombres_r'] = -12
        form = MetaRealForm(self.data_meta_real)
        self.assertFalse(form.is_valid())

    def test_meta_real_muj_vacio(self):
        self.programa.save()
        self.data_meta_real['numero_mujeres_r'] = ''
        form = MetaRealForm(self.data_meta_real)
        self.assertFalse(form.is_valid())

    def test_meta_real_rango_edad_no_valida(self):
        self.programa.save()
        self.data_meta_real['edad_r'] = 'No soy una opción válida'
        form = MetaRealForm(self.data_meta_real)
        self.assertFalse(form.is_valid())
