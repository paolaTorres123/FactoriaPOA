from behave import given, when, then
import time
from environment import login


@given(u'que deseo reactivar el proyecto "Emprendimiento"')
def step_impl(context):
    login(context)
    context.driver.get(context.url+'proyectos/')
    rows = context.driver.find_elements_by_tag_name('tr')
    proyectos = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]


@when(u'presiono el botón “Activar”')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-success').click()
    time.sleep(2)


@then(u'te redirije a la lista de los proyectos, donde ya'
      + ' aparecera el proyecto activado.')
def step_impl(context):
    time.sleep(1)
    context.driver.get(context.url+'proyectos/')


@when(u'intente encontrar el botón “{activar}”')
def step_impl(context, activar):
    time.sleep(3)
    rows = context.driver.find_elements_by_tag_name('tr')
    proyectos = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[4:]]
    context.test.assertNotIn(activar, proyectos)


@then(u'no se encuentra el botón "Activado" ya que el proyecto ya estaba'
      + ' activado, vuelve a cargar la lista.')
def step_impl(context):
    context.driver.get(context.url+'proyectos/')
