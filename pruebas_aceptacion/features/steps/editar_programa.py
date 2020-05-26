from behave import given, when, then
import time
from environment import login


@given(u'que inicio sesión en el sistema para ir a la sección de programas')
def step_impl(context):
    login(context)
    # pass


@given(u'presiono el botón "Editar"')
def step_impl(context):
    time.sleep(3)
    botones = context.td_programa[6].find_element_by_class_name('btn-success')
    # time.sleep(3)
    botones.click()
    time.sleep(3)


@given(u'que modifico el nombre del programa anterior por:'
       + ' "{nombre_programa}"')
def step_impl(context, nombre_programa):
    # pass
    # context.driver.get(context.url+'programa/editar/1')
    # context.driver.get(context.url+'programa/editar/'+str(context.id_programa))
    time.sleep(7)
    context.driver.find_element_by_id('id_nombre').clear()
    context.driver.find_element_by_id('id_nombre').send_keys(nombre_programa)


@given(u'deseo modificar el programa "{nombre_programa}"')
def step_impl(context, nombre_programa):
    context.nombre_programa = nombre_programa
    time.sleep(1)
    context.driver.find_elements_by_id('btnProgramas')[1].click()
    time.sleep(1)
    context.driver.find_elements_by_id('btnListaProgramas')[1].click()
    time.sleep(3)
    # context.driver.get(context.url+'programa/')
    programas = []
    rows = context.driver.find_elements_by_tag_name('tr')
    # programas = [row.find_elements_by_tag_name('td')[1].text for
    # row in rows[1:]]
    for row in rows[1:]:
        td_programa = row.find_elements_by_tag_name('td')
        programas.append(td_programa[1].text)
        if td_programa[1].text == nombre_programa:
            context.id_programa = row.find_elements_by_tag_name('td')[0].text
            context.td_programa = td_programa
    context.test.assertIn(nombre_programa, programas)


@when(u'presiono el botón de "Guardar cambios" en la edición')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-primary').click()


@then(u'el sistema permite ver el mensaje de "{mensaje_de_modificacion}"'
      + ' en edición.')
def step_impl(context, mensaje_de_modificacion):
    time.sleep(2)
    mensaje_exito = context.driver.find_element_by_id('mensaje').text
    context.test.assertEqual(mensaje_de_modificacion, mensaje_exito)


@then(u'el sistema permite ver el mensaje'
      + ' de "{mensaje_de_numero_beneficiarios_incorrecto}".')
def step_impl(context, mensaje_de_numero_beneficiarios_incorrecto):
    time.sleep(2)
    # mensaje_error = context.driver.find_element_by_id('mensaje').text
    context.test.assertIn(
        mensaje_de_numero_beneficiarios_incorrecto, context.driver.page_source)


@given(u'que modifico el número de beneficiarios anterior'
       + ' por: "{nuevo_numero_beneficiarios}"')
def step_impl(context, nuevo_numero_beneficiarios):
    context.driver.find_element_by_id('id_numero_beneficiarios').clear()
    context.driver.find_element_by_id(
        'id_numero_beneficiarios').send_keys(nuevo_numero_beneficiarios)
