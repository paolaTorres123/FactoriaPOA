from behave import given, when, then
import time
from environment import login


@given(u'que quiero modificar el proyecto "Emprendimiento"'
       + ' por "{nombre_proyecto}"')
def step_impl(context, nombre_proyecto):
    login(context)
    context.driver.get(context.url+'proyectos/')
    rows = context.driver.find_elements_by_tag_name('tr')
    proyectos = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]
    context.driver.find_element_by_class_name('btn-warning').click()
    time.sleep(4)
    context.driver.find_element_by_id('id_nombre_proyecto').clear()
    context.driver.find_element_by_id(
        'id_nombre_proyecto').send_keys(nombre_proyecto)


@when(u'presione el botón "Guardar cambios"')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-primary').click()


@then(u'te redirige a la lista de proyectos para que se vea el cambio.')
def step_impl(context):
    context.driver.get(context.url+'proyectos/')


@given(u'que quiero modificar el "Emprendimineto" por "{nombre_proyecto}"')
def step_impl(context, nombre_proyecto):
    login(context)
    context.driver.get(context.url+'proyectos/')
    rows = context.driver.find_elements_by_tag_name('tr')
    proyectos = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]
    context.driver.find_element_by_class_name('btn-warning').click()
    time.sleep(4)
    context.driver.find_element_by_id('id_nombre_proyecto').clear()
    context.driver.find_element_by_id(
        'id_nombre_proyecto').send_keys(nombre_proyecto)


@then(u'se muestra el mensaje "{mensaje_error_editar}" el marca el error')
def step_impl(context, mensaje_error_editar):
    time.sleep = 2
    context.test.assertIn(mensaje_error_editar, context.driver.page_source)


@then(u'te redirige al formulario.')
def step_impl(context):
    context.driver.get(context.url+'proyectos/')
