from django.test import TestCase
from usuarios.models import Administrativo
from django.contrib.auth.models import User
from programas.models import Partida, Programa
from django.urls import reverse
from . import test_models
from django.contrib.auth.models import User, Permission
from django.contrib.auth.models import Group


class SubprogramaViewTests(TestCase):
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
            primer_apellido='LOL',
            segundo_apellido='JJ',
            telefono='4949412345',
            foto='foto.png',
            usuario=self.usuario
        )
        self.administrativo.save()
        self.subp = test_models.SubprogramaModelTests.creaDefaultSubprograma(
            self)
        self.asigna_permisos_login()

    '''
    Vista Agregar subprograma
    '''

    def test_vistaAgregar_url(self):
        response = self.client.get('/subprograma/nuevo')
        self.assertEqual(response.status_code, 200)

    def test_vistaAgregar_nombre_url(self):
        response = self.client.get(reverse('nuevo_subprograma'))
        self.assertEqual(response.status_code, 200)

    def test_vistaAregar_html_correcto(self):
        response = self.client.get('/subprograma/nuevo')
        self.assertTemplateUsed(response,
                                'subprogramas/subprograma_form.html'
                                )

    def test_vistaAregar_envio_datos_a_lista_subprograma(self):
        response = self.client.get('/subprograma/')
        self.assertEqual(
            response.context['object_list'][0].nombre,
            'Subprograma De Referencia'
        )

    '''
    Vista Editar subprograma
    '''

    def test_vistaEditar_url(self):
        response = self.client.get(f'/subprograma/editar/{self.subp.id}')
        self.assertEqual(response.status_code, 200)

    def test_vistaEditar_nombre_url(self):
        response = self.client.get(
            reverse('editar_subprograma', args=[self.subp.id]))
        self.assertEqual(response.status_code, 200)

    def test_vistaEditar_html_correcto(self):
        response = self.client.get(f'/subprograma/editar/{self.subp.id}')
        self.assertTemplateUsed(response, 'subprogramas/subprograma_form.html')

    '''
    Vista Detalles/Ver subprograma
    '''

    def test_vistaVer_url(self):
        response = self.client.get(f'/subprograma/ver/{self.subp.id}')
        self.assertEqual(response.status_code, 200)

    def test_vistaVer_nombre_url(self):
        response = self.client.get(
            reverse('ver_subprograma', args=[self.subp.id]))
        self.assertEqual(response.status_code, 200)

    def test_vistaVer_html_correcto(self):
        response = self.client.get(f'/subprograma/ver/{self.subp.id}')
        self.assertTemplateUsed(
            response, 'subprogramas/subprograma_detail.html')

    '''
    Vista lista subprograma
    '''

    def test_vistaLista_url(self):
        response = self.client.get('/subprograma/')
        self.assertEqual(response.status_code, 200)

    def test_vistaLista_nombre_url(self):
        response = self.client.get(reverse('lista_subprograma'))
        self.assertEqual(response.status_code, 200)

    def test_vistaLista_html_correcto(self):
        response = self.client.get('/subprograma/')
        self.assertTemplateUsed(response, 'subprogramas/subprograma_list.html')

    def test_vistaLista_carga_datos(self):
        response = self.client.get('/subprograma/')
        self.assertIn('object_list', response.context)

    def test_vistaLista_envio_datos_a_Ver_subprograma(self):
        response = self.client.get(f'/subprograma/ver/{self.subp.id}')
        self.assertEqual(
            response.context['object'].nombre, 'Subprograma De Referencia')

    def test_vistaLista_envio_datos_a_Editar_subprograma(self):
        response = self.client.get(f'/subprograma/editar/{self.subp.id}')
        self.assertEqual(
            response.context['object'].nombre, 'Subprograma De Referencia')


    def asigna_permisos_login(self):
        user = User.objects.create_user(
            username='dirOperativo',
            password='F@@ctoria12',
            email='dir_operativo@factoria.gob.mx',
            is_staff=True
        )
        new_group, created = Group.objects.get_or_create(
            name='director_operativo')
        new_subprograma, created = Group.objects.get_or_create(
            name='encargado_subprograma')
        new_group.permissions.add(
            Permission.objects.get(codename='add_subprograma'))
        new_group.permissions.add(
            Permission.objects.get(codename='view_subprograma'))
        new_group.permissions.add(
            Permission.objects.get(codename='change_subprograma'))
        user.groups.add(new_group)
        self.client.login(username='dirOperativo', password='F@@ctoria12')