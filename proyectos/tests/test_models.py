from django.test import TestCase
from proyectos.models import Proyectos, Actividades, LONGUITUD_MAXIMA
from django.core.exceptions import ValidationError


class TestModels(TestCase):

    def setUp(self):
        self.actividad = Actividades(
            nombre_actividad='Juegos',
            unidad_medida='Eventos',
            cantidad=3,
            saldo=120000
        )
        self.actividad.save()

        self.proyecto = Proyectos(
            nombre_proyecto='Los emprendedores'
        )

    def test_agrega_proyecto(self):
        self.proyecto.save()
        self.assertEqual(Proyectos.objects.count(), 1)

    def test_agrega_actividad(self):
        self.prepara_actividad()
        self.actividad.save()
        self.assertEqual(Actividades.objects.count(), 1)

    def test_actividad_nombre_act_vacio(self):
        self.prepara_actividad()
        self.actividad.nombre_actividad = ''
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_unidad_medida_vacio(self):
        self.prepara_actividad()
        self.actividad.unidad_medida = ''
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_cantidad_vacio(self):
        self.prepara_actividad()
        self.actividad.cantidad = ''
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_saldo_vacio(self):
        self.prepara_actividad()
        self.actividad.saldo = ''
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_proyecto_nombre_pro_vacio(self):
        self.proyecto.save()
        self.proyecto.nombre_proyecto = ''
        with self.assertRaises(ValidationError):
            self.proyecto.full_clean()

    def test_actividad_nombre_act_vacio_mensaje(self):
        self.prepara_actividad()
        self.actividad.nombre_actividad = ''
        try:
            self.actividad.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['nombre_actividad'][0])
            self.assertEqual(msg, 'This field cannot be blank.')

    def test_actividad_unidad_medida_vacio_mensaje(self):
        self.prepara_actividad()
        self.actividad.unidad_medida = ''
        try:
            self.actividad.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['unidad_medida'][0])
            self.assertEqual(msg, 'This field cannot be blank.')

    def test_proyecto_nombre_pro_vacio_mensaje(self):
        self.proyecto.save()
        self.proyecto.nombre_proyecto = ''
        try:
            self.proyecto.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['nombre_proyecto'][0])
            self.assertEqual(msg, 'This field cannot be blank.')

    def test_actividad_nombre_act_incorrecto_format(self):
        self.prepara_actividad()
        self.actividad.nombre_actividad = '@$$#!122WE'
        try:
            self.actividad.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['nombre_actividad'][0])
            self.assertEqual(msg, 'No se permiten caracteres especiales')

    def test_proyecto_nombre_pro_incorrecto_format(self):
        self.proyecto.save()
        self.proyecto.nombre_proyecto = '@$$#!122WE'
        try:
            self.proyecto.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['nombre_proyecto'][0])
            self.assertEqual(msg, 'No se permiten caracteres especiales')

    def test_proyecto_unidad_medid_incorrecto_format(self):
        self.proyecto.save()
        self.proyecto.unidad_medida = 'POITPORITPETTR'
        try:
            self.proyecto.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['unidad_medida'][0])
            self.assertEqual(msg, 'No se permiten caracteres especiales')

    def test_proyecto_cantidad_incorrecto_format(self):
        self.proyecto.save()
        self.proyecto.cantidad = '4984984#$#^%4'
        try:
            self.proyecto.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['cantidad'][0])
            self.assertEqual(msg, 'No se permiten caracteres especiales')

    def test_proyecto_saldo_incorrecto_format(self):
        self.proyecto.save()
        self.proyecto.saldo = '49849879848@#$%^&*4#$#^%4'
        try:
            self.proyecto.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['saldo'][0])
            self.assertEqual(msg, 'No se permiten caracteres especiales')

    def test_actividad_nombre_act_mayor_60_caracteres(self):
        self.prepara_actividad()
        self.actividad.nombre_actividad = 'emmmrn'*20
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_unidad_medida_mayor_4_caracteres(self):
        self.prepara_actividad()
        self.actividad.unidad_medida = 'TUDND'
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_cantidad_mayor_3_caracteres(self):
        self.prepara_actividad()
        self.actividad.cantidad = 1234
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_saldo_mayor_9_caracteres(self):
        self.prepara_actividad()
        self.actividad.saldo = 12345678910
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_proyecto_nombre_pro_mayor_60_caracteres(self):
        self.proyecto.save()
        self.proyecto.nombre_proyecto = 'emmmrn'*20
        with self.assertRaises(ValidationError):
            self.proyecto.full_clean()

    def test_actividad_nombre_act_60_caracteres_msj(self):
        self.prepara_actividad()
        self.actividad.nombre_actividad = 'ffhuf6'*11
        try:
            self.actividad.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['nombre_actividad'][0])
            self.assertEqual(msg, 'Error en la longitud')

    def test_actividad_cantidad_mayor_3_caracteres_msj(self):
        self.prepara_actividad()
        self.actividad.cantidad = 1234
        try:
            self.actividad.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['cantidad'][0])
            self.assertEqual(msg, 'El valor máximo permitido es 100')

    def test_actividad_saldo_mayor_9_caracteres_msj(self):
        self.prepara_actividad()
        self.actividad.saldo = 12345678910
        try:
            self.actividad.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['saldo'][0])
            self.assertEqual(msg, 'El valor máximo permitido son 100000000')

    def test_actividad_sin_proyecto(self):
        self.prepara_actividad()
        self.actividad.proyecto = None
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_sin_proyecto_msg(self):
        self.prepara_actividad()
        self.actividad.proyecto = None
        try:
            self.actividad.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['proyecto'][0])
            self.assertEqual(msg, 'This field cannot be blank.')

    def test_actividad_unidad_medida_formato_incorrecto(self):
        self.prepara_actividad()
        self.actividad.unidad_medida = 'LPOPEIRIRIEOIRO'
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_cantidad_formato_incorrecto(self):
        self.prepara_actividad()
        self.actividad.cantidad = 123456
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_cantidad_valor_minimo(self):
        self.prepara_actividad()
        self.actividad.cantidad = -1
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_cantidad_valor_minimo_msg(self):
        self.prepara_actividad()
        self.actividad.cantidad = -1
        try:
            self.actividad.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['cantidad'][0])
            self.assertEqual(msg, 'El valor mínimo permitido es 1')

    def test_actividad_cantidad_valor_maximo(self):
        self.prepara_actividad()
        self.actividad.cantidad = 1222222222222222112121
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_cantidad_valor_maximo_msg(self):
        self.prepara_actividad()
        self.actividad.cantidad = 1222222222222222112121
        try:
            self.actividad.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['cantidad'][0])
            self.assertEqual(msg, 'El valor máximo permitido es 100')

    def test_actividad_saldo_formato_incorrecto(self):
        self.prepara_actividad()
        self.actividad.saldo = 1254545487878
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_saldo_valor_minimo(self):
        self.prepara_actividad()
        self.actividad.saldo = -1
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_saldo_valor_minimo_msg(self):
        self.prepara_actividad()
        self.actividad.saldo = -1
        try:
            self.actividad.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['saldo'][0])
            self.assertEqual(msg, 'El valor mínimo permitido es 1')

    def test_actividad_saldo_valor_maximo(self):
        self.prepara_actividad()
        self.actividad.saldo = 1222222222222222112.000
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def test_actividad_saldo_valor_maximo_msg(self):
        self.prepara_actividad()
        self.actividad.saldo = 1222222222222222112121.000
        try:
            self.actividad.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['saldo'][0])
            self.assertEqual(msg, 'El valor máximo permitido son 100000000')

    def test_return_object_proyecto(self):
        self.actividad = Actividades(
            nombre_actividad='Juegos',
            unidad_medida='Eventos',
            cantidad=3,
            saldo=120000
        )
        self.actividad.save()

        self.proyecto = Proyectos(
            nombre_proyecto='Los emprendedores'
        )
        self.proyecto.save()
        self.assertEqual(self.proyecto.nombre_proyecto,
                         self.proyecto.__str__())

    def test_min_longitud_nombre_proyecto(self):
        self.actividad = Actividades(
            nombre_actividad='Juegos',
            unidad_medida='Eventos',
            cantidad=3,
            saldo=120000
        )
        self.actividad.save()

        self.proyecto = Proyectos(
            nombre_proyecto='Los emprendedores'
        )
        self.proyecto.nombre_proyecto = 'Emprendimiento'
        self.assertLess(len(self.proyecto.nombre_proyecto), 60)

    def test_longitud_nombre_excedida(self):
        self.proyecto.nombre_proyecto = 'Este'*30

        with self.assertRaises(ValidationError):
            self.proyecto.full_clean()

    def test_prueba_error(self):
        self.proyecto.nombre_proyecto = 'ncjkn'*20
        try:
            self.proyecto.full_clean()
        except ValidationError as ex:
            massage = str(ex.message_dict['nombre_proyecto'][0])
            self.assertEqual(massage, LONGUITUD_MAXIMA)

    def prepara_actividad(self):
        self.proyecto.save()
        self.actividad.proyecto = self.proyecto
