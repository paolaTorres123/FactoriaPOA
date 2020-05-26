from behave import given, when, then
import time
from environment import login


@given(u'que inicio sesión en el sistema')
def step_impl(context):
    login(context)


@given(u'doy click en el botón de "Editar mi perfil"')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_id('btnMenu').click()
    context.driver.find_element_by_id('btnMiPerfil').click()


@when(u'modifico el número de teléfono: "{telefono}"')
def step_impl(context, telefono):
    time.sleep(2)
    context.driver.find_element_by_id('id_telefono').clear()
    context.driver.find_element_by_id('id_telefono').send_keys(telefono)


@when(u'presiono el botón de "Guardar cambios"')
def step_impl(context):
    context.driver.find_element_by_id('btnGuardarCambios').click()


@then(u'el sistema muestra el mensaje de "{mensaje}"')
def step_impl(context, mensaje):
    time.sleep(2)
    mensaje_exito = context.driver.find_element_by_id('mensaje').text
    context.test.assertEqual(mensaje, mensaje_exito)


@then(u'el sistema muestra el mensaje de error "{mensaje_error}"')
def step_impl(context, mensaje_error):
    time.sleep(2)
    listas = context.driver.find_elements_by_class_name('errorlist')
    errores = [li.find_elements_by_tag_name('li')[0].text for li in listas[1:]]
    context.test.assertIn(mensaje_error, errores)
