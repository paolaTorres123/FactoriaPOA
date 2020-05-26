from behave import when, then
import time
from environment import login


@when(u'doy click en el botón del menú "Usuarios"')
def step_impl(context):
    login(context)
    time.sleep(2)
    context.driver.find_element_by_id('btnUsuarios').click()


@when(u'doy click en el botón de "Usuarios registrados"')
def step_impl(context):
    context.driver.find_element_by_id('btnListaUsuarios').click()


@then(u'puedo ver al usuario "{usuario}" en la lista.')
def step_impl(context, usuario):
    time.sleep(2)
    rows = context.driver.find_elements_by_tag_name('tr')
    usuarios = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]
    context.test.assertIn(usuario, usuarios)


@then(u'no puedo ver al usuario "{usuario}" en la lista.')
def step_impl(context, usuario):
    time.sleep(2)
    rows = context.driver.find_elements_by_tag_name('tr')
    usuarios = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]
    context.test.assertNotIn(usuario, usuarios)
