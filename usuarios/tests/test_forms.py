from django.test import TestCase
from usuarios.forms import (UserForm, AdministrativoForm,
                            LoginForm, PASSWORD_INCORRECTO)
from django.contrib.auth.models import User


class TestFormUsuario(TestCase):

    def setUp(self, nombre='jorgesolis', correo='jasg15_@hotmail.com',
              password='Jorge123@', password_re='Jorge123@'):
        self.usuario = User(
            username=nombre,
            email=correo,
            password=password,
            is_superuser=True
        )

        self.data = {
            'username': nombre,
            'email': correo,
            'password': password,
            'password_re': password_re,
            'is_superuser': True
        }

        self.data_admin = {
            'nombre': 'Jorge',
            'primer_apellido': 'Solís',
            'segundo_apellido': 'Galván',
            'telefono': '4949412345',
            'foto': 'C:\\Users\\Lenovo\\Pictures\\3.png',
            'usuario': self.usuario.id
        }

    # Tests para cuenta de usuario

    def test_usuario_form_valido(self):
        form = UserForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_nombre_vacio(self):
        self.data['username'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_nombre_invalido_mensaje(self):
        self.data['username'] = 'jorge'
        form = UserForm(self.data)
        self.assertEqual(
            form.errors['username'],
            ['El nombre de usuario no sigue el formato'
             + ' solicitado, favor de verificarlo.'])

    def test_usuario_form_nombre_vacio_mensaje(self):
        self.data['username'] = ''
        form = UserForm(self.data)
        self.assertEqual(
            form.errors['username'],
            ['El nombre de usuario es requerido, favor de completarlo.'])

    def test_usuario_form_email_invalido(self):
        self.data['email'] = 'jasg15_@hotmail'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_email_vacio_mensaje(self):
        self.data['email'] = ''
        form = UserForm(self.data)
        self.assertEqual(form.errors['email'], [
                         'El correo es requerido, favor de completarlo.'])

    def test_usuario_form_email_invalido_mensaje(self):
        self.data['email'] = 'jasg15_@hotmail'
        form = UserForm(self.data)
        self.assertEqual(form.errors['email'], [
                         'Favor de ingresar un formato de correo válido.'])

    def test_usuario_form_password_invalido(self):
        self.data['password'] = 'Jorge123'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_invalido_mensaje(self):
        self.data['password'] = 'jorge'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], [PASSWORD_INCORRECTO])

    def test_usuario_form_password_re_requerido(self):
        self.data['password_re'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_con_espacios(self):
        self.data['password_re'] = 'Jorge123@ '
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_formato_invalido(self):
        self.data['password_re'] = 'jorgeasg'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_diferente_a_password(self):
        self.data['password'] = 'Inventors123@'
        self.data['password_re'] = 'Inventors124@'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_mas_caracteres(self):
        self.data['password_re'] = 'jorgeasg'*7
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_max_caracteres_mensaje(self):
        self.data['password_re'] = 'jorgeasg'*7
        form = UserForm(self.data)
        self.assertEqual(form.errors['password_re'], [PASSWORD_INCORRECTO])

    def test_usuario_form_password_re_min_caracteres(self):
        self.data['password_re'] = 'jor'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_administrativo_form_valido(self):
        self.usuario.save()
        self.data_admin['usuario'] = self.usuario.id
        form = AdministrativoForm(self.data_admin)
        self.assertTrue(form.is_valid())

    def test_administrativo_form_telefono_invalido(self):
        self.usuario.save()
        self.data_admin['usuario'] = self.usuario.id
        self.data_admin['telefono'] = '494941234'
        form = AdministrativoForm(self.data_admin)
        self.assertFalse(form.is_valid())

    def test_administrativo_form_telefono_invalido_mensaje(self):
        self.usuario.save()
        self.data_admin['usuario'] = self.usuario.id
        self.data_admin['telefono'] = '494941234'
        form = AdministrativoForm(self.data_admin)
        self.assertEqual(form.errors['telefono'], [
                         'El número telefónico debe contener 10 dígitos.'])

    def test_administrativo_form_nombre_invalido(self):
        self.usuario.save()
        self.data_admin['usuario'] = self.usuario.id
        self.data_admin['nombre'] = 'Jorge1'
        form = AdministrativoForm(self.data_admin)
        self.assertFalse(form.is_valid())

    def test_administrativo_form_nombre_requerido_mensaje(self):
        self.usuario.save()
        self.data_admin['usuario'] = self.usuario.id
        self.data_admin['nombre'] = ''
        form = AdministrativoForm(self.data_admin)
        self.assertEqual(form.errors['nombre'], [
                         'El nombre es requerido, favor de completarlo.'])

    def test_administrativo_form_nombre_min_caracteres_mensaje(self):
        self.usuario.save()
        self.data_admin['usuario'] = self.usuario.id
        self.data_admin['nombre'] = 'Jo'
        form = AdministrativoForm(self.data_admin)
        self.assertEqual(form.errors['nombre'], [
                         'La longitud mínima del nombre es de 3 caracteres.'])

    def test_administrativo_form_nombre_max_caracteres_mensaje(self):
        self.usuario.save()
        self.data_admin['usuario'] = self.usuario.id
        self.data_admin['nombre'] = 'Jorges'*10
        form = AdministrativoForm(self.data_admin)
        self.assertEqual(form.errors['nombre'], [
                         'La longitud máxima del nombre es de 50 caracteres.'])

    def test_administrativo_form_primer_apellido_invalido(self):
        self.usuario.save()
        self.data_admin['usuario'] = self.usuario.id
        self.data_admin['primer_apellido'] = 'Solís +'
        form = AdministrativoForm(self.data_admin)
        self.assertFalse(form.is_valid())

    def test_administrativo_form_primer_apellido_requerido_mensaje(self):
        self.usuario.save()
        self.data_admin['usuario'] = self.usuario.id
        self.data_admin['primer_apellido'] = ''
        form = AdministrativoForm(self.data_admin)
        self.assertEqual(
            form.errors['primer_apellido'],
            ['El primer apellido es requerido, favor de completarlo.'])

    def test_administrativo_form_primer_apellido_max_caracteres_mensaje(self):
        self.usuario.save()
        self.data_admin['usuario'] = self.usuario.id
        self.data_admin['primer_apellido'] = 'solisg'*10
        form = AdministrativoForm(self.data_admin)
        self.assertEqual(
            form.errors['primer_apellido'],
            ['La longitud máxima del primer apellido es de 50 caracteres.'])

    def test_administrativo_form_segundo_apellido_invalido(self):
        self.usuario.save()
        self.data_admin['usuario'] = self.usuario.id
        self.data_admin['segundo_apellido'] = ' Galván1'
        form = AdministrativoForm(self.data_admin)
        self.assertFalse(form.is_valid())

    def test_administrativo_form_segundo_apellido_max_caracteres_mensaje(self):
        self.usuario.save()
        self.data_admin['usuario'] = self.usuario.id
        self.data_admin['segundo_apellido'] = 'solisg'*10
        form = AdministrativoForm(self.data_admin)
        self.assertEqual(
            form.errors['segundo_apellido'],
            ['La longitud máxima del segundo apellido es de 50 caracteres.'])

    # Test Login

    def test_form_login_valido(self):
        self.crear_usuario()
        form = LoginForm(
            None, data={'username': 'jorgesolis', 'password': 'Jorge123@'})
        self.assertTrue(form.is_valid())

    def test_form_login_invalido(self):
        self.crear_usuario()
        form = LoginForm(
            None, data={'username': 'jorgeasolis', 'password': 'Jorge123@'})
        self.assertFalse(form.is_valid())

    def test_form_login_invalido_mensaje(self):
        self.crear_usuario()
        form = LoginForm(
            None, data={'username': 'jorgeasolis', 'password': 'Jorge123@'})
        self.assertEqual(
            form.errors['__all__'],
            ['El usuario o la contraseña son incorrectos,'
             + ' favor de intentarlo nuevamente.'])

    def test_login_username_nulo(self):
        self.crear_usuario()
        data_user = {
            'password': 'Jorge123@'
        }
        form = LoginForm(data=data_user)
        self.assertFalse(form.is_valid())

    def test_login_password_nulo(self):
        self.crear_usuario()
        data_user = {
            'username': 'jorgesolis'
        }
        form = LoginForm(data=data_user)
        self.assertFalse(form.is_valid())

    def test_login_password_nulo_mensaje(self):
        self.crear_usuario()
        data_user = {
            'username': 'jorgesolis'
        }
        form = LoginForm(data=data_user)
        self.assertEqual(form.errors['password'], [
                         'La contraseña es requerida, favor de verificarla.'])

    def crear_usuario(self):
        User.objects.create_user(
            username='jorgesolis',
            password='Jorge123@',
            email='jasg15_@gmail.com'
        )
