from behave import given, when, then
import time
from environment import login


@given(u'que inicio sesión en el sistema como Director operativo')
def step_impl(context):
    login(context)


@given(u'me dirijo a la lista de usuarios')
def step_impl(context):
    context.driver.get(context.url+'usuarios/')


@when(u'encuentro el usuario "{usuario}" y presiono el botón'
      + ' de "Reactivar cuenta"')
def step_impl(context, usuario):
    rows = context.driver.find_elements_by_tag_name('tr')
    users = [row.find_elements_by_tag_name('td') for row in rows[1:]]

    for user in users:
        if user[1].text == usuario:
            user[4].find_element_by_class_name('btn-success').click()
            break


@then(u'el sistema muestra el mensaje "{mensaje}" indicando que'
      + ' la reactivación fue exitosa.')
def step_impl(context, mensaje):
    time.sleep(2)
    mensaje_exito = context.driver.find_element_by_id('mensaje').text
    context.test.assertEqual(mensaje, mensaje_exito)


@when(u'encuentro el usuario "{usuario}"')
def step_impl(context, usuario):
    rows = context.driver.find_elements_by_tag_name('tr')
    users = [row.find_elements_by_tag_name('td') for row in rows[1:]]

    for user in users:
        if user[1].text == usuario:
            context.user = user
            break


@then(u'no puedo encontrar el botón de "{nombre_boton}" ya que la'
      + ' cuenta se encuentra activada.')
def step_impl(context, nombre_boton):
    button = context.user[4].find_element_by_tag_name('a').text
    context.test.assertNotEqual(button, nombre_boton)
