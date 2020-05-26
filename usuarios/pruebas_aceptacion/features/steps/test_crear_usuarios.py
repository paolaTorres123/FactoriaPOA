from behave import given, when, then
import time
from environment import login

# Steps para Escenario 1 - Creación de cuenta: Datos correctos


@given(u'que ingreso a la sección del sistema para '
       + 'crear una cuenta de usuario')
def step_impl(context):
    login(context)
    time.sleep(2)
    context.driver.get(context.url+'usuarios/nuevo')


@given(u'completo los datos correctos como usuario: "{usuario}", correo '
       + 'electrónico: "{correo}" , contraseña: "{contrasena}", la '
       + 'confirmación de la contraseña: "{confirm_contrasena}", indico que'
       + ' es director operativo, nombre: "{nombre}", primer_apellido:'
       + ' "{primer_apellido}" y telefono: "{tel}"')
def step_impl(context, usuario, correo, contrasena, confirm_contrasena,
              nombre, primer_apellido, tel):
    time.sleep(2)
    context.driver.find_element_by_id('id_username').send_keys(usuario)
    context.driver.find_element_by_id('id_email').send_keys(correo)
    context.driver.find_element_by_id('id_password').send_keys(contrasena)
    context.driver.find_element_by_id(
        'id_password_re').send_keys(confirm_contrasena)
    context.driver.find_element_by_id('id_is_superuser').click()
    context.driver.find_element_by_id('id_nombre').send_keys(nombre)
    context.driver.find_element_by_id(
        'id_primer_apellido').send_keys(primer_apellido)
    context.driver.find_element_by_id('id_telefono').send_keys(tel)


@when(u'presiono el botón de "Crear cuenta"')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-success').click()


@then(u'el sistema muestra el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    time.sleep(5)
    mensaje_exito = context.driver.find_element_by_id('mensaje').text
    context.test.assertEqual(mensaje, mensaje_exito)


@then(u'puedo ver en la lista de usuarios al usuario "{usuario}" '
      + 'que acabo de crear.')
def step_impl(context, usuario):
    time.sleep(4)
    rows = context.driver.find_elements_by_tag_name('tr')
    usuarios = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]
    context.test.assertIn(usuario, usuarios)

# Steps para Escenarios 2 y 3 -
# Creación de cuenta: Correo electrónico duplicado


@then(u'el sistema muestra el mensaje de error: "{mensaje_error}"')
def step_impl(context, mensaje_error):
    listas = context.driver.find_elements_by_class_name('errorlist')
    errores = [li.find_elements_by_tag_name('li')[0].text for li in listas[1:]]
    context.test.assertIn(mensaje_error, errores)
