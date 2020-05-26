from behave import given, when, then
import time


@given(u'que ingreso a la página de inicio de sesión')
def step_impl(context):
    context.driver.get(context.url+'usuarios/login')


@given(u'completo mis datos, usuario: "{user}" y la contraseña: "{password}"')
def step_impl(context, user, password):
    context.driver.find_element_by_id('id_username').send_keys(user)
    context.driver.find_element_by_id('id_password').send_keys(password)


@when(u'presiono el botón de "Iniciar Sesión"')
def step_impl(context):
    context.driver.find_element_by_id('btnLogin').click()


@then(u'puedo ver mi nombre de usuario: "{usuario}" en la'
      + ' parte superior de la página.')
def step_impl(context, usuario):
    time.sleep(2)
    username = context.driver.find_element_by_id('btnMenu').text
    context.test.assertEqual(username.lower(), usuario.lower())


@then(u'el sistema muestra el mensaje: "{mensaje_error}".')
def step_impl(context, mensaje_error):
    listas = context.driver.find_elements_by_class_name('errorlist')
    errores = [li.find_elements_by_tag_name('li')[0].text for li in listas[1:]]
    context.test.assertIn(mensaje_error, errores)
