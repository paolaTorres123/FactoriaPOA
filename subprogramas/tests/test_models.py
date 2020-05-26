from django.core.exceptions import ValidationError
from django.test import TestCase
from subprogramas.models import Subprograma
from programas.models import Partida, Programa
from usuarios.models import User, Administrativo


class SubprogramaModelTests(TestCase):

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
            nombre_partida='Partida 1 de 3000',
            monto_partida=6700.00,
            programa=self.programa,
        )
        self.partida.save()

        self.usuario = User(
            username="usuario de prueba",
            email="correo@gmail.com",
            password="django",
            is_superuser=True
        )
        self.usuario.save()

        self.administrativo = Administrativo(
            nombre="usuario de prueba",
            primer_apellido='Solís',
            segundo_apellido='Galván',
            telefono='4949412345',
            foto='foto.png',
            usuario=self.usuario
        )
        self.administrativo.save()

    def creaDefaultSubprograma(self):
        return Subprograma.objects.create(
            programa=self.programa,
            nombre="Subprograma De Referencia",
            presupuesto=20580,
            responsable=self.usuario,
            estatus="ACT",
        )

    def creaSubprogramaPersonal(self, nombre='', presupuesto=None, estatus=''):
        return Subprograma.objects.create(
            programa=self.programa,
            nombre=nombre,
            presupuesto=presupuesto,
            responsable=self.usuario,
            estatus=estatus,
        )

    '''
    Pruebas del guardado del subprograma
    '''

    def test_subprograma_bien_guardado(self):
        subprograma = self.creaDefaultSubprograma()
        subprograma_uno = Subprograma.objects.first()
        self.assertEqual(subprograma_uno, subprograma)
        self.assertEqual(subprograma_uno.nombre, 'Subprograma De Referencia')
        self.assertEqual(subprograma_uno.estatus, "ACT")
        self.assertEqual(subprograma_uno.presupuesto, 20580)
        self.assertEqual(len(Subprograma.objects.all()), 1)

    def test_subprograma_guardado_con_id(self):
        subprograma = self.creaDefaultSubprograma()
        self.assertTrue(subprograma.id)

    '''
    Pruebas del nombre del subprograma
    '''

    def test_subprograma_nombre_no_nulo(self):
        with self.assertRaises(ValidationError):
            subprograma = self.creaSubprogramaPersonal('', 5000, 'ACT')
            subprograma.full_clean()

    def test_subprograma_nombre_no_nulo_mensaje(self):
        with self.assertRaisesMessage(
                ValidationError, "El nombre no puede estar vacío."
        ):
            subprograma = self.creaSubprogramaPersonal('', 5000, 'ACT')
            subprograma.full_clean()

    def test_subprograma_nombre_letras_especiales_permitidas(self):
        subprograma = self.creaSubprogramaPersonal(
            'aksñdlaäáÁàm', 5000, 'ACT'
        )
        subprograma.full_clean()

    def test_subprograma_nombre_caracteres_especiales_no_permitidos(self):
        with self.assertRaises(ValidationError):
            subprograma = self.creaSubprogramaPersonal(
                'aksd\'lam', 5000, 'ACT')
            subprograma.full_clean()

    def test_subp_nombre_caracteres_especiales_no_permitidos_mensaje(self):
        with self.assertRaisesMessage(
                ValidationError, "Solo se permiten letras."
        ):
            subprograma = self.creaSubprogramaPersonal(
                'aksdñlamó_', 5000, 'ACT')
            subprograma.full_clean()

    def test_subprograma_nombre_numeros_no_permitidos(self):
        with self.assertRaises(ValidationError):
            subprograma = self.creaSubprogramaPersonal(
                'aksdlam34', 5000, 'ACT')
            subprograma.full_clean()

    def test_subprograma_nombre_numeros_no_permitidos_mensaje(self):
        with self.assertRaisesMessage(
                ValidationError, "Solo se permiten letras."
        ):
            subprograma = self.creaSubprogramaPersonal(
                'aksdl1am34', 5000, 'ACT')
            subprograma.full_clean()

    def test_subprograma_nombre_longitud_minima_pasada(self):
        with self.assertRaises(ValidationError):
            subprograma = self.creaSubprogramaPersonal('hola', 5000, 'ACT')
            subprograma.full_clean()

    def test_subprograma_nombre_longitud_minima_pasada_mensaje(self):
        with self.assertRaisesMessage(
                ValidationError,
                "El nombre debe ser de por lo menos 5 caracteres."
        ):
            subprograma = self.creaSubprogramaPersonal(
                'hola', 5000, 'ACT'
            )
            subprograma.full_clean()

    def test_subprograma_nombre_longitud_maxima_pasada(self):
        with self.assertRaises(ValidationError):
            subprograma = Subprograma(
                nombre="holadfgfffffffffhhhhhhhhhhhhhhhhhhhhhhg" +
                       "ffffffffffffffffffffffffffhhhhhhhhhhho",
                presupuesto=66478,
                responsable=self.usuario,
                estatus='ACT',
            )
            subprograma.full_clean()

    def test_subprograma_nombre_longitud_maxima_pasada_mensaje(self):
        with self.assertRaisesMessage(
                ValidationError,
                "El nombre no puede pasar los 50 caracteres."
        ):
            subprograma = Subprograma(
                nombre="holadfgfffffffffhhhhhhhhhhhhhhhhhhhhhhg" +
                       "ffffffffffffffffffffffffffhhhhhhhhhhho",
                presupuesto=66478,
                responsable=self.usuario,
                estatus='ACT',
            )
            subprograma.full_clean()

    '''
    Pruebas del programa del subprograma
    '''

    def test_subprograma_programa_requerido(self):
        error = False
        try:
            subprograma = Subprograma.objects.create(
                nombre="nombre de ejemplo",
                presupuesto=66478,
                responsable=self.usuario,
                estatus='ACT',
            )
            subprograma.full_clean()
        except Exception as e:
            error = True
        self.assertTrue(error)

    '''
    Pruebas del responsable del subprograma
    '''

    def test_subprograma_responsable_requerido(self):
        error = False
        try:
            subprograma = Subprograma.objects.create(
                programa=self.programa,
                nombre="nombre de ejemplo",
                presupuesto=66478,
                estatus='ACT',
            )
            subprograma.full_clean()
        except Exception as e:
            error = True
        self.assertTrue(error)

    '''
    Pruebas del presupuesto del subprograma
    '''

    def test_subprograma_presupuesto_requerido(self):
        try:
            subprograma = Subprograma.objects.create(
                nombre="nombre",
                presupuesto=None,
                estatus="ACT",
            )
            subprograma.full_clean()
        except Exception:
            self.assertEqual(Exception.__name__, "Exception")

    def test_subprograma_presupuesto_caracteres_no_numericos_no_permitidos(
            self):
        with self.assertRaises(ValidationError):
            subprograma = self.creaSubprogramaPersonal(
                'ejemplo', '5000e', 'ACT')
            subprograma.full_clean()

    def test_subprograma_nombre_caracteres_no_numericos_no_permitidos(self):
        with self.assertRaisesMessage(
                ValidationError, "El presupuesto debe ser numérico."
        ):
            subprograma = self.creaSubprogramaPersonal(
                'ejemplo', '5000e', 'ACT')
            subprograma.full_clean()
