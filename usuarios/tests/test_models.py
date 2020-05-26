from django.test import TestCase
from usuarios.models import Administrativo
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class TestModels(TestCase):

    def setUp(self, nombre='jorgesolis',
              correo='jasg15_@hotmail.com', password='Jorge123@'):
        self.usuario = User(
            username=nombre,
            email=correo,
            password=password,
            is_superuser=True
        )
        self.administrativo = Administrativo(
            nombre='Jorge',
            primer_apellido='Solís',
            segundo_apellido='Galván',
            telefono='4949412345',
            foto='foto.png',
            usuario=self.usuario
        )

    def test_return_object_usuario(self):
        self.usuario.full_clean()
        self.usuario.save()
        self.assertEqual(User.objects.first().username, self.usuario.__str__())

    def test_nombre_es_requerido(self):
        usuario = User(
            email='jasg15_@hotmail.com',
            password='jorge123@'
        )
        with self.assertRaises(ValidationError):
            usuario.full_clean()

    def test_nombre_usuario_min_8_char(self):
        self.usuario.username = 'jorgeas'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_nombre_usuario_no_acepta_espacios(self):
        self.usuario.username = 'jorgea sg'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()

    def test_nombre_usuario_no_acepta_caracteres_especiales(self):
        self.usuario.username = 'jorgeas@1'
        self.administrativo.usuario = self.usuario

        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_nombre_usuario_no_acepta_numeros(self):
        self.usuario.username = 'jorgeas11'
        self.administrativo.usuario = self.usuario
        try:
            self.administrativo.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['username'][0])
            self.assertEqual(
                msg,
                'El nombre de usuario no sigue el formato solicitado,'
                + ' favor de verificarlo.')

    def test_usuario_duplicado(self):
        self.usuario.save()
        usuario2 = User(
            username='jorgesolis',
            email='jasg15_@hotmail.com',
            password='Jorge123@'
        )
        try:
            usuario2.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['username'][0])
            self.assertEqual(msg, 'A user with that username already exists.')

    def test_correo_es_requerido(self):
        usuario = User(
            username='jorgeasg',
            password='jorge123@'
        )
        self.administrativo.usuario = usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_email_incorrecto(self):
        self.usuario.email = 'jasg15@gmail'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()

    def test_email_incorrecto_espacios(self):
        self.usuario.email = 'jasg15@gmail. com'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()

    def test_email_incorrecto_max_caracteres(self):
        self.usuario.email = 'jasg15@gmail.com'*10
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()

    def test_email_incorrecto_min_caracteres(self):
        self.usuario.email = 'j@g'
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()

    def test_email_duplicado(self):
        self.usuario.save()
        usuario2 = User(
            username='jorgeasolis',
            email='jasg15_@hotmail.com',
            password='Jorge123@'
        )
        try:
            usuario2.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['email'][0])
            self.assertEqual(
                msg,
                'El correo electrónico ingresado ya se encuentra registrado'
                + ' en el sistema. Favor de verificarlo.')

    def test_password_es_requerido(self):
        usuario = User(
            username='jorgeasg',
            email='jasg15_@hotmail.com'
        )
        with self.assertRaises(ValidationError):
            usuario.full_clean()

    def test_password_incorrecto(self):
        self.usuario.password = 'jorgeasg'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_password_correcto(self):
        self.usuario.password = 'Jorgeasg15.'
        self.usuario.full_clean()
        self.usuario.save()
        self.assertEqual(User.objects.first().password, self.usuario.password)

    def test_password_incorrecto_max_caracteres(self):
        self.usuario.password = 'jorgeasg'*7
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_password_incorrecto_min_caracteres(self):
        self.usuario.password = 'jor'
        try:
            self.usuario.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['password'][0])
            self.assertEqual(
                msg,
                'La contraseña no sigue el formato solicitado: Mínimo 8 '
                + 'caracteres, máximo 50 caracteres mínimo una mayúscula,'
                + ' mínimo una minúscula, mínimo un número y mínimo un '
                + 'símbolo, favor de verificarla.')

    # Tests para modelo Administrativo

    def test_return_object_administrativo(self):
        self.usuario.full_clean()
        self.usuario.save()
        self.administrativo.usuario = self.usuario
        self.administrativo.full_clean()
        self.administrativo.save()
        self.assertEqual(
            Administrativo.objects.first().__str__(),
            self.administrativo.__str__())

    def test_nombre_requerido(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.nombre = None
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_nombre_formato_incorrecto_numeros(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.nombre = 'Jorge1'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_nombre_formato_incorrecto_caracteres_especiales(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.nombre = 'Jorge+'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_nombre_max_caracteres(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.nombre = 'a'*51
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_nombre_max_caracteres_mensaje(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.nombre = 'a'*51
        self.administrativo.usuario = self.usuario
        try:
            self.administrativo.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['nombre'][0])
            self.assertEqual(
                msg,
                'La longitud máxima del nombre es de 50 caracteres.')

    def test_nombre_min_caracteres(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.nombre = 'jo'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_nombre_espacio_al_inicio(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.nombre = ' Jorge'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_primer_apellido_requerido(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.primer_apellido = None
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_primer_apellido_formato_incorrecto_numeros(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.primer_apellido = 'Solis1'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_primer_apellido_formato_incorrecto_numeros_mensaje(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.primer_apellido = 'Solis1'
        self.administrativo.usuario = self.usuario
        try:
            self.administrativo.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['primer_apellido'][0])
            self.assertEqual(
                msg,
                'Formato del primer apellido incorrecto, favor de veriicarlo.'
            )

    def test_primer_apellido_formato_incorrecto_caracteres_especiales(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.primer_apellido = 'Solis+'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_primer_apellido_max_caracteres(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.primer_apellido = 'a'*51
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_primer_apellido_min_caracteres(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.primer_apellido = 'so'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_primer_apellido_espacio_al_inicio(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.primer_apellido = ' Solis'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_segundo_apellido_no_requerido(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.segundo_apellido = ''
        self.administrativo.usuario = self.usuario
        self.administrativo.full_clean()
        self.administrativo.save()
        self.assertEqual(
            Administrativo.objects.first().__str__(),
            self.administrativo.__str__())

    def test_segundo_apellido_formato_incorrecto_numeros(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.segundo_apellido = 'Solis1'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_segundo_apellido_formato_incorrecto_caracteres_especiales(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.segundo_apellido = 'Solis+'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_segundo_apellido_max_caracteres(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.segundo_apellido = 'a'*51
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_segundo_apellido_min_caracteres(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.segundo_apellido = 'so'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_segundo_apellido_min_caracteres_mensaje(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.segundo_apellido = 'So'
        self.administrativo.usuario = self.usuario
        try:
            self.administrativo.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['segundo_apellido'][0])
            self.assertEqual(
                msg,
                'La longitud mínima del segundo apellido es de 3 caracteres.')

    def test_segundo_apellido_espacio_al_inicio(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.segundo_apellido = ' Solis'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_foto_formato_incorrecto(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.foto = 'foto.gif'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_foto_formato_incorrecto_mensaje(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.foto = 'foto.gif'
        self.administrativo.usuario = self.usuario
        try:
            self.administrativo.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['foto'][0])
            self.assertEqual(msg, 'Formato de imagen inválido.')

    def test_foto_formato_correcto(self):
        self.usuario.full_clean()
        self.usuario.save()
        self.administrativo.usuario = self.usuario
        self.administrativo.full_clean()
        self.administrativo.save()
        self.assertEqual(
            Administrativo.objects.first().__str__(),
            self.administrativo.__str__())

    def test_telefono_longitud_minima_incorrecta(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.telefono = '494941234'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_telefono_longitud_maxima_incorrecta(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.telefono = '49494123411'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_telefono_requerido(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.telefono = None
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_telefono_con_caracteres_especiales(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.telefono = '+494941234'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_telefono_con_espacios(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.telefono = '494941234 '
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_telefono_con_letras(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.telefono = '494941234f'
        self.administrativo.usuario = self.usuario
        with self.assertRaises(ValidationError):
            self.administrativo.full_clean()

    def test_telefono_formato_incorrecto_mensaje(self):
        self.usuario.full_clean()
        self.usuario.save()

        self.administrativo.telefono = '492121234g'
        self.administrativo.usuario = self.usuario
        try:
            self.administrativo.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['telefono'][0])
            self.assertEqual(msg, 'Formato del número de teléfono incorrecto.')

    def test_usuario_requerido(self):
        administrativo = Administrativo(
            nombre='Jorge',
            primer_apellido='Solís',
            segundo_apellido='Galván',
            telefono='4949412345',
            foto='foto.png',
        )
        with self.assertRaises(ValidationError):
            administrativo.full_clean()
