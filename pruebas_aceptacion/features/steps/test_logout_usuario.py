from behave import given, when, then
import time
from environment import login


@given(u'que inicié sesión en el sistema y deseo cerrar mi sesión')
def step_impl(context):
    login(context)


@when(u'presiono el botón de "Cerrar Sesión"')
def step_impl(context):
    context.driver.find_element_by_id('btnMenu').click()
    context.driver.find_element_by_id('btnCerrarSesion').click()


@then(u'el sistema pregunta lo siguiente: "¿Estás seguro de que deseas cerrar'
      + ' la sesión?", al confirmar, la sesión es cerrada')
def step_impl(context):
    context.driver.find_element_by_id('btnCerrar').click()


@then(u'me redirije a la pégina de Inicio de Sesión')
def step_impl(context):
    time.sleep(2)
    titulo = context.driver.find_element_by_id('btnLogin').text
    context.test.assertEqual(titulo.lower(), "iniciar sesión")


@then(u'el sistema pregunta lo siguiente: "¿Estás seguro de que deseas cerrar'
      + ' la sesión?", al no confirmar la operación, la sesión no es cerrada')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id('btnCancelar').click()


@then(u'puedo seguir viendo mi nombre de usuario: "{usuario}" en la parte'
      + ' superior de la pantalla.')
def step_impl(context, usuario):
    time.sleep(2)
    nombre = context.driver.find_element_by_id('btnMenu').text
    context.test.assertEqual(nombre.lower(), usuario.lower())
