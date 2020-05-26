from behave import when, then
import time


@when(u'encuentro el usuario "{usuario}" y presiono el'
      + ' botón de Desactivar cuenta')
def step_impl(context, usuario):
    rows = context.driver.find_elements_by_tag_name('tr')
    users = [row.find_elements_by_tag_name('td') for row in rows[1:]]

    for user in users:
        if user[1].text == usuario:
            user[4].find_element_by_class_name('btn-danger').click()
            break


@then(u'el sistema muestra el mensaje "{mensaje}" indicando'
      + ' que la desactivación fue exitosa.')
def step_impl(context, mensaje):
    time.sleep(2)
    mensaje_exito = context.driver.find_element_by_id('mensaje').text
    context.test.assertEqual(mensaje, mensaje_exito)


@then(u'no puedo encontrar el botón de "{nombre_boton}" ya que'
      + ' la cuenta se encuentra desactivada.')
def step_impl(context, nombre_boton):
    button = context.user[4].find_element_by_tag_name('a').text
    context.test.assertNotEqual(button, nombre_boton)
