from django.test import TestCase
from django.urls import reverse
from proyectos.models import Proyectos, Actividades
from django.contrib.auth.models import User, Permission
from django.contrib.auth.models import Group


class TestViews(TestCase):

    def setUp(self, nombre_proyecto="Emprendimiento"):
        self.actividad = Actividades(
            nombre_actividad='Juegos',
            unidad_medida='Congresos',
            cantidad=100,
            saldo=120000
        )

        self.data = {
            'activo': True,
            'nombre_proyecto': nombre_proyecto
        }
        self.asigna_permisos_login()

    def test_url_proyectos_alta(self):
        respose = self.client.get('/proyectos/nuevo')
        self.assertEqual(respose.status_code, 200)

    def test_nombre_url_proyecto_crear(self):
        response = self.client.get(reverse('nuevo_proyecto'))
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_proyecto_lista(self):
        response = self.client.get(reverse('lista_proyectos'))
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_proyecto_agregar_act(self):
        response = self.client.get(reverse('agregar_actividad'))
        self.assertEqual(response.status_code, 200)

    def test_template_proyecto_alta(self):
        response = self.client.get('/proyectos/nuevo')
        self.assertTemplateUsed(response, 'proyectos/proyectos_form.html')

    def test_template_proyecto_lista_prpyectos(self):
        response = self.client.get('/proyectos/')
        self.assertTemplateUsed(response, 'proyectos/proyectos_list.html')

    def test_no_agrega_sin_nombre_proyecto(self):
        self.data['nombre_proyecto'] = ''
        self.client.post('/proyectos/nuevo', data=self.data)
        self.assertEqual(Proyectos.objects.all().count(), 0)

    def test_titulo_se_encuentra_en_el_template_proyectos(self):
        response = self.client.get('/proyectos/nuevo')
        titulo = '<title>Nuevo Proyecto</title>'
        self.assertInHTML(titulo, response.rendered_content)

    def test_campo_nombre_proyecto_en_template(self):
        response = self.client.get('/proyectos/nuevo')
        formulario = ' <p><label for="id_nombre_proyecto">Nombre proyecto:'
        formulario += '</label><input type="text"'
        formulario += 'name="nombre_proyecto" id="id_nombre_proyecto" '
        formulario += 'class="form-control" required maxlength="60"></p>'
        self.assertInHTML(formulario, response.rendered_content)

    def test_campo_nombre_actividad_en_template(self):
        response = self.client.get('/proyectos/nuevo')
        formulario = '<p><label for="id_nombre_actividad">'
        formulario += 'Nombre actividad:</label> <input type="text"'
        formulario += 'name="nombre_actividad" maxlength="60" class='
        formulario += '"form-control" id="id_nombre_actividad" required></p>'
        self.assertInHTML(formulario, response.rendered_content)

    def test_campo_unidad_medida_en_template(self):
        response = self.client.get('/proyectos/nuevo')
        formulario = '<p><label for="id_unidad_medida">Unidad medida:'
        formulario += '</label> <select name="unidad_medida" '
        formulario += 'class="form-control" id="id_unidad_medida">'
        formulario += '<option value="CON">Congresos</option>'
        formulario += '<option value="EVN">Eventos</option><option '
        formulario += 'value="CONF">'
        formulario += 'Conferencias</option></select></p>'
        self.assertInHTML(formulario, response.rendered_content)

    def test_campo_cantidad_en_template(self):
        response = self.client.get('/proyectos/nuevo')
        formulario = '<p><label for="id_cantidad">Cantidad:</label>'
        formulario += '<input type="number" name="cantidad" value="0"'
        formulario += 'class="form-control" required id="id_cantidad"></p>'
        self.assertInHTML(formulario, response.rendered_content)

    def test_campo_saldo_en_template(self):
        response = self.client.get('/proyectos/nuevo')
        formulario = '<p><label for="id_saldo">Saldo:</label>'
        formulario += '<input type="number" name="saldo" value="0.0"'
        formulario += 'class="form-control" id="id_saldo"'
        formulario += 'step="0.01" required></p>'
        self.assertInHTML(formulario, response.rendered_content)

    def test_envio_actividad(self):
        proyecto = self.agrega_proyecto()
        self.agrega_actividad(proyecto)
        response = self.client.get('/proyectos/')
        self.assertIn('object_list', response.context)

    def test_boton_crear_proyecto_en_template(self):
        response = self.client.get('/proyectos/nuevo')
        boton = '<button type="submit" class="btn btn-primary">'
        boton += 'Crear proyecto</button>'
        self.assertInHTML(boton, response.rendered_content)

