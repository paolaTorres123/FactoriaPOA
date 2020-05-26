from behave import given, when, then
import time
from environment import login


@given(u'que deseo desactivar el proyecto "Emprendiminto"')
def step_impl(context):
    login(context)
    context.driver.get(context.url+'proyectos/')
    rows = context.driver.find_elements_by_tag_name('tr')
    proyectos = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]


@when(u'presiono el botón “Desactivar”')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-danger').click()
    time.sleep(3)


@then(u'te redirije a la lista de los proyectos, donde ya aparecera'
      + ' el proyecto desactivado.')
def step_impl(context):
    time.sleep(3)
    context.driver.get(context.url+'proyectos/')


@given(u'que deseo desactivar el proyecto "Empredimiento"')
def step_impl(context):
    login(context)
    rows = context.driver.find_elements_by_tag_name('tr')
    proyectos = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]
    time.sleep(2)


@when(u'intente encontrar el botón "{desactivar}"')
def step_impl(context, desactivar):
    time.sleep(3)
    rows = context.driver.find_elements_by_tag_name('tr')
    proyectos = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[4:]]
    context.test.assertNotIn(desactivar, proyectos)


@then(u'no encuentra el botón "Desactivar" ya que ya'
      + ' esta desactivado, vuelve a cargar la lista.')
def step_impl(context):
    context.driver.get(context.url+'proyectos/')
    time.sleep(2)
