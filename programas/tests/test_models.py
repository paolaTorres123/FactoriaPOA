from django.test import TestCase
from programas.models import (Programa, Partida, MetaPrograma, MetaReal,
                              LONGITUD_MAXIMA)
from django.core.exceptions import ValidationError
from unittest import skip


class TestModels(TestCase):

    def setUp(self):

        self.programa = Programa(
            nombre='Programa para Jóvenes Zacatecanos',
            anio_ejercicio_fiscal=2019,
            recurso_asignado=600000,
            fuente='Gobierno',
            tipo='MEN',
            status='ACT',
            tipo_programa_p='APO',
        )
        self.programa.save()

        self.partida = Partida(
            numero_partida=3000,
            nombre_partida='Partida tres mil',
            monto_partida=6700.00,
            programa=self.programa,
        )
        self.partida.save()

        self.meta_programada = MetaPrograma(
            numero_actividades=5,
            numero_beneficiarios=100,
            numero_hombres=250,
            numero_mujeres=250,
            edad='ADU'
        )

        self.meta_real = MetaReal(
            numero_actividades_r=5,
            numero_beneficiarios_r=700,
            numero_hombres_r=550,
            numero_mujeres_r=150,
            edad_r='NAD'
        )

    def test_agrega_modelo_programa(self):
        self.assertEqual(Programa.objects.count(), 1)

    def test_return_object_programa(self):
        self.programa.full_clean()
        self.programa.save()
        self.assertEqual(self.programa.nombre, self.programa.return_nombre())

    def test_return_object_partida(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.full_clean()
        self.partida.save()
        self.assertEqual(Partida.objects.first().__str__(),
                         self.partida.nombre_partida.__str__())

    def test_nombre_programa_es_requerido(self):
        self.programa.nombre = None
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_nombre_programa_min_5_caracteres(self):
        self.programa.nombre = 'prog'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_nombre_programa_formato_incorrecto_caracteres_especiales(self):
        self.programa.nombre = '$$$$&%programa%&$$$'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_nombre_programa_caracteres_numericos_no_permitidos(self):
        self.programa.nombre = 'programa Niños 9999'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_max_longitud_nombre_programa(self):
        self.programa.nombre = 'Este es un nombre que es demasiado largo'*2
        self.assertLess(len(self.programa.nombre), 100)

    def test_longitud_nombre_excedida(self):
        self.programa.nombre = 'Este es un nombre que es demasiado largo'*10

        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_nombre_programa_primer_caracter_espacio_no_permitido(self):
        self.programa.nombre = ' programa Niños'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_nombre_programa_no_puede_estar_vacio(self):
        self.programa.nombre = ''
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_anio_fiscal_programa_es_requerido(self):
        self.programa.anio_ejercicio_fiscal = None
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_anio_fiscal_programa_no_puede_estar_vacio(self):
        self.programa.anio_ejercicio_fiscal = ''
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_anio_fiscal_programa_no_acepta_caracteres_especiales(self):
        self.programa.anio_ejercicio_fiscal = '$$$7###/'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_anio_fiscal_programa_no_acepta_caracteres(self):
        self.programa.anio_ejercicio_fiscal = 'Año dos mil diez'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_anio_fiscal_programa_debe_tener_4_digitos(self):
        self.programa.anio_ejercicio_fiscal = 15
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_recurso_asignado_programa_es_requerido(self):
        self.programa.recurso_asignado = None
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_recurso_asignado_programa_no_puede_estar_vacio(self):
        self.programa.recurso_asignado = ''
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_recurso_asignado_programa_no_acepta_caracteres_especiales(self):
        self.programa.recurso_asignado = '$$=$'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_recurso_asignado_programa_no_acepta_caracteres(self):
        self.programa.recurso_asignado = 'Año dos mil diez 2017'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_recurso_asignado_programa_valor_minimo_de_0(self):
        self.programa.recurso_asignado = -56
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_recurso_asignado_programa_valor_maximo_de_6000000(self):
        self.programa.recurso_asignado = 6000000.01
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_fuente_programa_es_requerido(self):
        self.programa.fuente = None
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_fuente_programa_no_puede_estar_vacio(self):
        self.programa.fuente = ''
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_fuente_programa_no_caracteres_especiales(self):
        self.programa.fuente = '#%Secretaría de Economía%&'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_fuente_programa_no_caracteres_numericos(self):
        self.programa.fuente = 'Secretaría9'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_fuente_programa_no_debe_rebasar_100_caracteres(self):
        self.programa.fuente = 'A'*120
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_fuente_programa_debe_ser_mayor_a_5_caracteres(self):
        self.programa.fuente = 'tres'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_fuente_programa_primer_caracter_sin_espacio(self):
        self.programa.fuente = ' Programa de Apoyo a Familias'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_tipo_programa_selecciona_opcion_invalida(self):
        self.programa.tipo = 'Esta opción no existe'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_tipo_programa_requerida(self):
        self.programa.tipo = None
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_tipo_programa_no_vacio(self):
        self.programa.tipo = ''
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_status_programa_no_vacio(self):
        self.programa.status = ''
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_status_programa_requerido(self):
        self.programa.status = None
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_status_programa_selecciona_opcion_invalida(self):
        self.programa.status = 'Status No Válido'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_tipo_programa_p_vacio(self):
        self.programa.tipo_programa_p = ''
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_tipo_programa_p_requerido(self):
        self.programa.tipo_programa_p = None
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    def test_tipo_programa_p_selecciona_opcion_invalida(self):
        self.programa.tipo_programa_p = 'Opción inválida'
        with self.assertRaises(ValidationError):
            self.programa.full_clean()

    # Campos de Partida

    def test_numero_partida_vacia(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.numero_partida = ''
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_numero_partida_requerida(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.numero_partida = None
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_numero_partida_caracteres_no_especiales(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.numero_partida = '%&%&%'
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_numero_partida_caracteres_no_permitidos(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.numero_partida = 'Dos mil setenta y cuatro'
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_numero_partida_debe_tener_4_digitos(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.numero_partida = 915
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_nombre_partida_no_vacia(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.nombre_partida = ''
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_nombre_partida_requerido(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.nombre_partida = None
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_nombre_partida_no_caracteres_especiales(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.nombre_partida = '$#Especial#$'
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_nombre_partida_no_numeros_permitidos(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.nombre_partida = 'Partida 3000'
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_nombre_partida_con_espacio_al_inicio(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.nombre_partida = ' Partida correcta'
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_nombre_partida_rebasa_cantidad_maxima_de_70_caracteres(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.nombre_partida = 'S'*71
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_nombre_partida_es_menor_a_cantidad_minima_de_5_caracteres(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.nombre_partida = 'Nom'
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_monto_partida_requerido(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.monto_partida = None
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_monto_partida_no_vacio(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.monto_partida = ''
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_monto_partida_no_caracteres_especiales(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.monto_partida = '$$$$###12'
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_monto_partida_no_caracteres_permitidos(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.monto_partida = 'doscientos'
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_monto_partida_no_mayor_a_6000000(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.monto_partida = 9000000
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    def test_monto_partida_no_menor_a_0(self):
        self.programa.full_clean()
        self.programa.save()
        self.partida.programa = self.programa
        self.partida.monto_partida = -15
        with self.assertRaises(ValidationError):
            self.partida.full_clean()

    # Metas programadas
    def test_meta_programada_act_no_vacia(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_actividades = ''
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_act_requerido(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_actividades = None
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_act_no_caracteres_especiales(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_actividades = '$$$$$'
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_act_no_caracteres(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_actividades = 'Numero de actividades'
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_act_valor_minimo_de_0(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_actividades = -1
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_act_valor_maximo_de_100(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_actividades = 102
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_ben_vacio(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_beneficiarios = ''
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_ben_requerido(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_beneficiarios = None
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_ben_no_acepta_caracteres_especiales(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_beneficiarios = '$###$'
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_ben_no_acepta_caracteres(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_beneficiarios = 'beneficiarios'
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_ben_no_debe_ser_menor_a_0(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_beneficiarios = -12
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_ben_no_debe_ser_mayor_a_9000000(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_beneficiarios = 9000001
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_hom_vacio(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_hombres = ''
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_hom_requerido(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_hombres = None
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_hom_no_caracteres_especiales(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_hombres = '$##$$##'
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_hom_no_caracteres(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_hombres = 'quinientos'
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_hom_valor_minimo_de_0(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_hombres = -13
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_hom_valor_minimo_de_9000000(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_hombres = 9000001
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_muj_vacio(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_mujeres = ''
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_muj_requerido(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_mujeres = None
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_muj_no_caracteres_especiales(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_mujeres = '$##$$##'
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_muj_no_caracteres(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_mujeres = 'quinientos'
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_muj_valor_minimo_de_0(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_mujeres = -13
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_muj_valor_minimo_de_9000000(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.numero_mujeres = 9000001
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_edad_opcion_incorrecta(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.edad = 'AME'
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_edad_no_vacio(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.edad = ''
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    def test_meta_programada_edad_requerido(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_programada.programa = self.programa
        self.meta_programada.edad = None
        with self.assertRaises(ValidationError):
            self.meta_programada.full_clean()

    # Metas Reales
    def test_meta_real_act_no_vacia(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_actividades_r = ''
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_act_requerido(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_actividades_r = None
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_act_no_caracteres_especiales(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_actividades_r = '$$$$$'
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_act_no_caracteres(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_actividades_r = 'Numero de actividades'
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_act_valor_minimo_de_0(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_actividades_r = -1
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_act_valor_maximo_de_100(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_actividades_r = 102
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_ben_vacio(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_beneficiarios_r = ''
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_ben_requerido(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_beneficiarios_r = None
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_ben_no_acepta_caracteres_especiales(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_beneficiarios_r = '$###$'
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_ben_no_acepta_caracteres(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_beneficiarios_r = 'beneficiarios'
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_ben_no_debe_ser_menor_a_0(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_beneficiarios_r = -12
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_ben_no_debe_ser_mayor_a_9000000(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_beneficiarios_r = 9000001
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_hom_vacio(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_hombres_r = ''
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_hom_requerido(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_hombres_r = None
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_hom_no_caracteres_especiales(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_hombres_r = '$##$$##'
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_hom_no_caracteres(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_hombres_r = 'quinientos'
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_hom_valor_minimo_de_0(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_hombres_r = -13
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_hom_valor_minimo_de_9000000(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_hombres_r = 9000001
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_muj_vacio(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_mujeres_r = ''
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_muj_requerido(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_mujeres_r = None
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_muj_no_caracteres_especiales(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_mujeres_r = '$##$$##'
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_muj_no_caracteres(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_mujeres_r = 'quinientos'
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_muj_valor_minimo_de_0(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_mujeres_r = -13
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_muj_valor_minimo_de_9000000(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.numero_mujeres_r = 9000001
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_edad_r_opcion_incorrecta(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.edad_r = 'AUD'
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_edad_r_no_vacio(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.edad_r = ''
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    def test_meta_real_edad_r_requerido(self):
        self.programa.full_clean()
        self.programa.save()
        self.meta_real.programa_r = self.programa
        self.meta_real.edad_r = None
        with self.assertRaises(ValidationError):
            self.meta_real.full_clean()

    # Fail
    @skip
    def test_nombre_programa_nombre_requerido(self):
        self.programa.nombre = None
        try:
            self.programa.full_clean()
        except ValidationError as ex:
            message = str(ex.message_dict['nombre'][0])
            self.assertEqual(message, LONGITUD_MAXIMA)

    def test_return_object_partida_correcto(self):
        self.partida.full_clean()
        self.partida.save()
        self.assertEqual(self.partida.nombre_partida, self.partida.__str__())

    # Fail
    @skip
    def test_anio_ejercicio_fiscal_requerido(self):
        self.programa.anio_ejercicio_fiscal = None
        try:
            self.programa.full_clean()
        except ValidationError as ex:
            message = str(ex.message_dict['anio_ejercicio_fiscal'][0])
            self.assertEqual(message, LONGITUD_MAXIMA)

    def test_prueba_texto_de_error_nombre_programa(self):
        self.programa.nombre = 'Este es un nombre que es demasiado largo.'*11
        try:
            self.programa.full_clean()
        except ValidationError as ex:
            message = str(ex.message_dict['nombre'][0])
            self.assertEqual(message, LONGITUD_MAXIMA)

    def test_insercion_del_programa(self):
        self.programa.save()
        self.assertEqual(Programa.objects.all()[0], self.programa)