# Test para editar proyectos
    def test_editar_proyecto_response(self):
        self.agrega_proyecto()
        id = Proyectos.objects.first().id
        response = self.client.get('/proyectos/editar/'+str(id))
        self.assertEqual(response.status_code, 200)

    def test_editar_proyecto_form(self):
        self.agrega_proyecto()
        id = Proyectos.objects.first().id
        data = {
            'nombre_proyecto': 'Emprendimiento'
        }
        self.client.post('/proyectos/editar/'+str(id), data=data)
        self.assertEqual(Proyectos.objects.first(
        ).nombre_proyecto, 'Emprendimiento')

    def test_proyecto_editar_response(self):
        self.agrega_proyecto()
        id = Proyectos.objects.first().id
        data = {
            'nombre_proyecto': ''
        }
        self.client.post('/proyectos/editar/'+str(id), data=data)
        self.assertEqual(Proyectos.objects.first(
        ).nombre_proyecto, 'Emprendimiento')

    # Test para listar
    def test_proyecto_agregado_correctamente(self):
        proyecto = self.agrega_proyecto()
        self.agrega_actividad(proyecto)
        response = self.client.get('/proyectos/')
        self.assertInHTML('<td>Emprendimiento</td>', response.rendered_content)

    def test_tabla_se_encuentra_en_template(self):
        response = self.client.get('/proyectos/')
        thead = '<thead class="thead-dark"><th>ID Proyecto</th><th>'
        thead += 'Nombre del proyecto</th><th>Ver Actividad</th><th>Editar'
        thead += '</th><th>Desactivar/Reactivar</th></thead>'
        self.assertInHTML(thead, response.rendered_content)

    # Test desactivar
    def test_agrega_activo_sin_valor(self):
        self.data['activo'] = ''
        self.client.post('/proyectos/', data=self.data)
        self.assertEqual(Proyectos.objects.all().count(), 0)

    def test_desactivar_proyecto_response(self):
        self.agrega_proyecto()
        id = Proyectos.objects.first().id
        self.client.post('/proyectos/desactivar/'+str(id))

    def test_desactivar_proyecto_ya_desactivado(self):
        proyecto = Proyectos(
            activo=False,
            nombre_proyecto='Emprendimiento'
        )
        proyecto.save()
        id = Proyectos.objects.first().id
        self.client.post('/proyectos/desactivar/'+str(id))

    def test_boton_desactivar_proyecto_template(self):
        proyecto = self.agrega_proyecto()
        response = self.client.get('/proyectos/')
        id = proyecto.id
        self.assertInHTML('<a href="/proyectos/desactivar/'+str(id) +
                          '" class="btn btn-danger btn-sm">Desactivar</a>',
                          response.rendered_content)

    # Test reactivar proyecto
    def test_reactivar_proyecto_response(self):
        self.agrega_proyecto()
        id = Proyectos.objects.first().id
        self.client.post('/proyectos/activar/'+str(id))

    def test_activar_proyecto_activado(self):
        self.agrega_proyecto()
        id = Proyectos.objects.first().id
        self.client.post('/proyectos/activar/'+str(id))

    def test_boton_activar_proyecto_template(self):
        proyecto = Proyectos(
            activo=False,
            nombre_proyecto='Emprendimiento'
        )
        proyecto.save()
        response = self.client.get('/proyectos/')
        id = proyecto.id
        self.assertInHTML(
            '<a href="/proyectos/activar/'+str(id) +
            '" class="btn btn-success btn-sm">Activar</a>',
            response.rendered_content
        )

    def agrega_actividad(self, proyecto):
        actividad = Actividades.objects.create(
            nombre_actividad='Juegos',
            unidad_medida='Congresos',
            cantidad=100,
            saldo=120000,
            proyecto=proyecto
        )
        return actividad

    def agrega_proyecto(self):
        proyecto = Proyectos.objects.create(
            activo=True,
            nombre_proyecto="Emprendimiento"

        )
        return proyecto

    def asigna_permisos_login(self):
        user = User.objects.create_user(
            username='cultEmprendedora',
            password='F@@ctoria12',
            email='cult_emprendedora@factoria.gob.mx'
        )
        new_group, created = Group.objects.get_or_create(
            name='director_operativo')
        new_subprograma, created = Group.objects.get_or_create(
            name='encargado_subprograma')
        new_subprograma.permissions.add(
            Permission.objects.get(codename='view_proyectos'))
        new_subprograma.permissions.add(
            Permission.objects.get(codename='add_proyectos'))
        new_subprograma.permissions.add(
            Permission.objects.get(codename='change_proyectos'))
        new_subprograma.permissions.add(
            Permission.objects.get(codename='add_actividades'))
        new_subprograma.permissions.add(
            Permission.objects.get(codename='view_actividades'))
        user.groups.add(new_subprograma)
        self.client.login(username='cultEmprendedora', password='F@@ctoria12')
