from django.test import TestCase
from django.urls import reverse
from programas.models import Programa, Partida, MetaPrograma, MetaReal
from unittest import skip


class TestViews(TestCase):

    def setUp(self, nombre="Programa para Jóvenes Zacatecanos",
              anio_ejercicio_fiscal=2019,
              recurso_asignado=600000,
              fuente='Trimestral'):
        self.programa = Programa(
            nombre=nombre,
            anio_ejercicio_fiscal=anio_ejercicio_fiscal,
            recurso_asignado=recurso_asignado,
            fuente=fuente,
            tipo='Mensual',
            status='Activo',
        )

        self.data = {
            'numero_partida': 3000,
            'nombre_partida': 'Partida de Tres Mil',
            'monto_partida': 6700.00,
            # 'programa' : Programa.objects.first().id,
        }

        self.data_programa = {
            'nombre': 'Programa de Recursos',
            'anio_ejercicio_fiscal': 1998,
            'recurso_asignado': 50000,
            'fuente': 'Nacional',
            'tipo': 'MEN',
            'status': 'ACT',
            'tipo_programa_p': 'APO',
            'numero_actividades': 7,
            'numero_beneficiarios': 900,
            'numero_hombres': 333,
            'numero_mujeres': 444,
            'edad': 'ADU',
            'numero_actividades_r': 5,
            'numero_beneficiarios_r': 500,
            'numero_hombres_r': 250,
            'numero_mujeres_r': 250,
            'edad_r': 'ADU',
            'numero_partida': 3000,
            'nombre_partida': 'Partida de Tres Mil',
            'monto_partida': 6700.00,
        }

    # Test para programa nuevo
    # Verificar que si puede acceder a la URL indicada
    def test_url_programa_crear(self):
        response = self.client.get('/programa/nuevo')
        self.assertEqual(response.status_code, 200)

    # Ahora se hace la prueba de llamada por el nombre
    def test_nombre_url_programa_crear(self):
        response = self.client.get(reverse('nuevo_programa'))
        self.assertEqual(response.status_code, 200)

    # Probar un template que yo quiero utilizar
    def test_template_correcto_programa_crear(self):
        response = self.client.get('/programa/nuevo')
        self.assertTemplateUsed(response, 'programas/programa_form.html')

    def test_titulo_se_encuentra_en_el_template_programa_nuevo(self):
        response = self.client.get('/programa/nuevo')
        titulo_pagina = '<title>Crear Nuevo Programa</title>'
        self.assertInHTML(titulo_pagina, response.rendered_content)

    def test_agrega_programa_form(self):
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.client.get('/programa/nuevo')
        self.assertEqual(Programa.objects.all().count(), 1)

    def test_anio_ejercicio_fis_formulario_se_encuentra_en_el_template(self):
        response = self.client.get('/programa/nuevo')
        label = '<p><label for="id_anio_ejercicio_fiscal">Año Fiscal:</label> '
        label += '<input type="number" name="anio_ejercicio_fiscal" value="0" '
        label += 'required id="id_anio_ejercicio_fiscal" class="form-control">'
        label += '</p>'
        self.assertInHTML(label, response.rendered_content)

    def test_no_agrega_sin_nombre_del_programa(self):
        self.data_programa['nombre'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_anio_fiscal_programa(self):
        self.data_programa['anio_ejercicio_fiscal'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_recurso_asignado_programa(self):
        self.data_programa['recurso_asignado'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_fuente_programa(self):
        self.data_programa['fuente'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_status_programa(self):
        self.data_programa['status'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_tipo_programa(self):
        self.data_programa['tipo'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_tipo_programa_p_programa(self):
        self.data_programa['tipo_programa_p'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    @skip
    def test_redirige_a_otra_url_despues_de_agregar_programa(self):
        response = self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(response.url, '/programa/')

    # Test para partida
    def test_agrega_partida_form(self):
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.client.get('/programa/nuevo')
        self.assertEqual(Programa.objects.all().count(), 1)

    def test_no_agrega_sin_numero_de_partida(self):
        self.data_programa['numero_partida'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_nombre_de_partida(self):
        self.data_programa['nombre_partida'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_monto_de_partida(self):
        self.data_programa['monto_partida'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    # Test para Meta Programada
    def test_agrega_meta_programada_form(self):
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.client.get('/programa/nuevo')
        self.assertEqual(Programa.objects.all().count(), 1)

    def test_no_agrega_sin_numero_de_actividades(self):
        self.data_programa['numero_actividades'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_numero_de_beneficiarios(self):
        self.data_programa['numero_beneficiarios'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_numero_de_hombres(self):
        self.data_programa['numero_hombres'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_numero_de_mujeres(self):
        self.data_programa['numero_mujeres'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_rango_edad(self):
        self.data_programa['edad'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    # Test para Meta Real
    def test_agrega_meta_real_form(self):
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.client.get('/programa/nuevo')
        self.assertEqual(Programa.objects.all().count(), 1)

    def test_no_agrega_sin_numero_de_actividades_reales(self):
        self.data_programa['numero_actividades_r'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_numero_de_beneficiarios_reales(self):
        self.data_programa['numero_beneficiarios_r'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_numero_de_hombres_reales(self):
        self.data_programa['numero_hombres_r'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_numero_de_mujeres_reales(self):
        self.data_programa['numero_mujeres_r'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    def test_no_agrega_sin_rango_edad_reales(self):
        self.data_programa['edad_r'] = ''
        self.client.post('/programa/nuevo', data=self.data_programa)
        self.assertEqual(Programa.objects.all().count(), 0)

    # Test para listar programas
    # Verificar que si puede acceder a la URL indicada
    def test_url_programa_listado(self):
        response = self.client.get('/programa/')
        self.assertEqual(response.status_code, 200)

    # Ahora se hace la prueba de llamada por el nombre
    def test_nombre_url_programa_listado(self):
        response = self.client.get(reverse('lista_programa'))
        self.assertEqual(response.status_code, 200)

    # Probar un template que yo quiero utilizar
    def test_template_correcto_programa_listado(self):
        response = self.client.get('/programa/')
        self.assertTemplateUsed(response, 'programas/programa_list.html')

    def test_titulo_se_encuentra_en_el_template_programa_listado(self):
        response = self.client.get('/programa/')
        titulo_pagina = '<title>Lista de Programas</title>'
        self.assertInHTML(titulo_pagina, response.rendered_content)

    def test_envio_datos_programas(self):
        self.guarda_programa_completo()
        response = self.client.get('/programa/')
        self.assertIn('object_list', response.context)

    def test_envio_programa_jovenes_datos(self):
        self.guarda_programa_completo()
        response = self.client.get('/programa/')
        # print(response.context['object_list'][0])
        self.assertEqual('Programa para Jóvenes 2',
                         response.context['object_list'][0].nombre)

    def test_se_encuentre_en_el_template_programa_jovenes(self):
        self.guarda_programa_completo()
        response = self.client.get('/programa/')
        self.assertContains(response, 'Programa para Jóvenes 2')

    def test_programa_joven_se_encuentre_en_template_dentro_de_td(self):
        self.guarda_programa_completo()
        response = self.client.get('/programa/')
        self.assertInHTML('<td>Programa para Jóvenes 2</td>',
                          response.rendered_content)

    # Tests para editar programas
    def test_url_programa_editar(self):
        # self.programa.save()
        self.guarda_programa_completo()
        id = Programa.objects.first().id
        response = self.client.get('/programa/editar/'+str(id))
        self.assertEqual(response.status_code, 200)

    def test_template_correcto_programa_editar(self):
        # self.programa.save()
        self.guarda_programa_completo()
        id = Programa.objects.first().id
        response = self.client.get('/programa/editar/' + str(id))
        self.assertTemplateUsed(response, 'programas/programa_edit.html')

    def test_editar_programa(self):
        # self.programa.save()
        self.guarda_programa_completo()
        id = Programa.objects.first().id
        data_solo_programa = {
            'nombre': 'Programa de Recursos Modificado en POST',
            'anio_ejercicio_fiscal': 1998,
            'recurso_asignado': 50000,
            'fuente': 'Nacional',
            'tipo': 'MEN',
            'status': 'ACT',
            'tipo_programa_p': 'APO',
            'numero_actividades': 7,
            'numero_beneficiarios': 900,
            'numero_hombres': 333,
            'numero_mujeres': 444,
            'edad': 'ADU',
            'numero_actividades_r': 5,
            'numero_beneficiarios_r': 500,
            'numero_hombres_r': 250,
            'numero_mujeres_r': 250,
            'edad_r': 'ADU',
            'numero_partida': 3000,
            'nombre_partida': 'Partida Modificado',
            'monto_partida': 6700.00,
        }
        self.client.post('/programa/editar/'+str(id), data=data_solo_programa)
        self.assertEqual(Programa.objects.first().nombre,
                         'Programa de Recursos Modificado en POST')

    def test_editar_partida(self):
        # self.programa.save()
        self.guarda_programa_completo()
        id = Programa.objects.first().id

        data_solo_partida = {
            'nombre': 'Programa de Recursos',
            'anio_ejercicio_fiscal': 1998,
            'recurso_asignado': 50000,
            'fuente': 'Nacional',
            'tipo': 'MEN',
            'status': 'ACT',
            'tipo_programa_p': 'APO',
            'numero_actividades': 7,
            'numero_beneficiarios': 900,
            'numero_hombres': 333,
            'numero_mujeres': 444,
            'edad': 'ADU',
            'numero_actividades_r': 5,
            'numero_beneficiarios_r': 500,
            'numero_hombres_r': 250,
            'numero_mujeres_r': 250,
            'edad_r': 'ADU',
            'numero_partida': 3000,
            'nombre_partida': 'Partida Modificado en POST',
            'monto_partida': 6700.00,
        }
        self.client.post('/programa/editar/'+str(id), data=data_solo_partida)
        self.assertEqual(Partida.objects.first().nombre_partida,
                         'Partida Modificado en POST')

    def test_editar_metas_reales(self):
        # self.programa.save()
        self.guarda_programa_completo()
        id = Programa.objects.first().id

        data_solo_meta_real = {
            'nombre': 'Programa de Recursos',
            'anio_ejercicio_fiscal': 1998,
            'recurso_asignado': 50000,
            'fuente': 'Nacional',
            'tipo': 'MEN',
            'status': 'ACT',
            'tipo_programa_p': 'APO',
            'numero_actividades': 7,
            'numero_beneficiarios': 900,
            'numero_hombres': 333,
            'numero_mujeres': 444,
            'edad': 'ADU',
            'numero_actividades_r': 5,
            'numero_beneficiarios_r': 500,
            'numero_hombres_r': 250,
            'numero_mujeres_r': 250,
            'edad_r': 'ADU',
            'numero_partida': 3000,
            'nombre_partida': 'Partida Modificado en POST',
            'monto_partida': 6700.00,
        }
        self.client.post('/programa/editar/'+str(id), data=data_solo_meta_real)
        self.assertEqual(MetaReal.objects.first().numero_actividades_r, 5)

    def test_editar_metas_esperadas(self):
        # self.programa.save()
        self.guarda_programa_completo()
        id = Programa.objects.first().id

        data_solo_meta_esperada = {
            'nombre': 'Programa de Recursos',
            'anio_ejercicio_fiscal': 1998,
            'recurso_asignado': 50000,
            'fuente': 'Nacional',
            'tipo': 'MEN',
            'status': 'ACT',
            'tipo_programa_p': 'APO',
            'numero_actividades': 7,
            'numero_beneficiarios': 900,
            'numero_hombres': 333,
            'numero_mujeres': 444,
            'edad': 'ADU',
            'numero_actividades_r': 5,
            'numero_beneficiarios_r': 500,
            'numero_hombres_r': 250,
            'numero_mujeres_r': 250,
            'edad_r': 'ADU',
            'numero_partida': 3000,
            'nombre_partida': 'Partida Modificado en POST',
            'monto_partida': 6700.00,
        }
        self.client.post('/programa/editar/'+str(id),
                         data=data_solo_meta_esperada)
        self.assertEqual(MetaPrograma.objects.first().numero_actividades, 7)

    def test_editar_nombre_incorrecto_form(self):
        # self.programa.save()
        self.guarda_programa_completo()
        id = Programa.objects.first().id
        data_solo_programa = {
            'nombre': '',
            'anio_ejercicio_fiscal': 1998,
            'recurso_asignado': 50000,
            'fuente': 'Nacional',
            'tipo': 'MEN',
            'status': 'ACT',
            'tipo_programa_p': 'APO',
            'numero_actividades': 7,
            'numero_beneficiarios': 900,
            'numero_hombres': 333,
            'numero_mujeres': 444,
            'edad': 'ADU',
            'numero_actividades_r': 5,
            'numero_beneficiarios_r': 500,
            'numero_hombres_r': 250,
            'numero_mujeres_r': 250,
            'edad_r': 'ADU',
            'numero_partida': 3000,
            'nombre_partida': 'Partida Modificado',
            'monto_partida': 6700.00,
        }
        self.client.post('/programa/editar/'+str(id), data=data_solo_programa)
        self.assertEqual(Programa.objects.first().nombre,
                         'Programa para Jóvenes 2')

    # Test para desactivar programa

    def test_boton_desactivar_programa_template(self):
        self.guarda_programa_completo()
        response = self.client.get('/programa/')
        id = Programa.objects.first().id

        # print(Programa.objects.first().status)
        self.assertInHTML(
            '<a href="/programa/desactivar/'+str(id) +
            '" class="btn btn-danger btn-sm">Desactivar</a>',
            response.rendered_content
        )

    def test_url_programa_desactivar_redirige(self):
        self.guarda_programa_completo()
        id = Programa.objects.first().id
        response = self.client.get('/programa/desactivar/'+str(id))
        self.assertEqual(response.status_code, 302)

    def test_url_programa_desactivar_redirige_URL_correcta(self):
        self.guarda_programa_completo()
        id = Programa.objects.first().id
        response = self.client.get('/programa/desactivar/'+str(id))
        self.assertEqual(response.url, '/programa/')

    def test_desactivar_programa_response(self):
        self.guarda_programa_completo()
        id = Programa.objects.first().id
        self.client.post('/programa/desactivar/'+str(id))
        self.assertNotEqual(Programa.objects.first().status, 'Act')

    def test_desactivar_programa_ya_desactivado(self):
        programa = Programa(
            nombre='Programa para Jóvenes Tres',
            anio_ejercicio_fiscal=2022,
            recurso_asignado=54501,
            fuente='Federal',
            tipo='Mensual',
            status='Inactivo',
        )
        programa.save()
        id = Programa.objects.first().id
        self.client.post('/programa/desactivar/'+str(id))
        self.assertNotEqual(Programa.objects.first().status, 'Act')

    # Test para reactivar programa
    def test_boton_reactivar_programa_template(self):
        programa = Programa(
            nombre='Programa para Jóvenes Tres',
            anio_ejercicio_fiscal=2022,
            recurso_asignado=54501,
            fuente='Federal',
            tipo='Mensual',
            status='Inactivo',
        )
        # self.guarda_programa_completo()
        programa.save()
        response = self.client.get('/programa/')
        id = Programa.objects.first().id
        self.assertInHTML(
            '<a href="/programa/reactivar/'+str(id) +
            '" class="btn btn-primary btn-sm">Reactivar</a>',
            response.rendered_content
        )

    def test_url_programa_reactivar_redirige(self):
        self.guarda_programa_completo()
        id = Programa.objects.first().id
        response = self.client.get('/programa/reactivar/'+str(id))
        self.assertEqual(response.status_code, 302)

    def test_reactivar_programa_response(self):
        # self.guarda_programa_completo()
        programa = Programa(
            nombre='Programa para Jóvenes Cuatro',
            anio_ejercicio_fiscal=2053,
            recurso_asignado=54501,
            fuente='Federal',
            tipo='Mensual',
            status='Inactivo',
        )
        programa.save()
        id = Programa.objects.first().id
        self.client.post('/programa/reactivar/'+str(id))
        self.assertEqual(Programa.objects.first().status, 'ACT')

    def test_url_programa_reactivar_redirige_URL_correcta(self):
        self.guarda_programa_completo()
        id = Programa.objects.first().id
        response = self.client.get('/programa/reactivar/'+str(id))
        self.assertEqual(response.url, '/programa/')

    def test_reactivar_usuario_ya_activado(self):
        programa = Programa(
            nombre='Programa para Jóvenes Tres',
            anio_ejercicio_fiscal=2022,
            recurso_asignado=54501,
            fuente='Federal',
            tipo='Mensual',
            status='Activo',
        )
        programa.save()
        id = Programa.objects.first().id
        self.client.post('/programa/reactivar/'+str(id))
        self.assertEqual(Programa.objects.first().status, 'Act')

    # Ahora se hace la prueba de llamada por el nombre
    # def test_nombre_url_programa_desactivar(self):
    #    response = self.client.get(reverse('desactivar_programa'))
    #    self.assertEqual(response.status_code, 200)

    def guarda_programa_completo(self):
        self.programa_com = Programa(
            nombre='Programa para Jóvenes 2',
            anio_ejercicio_fiscal=2020,
            recurso_asignado=54500,
            fuente='Federal',
            tipo='Mensual',
            status='Activo',
        )
        self.programa_com.save()
        self.partida_com = Partida(
            numero_partida=3000,
            nombre_partida='Partida de Tres Mil prueba',
            monto_partida=6700.00,
            programa=self.programa_com,
        )
        self.partida_com.save()
        self.metas_es_com = MetaPrograma(
            numero_actividades=5,
            numero_beneficiarios=100,
            numero_hombres=250,
            numero_mujeres=250,
            edad='Jóvenes',
            meta_esperada=True,
            programa=self.programa_com,
        )
        self.metas_es_com.save()
        self.metas_re_com = MetaReal(
            numero_actividades_r=99,
            numero_beneficiarios_r=100,
            numero_hombres_r=250,
            numero_mujeres_r=250,
            edad_r='Jóvenes',
            meta_esperada_r=False,
            programa_r=self.programa_com,
        )
        self.metas_re_com.save()
        return self.programa_com
