from django.test import TestCase
from subprogramas.forms import SubprogramaForm, EdicionSubprogramaForm
from programas.models import Partida, Programa
from usuarios.models import User, Administrativo


class SubprogramaFormTests(TestCase):

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

    # El estatus se agrega por defecto
    def test_SubprogramaForm_crear_sin_estatus(self):
        form = SubprogramaForm(
            data={
                'programa': self.programa.id,
                'nombre': 'ejemplo',
                'presupuesto': 5000,
                'responsable': self.usuario.id,
                'estatus': 'ACT',
            }
        )
        self.assertTrue(form.is_valid())

    # El estatus se debe indicar de forma obligatoria
    def test_EdicionSubprogramaForm_modificar_sin_estatus(self):
        form = EdicionSubprogramaForm(
            data={
                'programa': self.programa.id,
                'nombre': 'ejemplo',
                'presupuesto': 5000,
                'responsable': self.usuario.id,
            }
        )
        self.assertFalse(form.is_valid())
