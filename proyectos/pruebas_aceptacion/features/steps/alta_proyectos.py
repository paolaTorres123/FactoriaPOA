from behave import given, when, then
import time
from environment import login


@given(u'que ingreso los datos correctos para crear un proyecto como; nombre'
       + ' proyecto: "{nombre_proyecto}"; nombre_actividad:'
       + ' "{nombre_actividad}"; unidad de medida: "{unidad_medida}";'
       + ' cantidad "{cantidad}"; saldo: "{saldo}"')
def step_impl(context, nombre_proyecto, nombre_actividad, unidad_medida,
              cantidad, saldo):
    login(context)
    context.driver.get(context.url+'proyectos/nuevo')
    context.driver.find_element_by_id(
        'id_nombre_proyecto').send_keys(nombre_proyecto)
    context.driver.find_element_by_id(
        'id_nombre_actividad').send_keys(nombre_actividad)
    context.driver.find_element_by_id(
        'id_unidad_medida').send_keys(unidad_medida)
    context.driver.find_element_by_id('id_cantidad').clear()
    context.driver.find_element_by_id('id_cantidad').send_keys(cantidad)
    context.driver.find_element_by_id('id_saldo').clear()
    context.driver.find_element_by_id('id_saldo').send_keys(saldo)


@when(u'presione el botón  "Crear proyecto"')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-primary').click()


@then(u'puedo ver el proyecto "{nombre_proyecto}" en la lista de proyectos.')
def step_impl(context, nombre_proyecto):
    rows = context.driver.find_elements_by_tag_name('tr')
    proyectos = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]
    context.test.assertIn(nombre_proyecto, proyectos)


@given(u'que ingreso los datos incorrectos para crear un proyecto como;'
       + ' nombre proyecto: "{nombre_proyecto}"; nombre_actividad:'
       + ' "{nombre_actividad}"; unidad de medida: "{unidad_medida}";'
       + ' cantidad "{cantidad}"; saldo: "{saldo}"')
def step_impl(context, nombre_proyecto, nombre_actividad, unidad_medida,
              cantidad, saldo):
    login(context)
    context.driver.get(context.url+'proyectos/nuevo')
    context.driver.find_element_by_id(
        'id_nombre_proyecto').send_keys(nombre_proyecto)
    context.driver.find_element_by_id(
        'id_nombre_actividad').send_keys(nombre_actividad)
    context.driver.find_element_by_id(
        'id_unidad_medida').send_keys(unidad_medida)
    context.driver.find_element_by_id('id_cantidad').clear()
    context.driver.find_element_by_id('id_cantidad').send_keys(cantidad)
    context.driver.find_element_by_id('id_saldo').clear()
    context.driver.find_element_by_id('id_saldo').send_keys(saldo)


@when(u'presiono el botón "Crear proyecto"')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-primary').click()


@then(u'el sistema manda un mensaje diciendo "{mensaje_error}"')
def step_impl(context, mensaje_error):
    time.sleep = 4
    listas = context.driver.find_elements_by_class_name('errorlist')
    errores = [li.find_elements_by_tag_name('li')[0].text for li in listas[0:]]
    context.test.assertIn(mensaje_error, errores)
