from django.test import TestCase
from django.urls import reverse
from usuarios.models import Administrativo
from django.contrib.auth.models import User, Permission
from django.contrib.auth.models import Group


class TestViews(TestCase):
    def setUp(self):
        self.usuario = User(
            username='jorgesolis',
            email='jasg15_@gmail.com',
            password='Jorgeasg15@',
            is_superuser=True,
            is_active=True
        )

        self.data_admin = {
            'nombre': 'Jorge Alfonso',
            'primer_apellido': 'Solís',
            'segundo_apellido': 'Galván',
            'telefono': 4941056009,
            'foto': 'C:\\Users\\Lenovo\\Pictures\\3.png',
            'username': 'jorgesolis',
            'email': 'jasg15_@gmail.com',
            'password': 'Jorgeasg15@',
            'password_re': 'Jorgeasg15@',
            'is_superuser': True,
        }

    # Tests para nuevo usuario
    def test_crea_cuenta_response(self):
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/nuevo')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_nuevo_usuario_response(self):
        self.asigna_permisos_login()
        response = self.client.get(reverse('nuevo_usuario'))
        self.assertEqual(response.status_code, 200)

    def test_template_correcto_nuevo_usuario(self):
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/nuevo')
        self.assertTemplateUsed(response, 'usuarios/usuario_form.html')

    def test_titulo_se_encuentra_en_el_template(self):
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/nuevo')
        titulo = '<title> Crear cuenta de usuario </title>'
        self.assertInHTML(titulo, response.rendered_content)

    def test_agrega_administrativo_form(self):
        self.asigna_permisos_login()
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 1)

    def test_no_agrega_sin_nombre_usuario(self):
        self.asigna_permisos_login()
        self.data_admin['username'] = ''
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_con_nombre_usuario_con_espacios(self):
        self.asigna_permisos_login()
        self.data_admin['username'] = 'jorge alfonso'
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_con_nombre_usuario_min_caracteres(self):
        self.asigna_permisos_login()
        self.data_admin['username'] = 'jorge'
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_con_nombre_usuario_max_caracteres(self):
        self.asigna_permisos_login()
        self.data_admin['username'] = 'jorge'*5
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_usuario_sin_correo(self):
        self.asigna_permisos_login()
        # Se agrega porque al crear el usuario para iniciar sesión y crear otro
        # usuario, ya se guarda uno en la BD
        no_users = User.objects.all().count()
        self.data_admin['email'] = ''
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(User.objects.all().count(), no_users)

    def test_no_agrega_usuario_correo_con_espacios(self):
        self.asigna_permisos_login()
        no_users = User.objects.all().count()
        self.data_admin['email'] = 'jasg15 @hotmail.com'
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(User.objects.all().count(), no_users)

    def test_no_agrega_usuario_correo_min_caracteres(self):
        self.asigna_permisos_login()
        no_users = User.objects.all().count()
        self.data_admin['email'] = 'j@'
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(User.objects.all().count(), no_users)

    def test_no_agrega_usuario_correo_max_caracteres(self):
        self.asigna_permisos_login()
        no_users = User.objects.all().count()
        self.data_admin['email'] = 'jasg15@gmail.com'*30
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(User.objects.all().count(), no_users)

    def test_no_agrega_usuario_sin_password(self):
        self.asigna_permisos_login()
        self.data_admin['password'] = ''
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_usuario_password_min_caracteres(self):
        self.asigna_permisos_login()
        self.data_admin['password'] = 'hola1'
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_usuario_password_max_caracteres(self):
        self.asigna_permisos_login()
        self.data_admin['password'] = 'hola12'*10
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_usuario_sin_nombre(self):
        self.asigna_permisos_login()
        self.data_admin['nombre'] = ''
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_usuario_nombre_max_caracteres(self):
        self.asigna_permisos_login()
        self.data_admin['nombre'] = 'jorgealfonso'*10
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_usuario_nombre_formato_incorrecto(self):
        self.asigna_permisos_login()
        self.data_admin['nombre'] = ' jorge alfonso'
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_usuario_sin_primer_apellido(self):
        self.asigna_permisos_login()
        self.data_admin['primer_apellido'] = ''
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_usuario_primer_apellido_max_caracteres(self):
        self.asigna_permisos_login()
        self.data_admin['primer_apellido'] = 'solisg'*10
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_usuario_primer_apellido_formato_incorrecto(self):
        self.asigna_permisos_login()
        self.data_admin['primer_apellido'] = ' solis'
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_agrega_usuario_sin_segundo_apellido(self):
        self.asigna_permisos_login()
        self.data_admin['segundo_apellido'] = ''
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 1)

    def test_no_agrega_usuario_segundo_apellido_formato_incorrecto(self):
        self.asigna_permisos_login()
        self.data_admin['segundo_apellido'] = ' sanchez'
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_usuario_segundo_apellido_max_caracteres(self):
        self.asigna_permisos_login()
        self.data_admin['segundo_apellido'] = 'sanchez'*10
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_usuario_sin_telefono(self):
        self.asigna_permisos_login()
        self.data_admin['telefono'] = ''
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_no_agrega_usuario_telefono_formato_incorrecto(self):
        self.asigna_permisos_login()
        self.data_admin['telefono'] = '49494123'
        self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(Administrativo.objects.all().count(), 0)

    def test_redirige_despues_de_agregar_usuario(self):
        self.asigna_permisos_login()
        response = self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(response.url, '/usuarios/')

    def test_redirige_si_no_inicio_sesion_agregar_usuario(self):
        response = self.client.post('/usuarios/nuevo', data=self.data_admin)
        self.assertEqual(response.url, '/usuarios/login?next=/usuarios/nuevo')

    # Tests para listar usuarios

    def test_redirige_si_no_inicio_sesion_listar_usuarios(self):
        response = self.client.post('/usuarios/')
        self.assertEqual(response.url, '/usuarios/login?next=/usuarios/')

    def test_listar_cuentas_response(self):
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_lista_usuarios(self):
        self.asigna_permisos_login()
        response = self.client.get(reverse('lista_usuarios'))
        self.assertEqual(response.status_code, 200)

    def test_template_correcto_listar_cuentas(self):
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/')
        self.assertTemplateUsed(response, 'usuarios/usuarios.html')

    def test_titulo_se_encuentra_en_el_template_lista_usuarios(self):
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/')
        titulo = '<h2 class="aex" >Usuarios</h2>'
        self.assertInHTML(titulo, response.rendered_content)

    def test_envio_datos_usuarios(self):
        self.guarda_administrativo()
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/')
        self.assertIn('object_list', response.context)

    def test_envio_jorgeasolis_datos_usuario(self):
        self.guarda_administrativo()
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/')
        self.assertEqual(
            'jorgesolis',
            response.context['object_list'][0]['usuario'].username)

    def test_jorgeasolis_se_encuentre_en_el_template(self):
        self.guarda_administrativo()
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/')
        self.assertContains(response, 'jorgesolis')

    def test_jorgeasolis_se_encuentre_en_el_template_en_un_td(self):
        self.guarda_administrativo()
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/')
        self.assertInHTML('<td>jorgesolis</td>', response.rendered_content)

    # Tests para Login

    def test_login_response(self):
        response = self.client.get('/usuarios/login')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_login_response(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_template_correcto_login(self):
        response = self.client.get('/usuarios/login')
        self.assertTemplateUsed(response, 'usuarios/login.html')

    def test_titulo_se_encuentra_en_el_template_login(self):
        response = self.client.get('/usuarios/login')
        titulo = '<title> Inicio de sesión </title>'
        self.assertInHTML(titulo, response.rendered_content)

    def test_campo_usuario_se_encuentra_en_el_template(self):
        response = self.client.get('/usuarios/login')
        formulario = '<label for="id_username">Usuario:</label>'
        formulario += '<input class="au-input au-input--full" type="text" '
        formulario += 'name="username" id="id_username" placeholder'
        formulario += '="Nombre de usuario">'
        self.assertInHTML(formulario, response.rendered_content)

    def test_campo_password_se_encuentra_en_el_template(self):
        response = self.client.get('/usuarios/login')
        formulario = '<label for="id_password">Contraseña</label>'
        formulario += '<input class="au-input au-input--full" type="password" '
        formulario += 'name="password" id="id_password" placeholder'
        formulario += '="Contraseña">'
        self.assertInHTML(formulario, response.rendered_content)

    def test_redirige_despues_de_iniciar_sesion(self):
        User.objects.create_user(
            username='jorgesolis',
            password='Jorge123@',
            email='jasg15_@gmail.com'
        )
        data_login = {
            'username': 'jorgesolis',
            'password': 'Jorge123@',
        }
        response = self.client.post('/usuarios/login', data=data_login)
        self.assertEqual(response.url, '/principal/')

    # Tests para Logout

    def test_boton_cerrar_se_encuentra_en_el_template_base(self):
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/nuevo')
        boton = '<a href="javascript: cerrarSesion(\'/usuarios/logout\')" '
        boton += 'id="btnCerrarSesion"><i class="zmdi zmdi-power">'
        boton += '</i>Cerrar Sesión</a>'
        self.assertInHTML(boton, response.rendered_content)

    def test_modal_confirmacion_cerrar_se_encuentra_en_el_template_base(self):
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/nuevo')
        boton = '<h5 class="modal-title" id="exampleModalLabel">'
        boton += 'Confirmación</h5>'
        self.assertInHTML(boton, response.rendered_content)

    def test_logout_redireccion(self):
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/logout')
        self.assertEqual(response.url, '/usuarios/login')

    # Tests para editar usuario

    def test_editar_usuario_response(self):
        self.guarda_administrativo()
        id = User.objects.first().id
        response = self.client.get('/usuarios/editar/'+str(id))
        self.assertEqual(response.status_code, 200)

    def test_template_correcto_editar_usuario(self):
        self.guarda_administrativo()
        id = User.objects.first().id
        response = self.client.get('/usuarios/editar/'+str(id))
        self.assertTemplateUsed(response, 'usuarios/editar_usuario.html')

    def test_editar_usuario_form(self):
        self.guarda_administrativo()
        id = User.objects.first().id
        data = {
            'nombre': 'Jorge Alfonso',
            'primer_apellido': 'Solís',
            'segundo_apellido': 'Galván',
            'telefono': '4949412345',
            'foto': 'foto.png',
        }
        self.client.post('/usuarios/editar/'+str(id), data=data)
        self.assertEqual(
            Administrativo.objects.first().nombre, 'Jorge Alfonso')

    def test_editar_nombre_incorrecto_form(self):
        self.guarda_administrativo()
        id = User.objects.first().id
        data = {
            'nombre': '',
            'primer_apellido': 'Solís',
            'segundo_apellido': 'Galván',
            'telefono': '4949412345',
            'foto': 'foto.png',
        }
        self.client.post('/usuarios/editar/'+str(id), data=data)
        self.assertEqual(Administrativo.objects.first().nombre, 'Jorge')

    # Tests para desactivar usuario

    def test_redirige_si_no_inicio_sesion_desactivar_usuarios(self):
        response = self.client.post('/usuarios/desactivar/1')
        self.assertEqual(
            response.url, '/usuarios/login?next=/usuarios/desactivar/1')

    def test_desactivar_usuario_response(self):
        self.asigna_permisos_login()
        self.guarda_administrativo()
        id = User.objects.first().id
        self.client.post('/usuarios/desactivar/'+str(id))
        self.assertFalse(User.objects.first().is_active)

    def test_desactivar_usuario__ya_desactivado(self):
        self.asigna_permisos_login()
        usuario = User(
            username='jorgesolis',
            email='jasg15_@gmail.com',
            password='Jorge123@',
            is_superuser=True,
            is_active=False
        )
        usuario.save()
        id = User.objects.first().id
        self.client.post('/usuarios/desactivar/'+str(id))
        self.assertFalse(User.objects.first().is_active)

    def test_boton_desactivar_usuario_en_template(self):
        # Se crea un usuario activo
        user = self.guarda_administrativo()
        self.asigna_permisos_login()
        response = self.client.get('/usuarios/')
        id = user.id
        self.assertInHTML('<a href="/usuarios/desactivar/'+str(id) +
                          '" class="btn btn-danger btn-sm">Desactivar</a>',
                          response.rendered_content)

    # Tests para reactivar usuario

    def test_redirige_si_no_inicio_sesion_reactivar_usuarios(self):
        response = self.client.post('/usuarios/reactivar/1')
        self.assertEqual(
            response.url, '/usuarios/login?next=/usuarios/reactivar/1')

    def test_reactivar_usuario_response(self):
        self.asigna_permisos_login()
        usuario = User(
            username='jorgesolis',
            email='jasg15_@gmail.com',
            password='Jorge123@',
            is_superuser=True,
            is_active=False
        )
        usuario.save()
        id = User.objects.first().id
        self.client.post('/usuarios/reactivar/'+str(id))
        self.assertTrue(User.objects.first().is_active)

    def test_reactivar_usuario_ya_activado(self):
        self.asigna_permisos_login()
        self.guarda_administrativo()
        id = User.objects.first().id
        self.client.post('/usuarios/reactivar/'+str(id))
        self.assertTrue(User.objects.first().is_active)

    def test_boton_reactivar_usuario_en_template(self):
        # Se crea un usuario inactivo
        self.asigna_permisos_login()
        usuario = User(
            username='jorgesolis',
            email='jasg15_@gmail.com',
            password='Jorge123@',
            is_superuser=True,
            is_active=False
        )
        usuario.save()
        administrativo = Administrativo(
            nombre='Jorge',
            primer_apellido='Solís',
            segundo_apellido='Galván',
            telefono='4949412345',
            foto='foto.png',
            usuario=usuario
        )
        administrativo.save()
        id = usuario.id
        response = self.client.get('/usuarios/')
        self.assertInHTML('<a href="/usuarios/reactivar/'+str(id) +
                          '" class="btn btn-success btn-sm">Reactivar</a>',
                          response.rendered_content)

    def login(self):
        self.usuario.save()
        self.client.login(username='jorgesolis', password='Jorgeasg15@')

    def guarda_administrativo(self):
        self.usuario = User(
            username='jorgesolis',
            email='jasg15_@gmail.com',
            password='Jorge123@',
            is_superuser=True
        )
        self.usuario.save()
        self.administrativo = Administrativo(
            nombre='Jorge',
            primer_apellido='Solís',
            segundo_apellido='Galván',
            telefono='4949412345',
            foto='foto.png',
            usuario=self.usuario
        )
        self.administrativo.save()
        return self.usuario

    def asigna_permisos_login(self):
        user1 = User.objects.create_user(
            username='dirOperativo',
            password='F@@ctoria12',
            email='dir_operativo@factoria.gob.mx',
            is_staff=True
        )
        new_group, created = Group.objects.get_or_create(
            name='director_operativo')
        new_subprograma, created = Group.objects.get_or_create(
            name='encargado_subprograma')
        new_group.permissions.add(Permission.objects.get(codename='view_user'))
        new_group.permissions.add(Permission.objects.get(codename='add_user'))
        user1.groups.add(new_group)
        self.client.login(username='dirOperativo', password='F@@ctoria12')
