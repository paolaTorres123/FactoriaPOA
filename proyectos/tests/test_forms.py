from django.test import TestCase
from proyectos.models import (Actividades, LONGITUD_MINIMA,
                              VALOR_MINIMO, FORMATO_CARACTER_INCORRECTO)
from proyectos.forms import ProyectoForm, ActividadesForm


class TestForms(TestCase):

    def setUp(self, nombre_proyecto="Emprendimiento"):
        actividad = Actividades(
            nombre_actividad='Juegos',
            unidad_medida='Congresos',
            cantidad=12,
            saldo=120000.36
        )
        actividad.save()

        self.data = {
            'nombre_proyecto': nombre_proyecto
        }

    def test_form_proyecto_valido(self):
        form = ProyectoForm(
            self.data
        )
        self.assertTrue(form.is_valid())

    def test_usuario_form_nombre_vacio(self):
        self.data['nombre_proyecto'] = ''
        form = ProyectoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_longitud_excedida__nombre_proyecto_false(self):
        self.data['nombre_proyecto'] = 'Emprendimiento'*10
        self.form = ProyectoForm(
            self.data
        )
        self.assertFalse(self.form.is_valid())

    def test_min_longitud_nombre_proyecto(self):
        self.data['nombre_proyecto'] = 'Empr'
        form = ProyectoForm(
            self.data
        )
        self.assertIn(LONGITUD_MINIMA, form.errors['nombre_proyecto'])

    def test_no_numerico_proyecto(self):
        self.data['nombre_proyecto'] = 4516155556
        form = ProyectoForm(
            self.data
        )
        self.assertIn(FORMATO_CARACTER_INCORRECTO,
                      form.errors['nombre_proyecto'])

    def test_no_caracteres_especiales_proyecto(self):
        self.data['nombre_proyecto'] = '!#$#%^&*()*&^'
        form = ProyectoForm(
            self.data
        )
        self.assertIn(FORMATO_CARACTER_INCORRECTO,
                      form.errors['nombre_proyecto'])

    def test_nombre_proyecto_asignado_vacio(self):
        self.data['nombre_proyecto'] = None
        form = ProyectoForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_cantidad_actividad_vacio(self):
        self.data['cantidad'] = ''
        form = ActividadesForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_nombre_actividad_vacio(self):
        self.data['nombre_activdad'] = ''
        form = ActividadesForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_unidad_medida_actividad_vacio(self):
        self.data['unidd_medida'] = ''
        form = ActividadesForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_saldo_actividad_vacio(self):
        self.data['saldo'] = ''
        form = ActividadesForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_min_longitud_nombre_actividad(self):
        self.data['nombre_actividad'] = 'Empr'
        form = ActividadesForm(
            self.data
        )
        self.assertIn(LONGITUD_MINIMA, form.errors['nombre_actividad'])

    def test_longitud_excedida_nombre_actividad_false(self):
        self.data['nombre_proyecto'] = 'Juegos'*30
        self.form = ProyectoForm(
            self.data
        )
        self.assertFalse(self.form.is_valid())

    def test_no_numerico_actividad(self):
        self.data['nombre_actividad'] = 4516155556
        form = ActividadesForm(
            self.data
        )
        self.assertIn(FORMATO_CARACTER_INCORRECTO,
                      form.errors['nombre_actividad'])

    def test_no_caracteres_especiales_actividad(self):
        self.data['nombre_actividad'] = '!#$#%^&*()*&^'
        form = ActividadesForm(
            self.data
        )
        self.assertIn(FORMATO_CARACTER_INCORRECTO,
                      form.errors['nombre_actividad'])

    def test_unidad_medida_actividad_no_vacia(self):
        self.data['unidad_medida'] = None
        form = ActividadesForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_actividad_sin_unidad_medida_asignado_msj_error(self):
        self.data['unidad_medida'] = None
        form = ActividadesForm(
            self.data
        )
        self.assertEqual(form.errors['unidad_medida'], ['Requerido'])

    def test_cantidad_actividad_no_vacia(self):
        self.data['cantidad'] = None
        form = ActividadesForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_actividad_sin_cantidad_asignado_msj_error(self):
        self.data['cantidad'] = None
        form = ActividadesForm(
            self.data
        )
        self.assertEqual(form.errors['cantidad'], ['Requerido'])

    def test_cantidad_excede_valor_maximo(self):
        self.data['cantidad'] = 45252
        form = ActividadesForm(self.data)
        self.assertFalse(form.is_valid())

    def test_cantidad_error_valor_minimo(self):
        self.data['cantidad'] = 0
        form = ActividadesForm(self.data)
        self.assertFalse(form.is_valid())

    def test_no_caracteres_especiales_actividad_cantidad(self):
        self.data['cantidad'] = '!#$#%^&*()*&^'
        form = ActividadesForm(
            self.data
        )
        self.assertIn(VALOR_MINIMO, form.errors['cantidad'])

    def test_no_letras_actividad_cantidad(self):
        self.data['cantidad'] = 'Emprendimiento'
        form = ActividadesForm(
            self.data
        )
        self.assertIn(VALOR_MINIMO, form.errors['cantidad'])

    def test_saldo_actividad_no_vacia(self):
        self.data['saldo'] = None
        form = ActividadesForm(
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_actividad_sin_saldo_asignado_msj_error(self):
        self.data['saldo'] = None
        form = ActividadesForm(
            self.data
        )
        self.assertEqual(form.errors['saldo'], ['Requerido'])

    def test_saldo_excede_valor_maximo(self):
        self.data['saldo'] = 45252451236445
        form = ActividadesForm(self.data)
        self.assertFalse(form.is_valid())

    def test_saldo_con_decimales(self):
        self.data['saldo'] = 12348.20
        form = ActividadesForm(self.data)
        self.assertFalse(form.is_valid())

    def test_saldo_error_valor_minimo(self):
        self.data['saldo'] = -1
        form = ActividadesForm(self.data)
        self.assertFalse(form.is_valid())

    def test_no_caracteres_especiales_actividad_saldo(self):
        self.data['saldo'] = '!#$#%^&*()*&^'
        form = ActividadesForm(
            self.data
        )
        self.assertIn(VALOR_MINIMO, form.errors['saldo'])

    def test_no_letras_actividad_saldo(self):
        self.data['saldo'] = 'Emprendimiento'
        form = ActividadesForm(
            self.data
        )
        self.assertIn(VALOR_MINIMO, form.errors['saldo'])
