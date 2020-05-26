from behave import given, when, then
import time
from environment import login


@given(u'que ingreso al sistema')
def step_impl(context):
    login(context)
    context.driver.get(context.url+'proyectos/nuevo')


@when(u'doy click en el botón de "Proyectos"')
def step_impl(context):
    context.driver.find_element_by_id('btnProyectos').click()
    context.driver.find_element_by_id('btnListaProyectos').click()


@then(u'se muestra la información del proyecto "{nombre_proyecto}"'
      + ' en la lista.')
def step_impl(context, nombre_proyecto):
    time.sleep(3)
    rows = context.driver.find_elements_by_tag_name('tr')
    proyectos = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]
    time.sleep(4)
    context.test.assertIn(nombre_proyecto, proyectos)


@then(u'no puedo ver al proyecto "{nombre_proyecto}" en la lista.')
def step_impl(context, nombre_proyecto):
    rows = context.driver.find_elements_by_tag_name('tr')
    proyectos = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]
    context.test.assertNotIn(nombre_proyecto, proyectos)
