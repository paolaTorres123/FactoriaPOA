from behave import given, when, then
import time
from environment import login


@given(
    u'que ingreso los datos porgrama: "{nombre_programa}", '
    u'nombre: "{nombre_subprograma}", '
    u'presupuesto "{presupuesto}", '
    u'responsable: "{nombre_responsable}" '
    u'para crear un subprograma')
def step_impl(context, nombre_programa, nombre_subprograma,
              presupuesto, nombre_responsable):
    login(context)
    context.driver.get(
        context.urlBase + "subprograma/nuevo")
    context.driver.find_element_by_id("id_programa") \
        .send_keys(nombre_programa)
    context.driver.find_element_by_id("id_nombre") \
        .send_keys(nombre_subprograma)
    context.driver.find_element_by_id("id_presupuesto") \
        .send_keys(presupuesto)
    context.driver.find_element_by_id("id_responsable") \
        .send_keys(nombre_responsable)


@when(u'presione el botón "Guardar"')
def step_impl(context):
    context.driver.find_element_by_id("btn_guardar").click()


@then(u'el sistema manda un mensaje diciendo "{mensaje}".')
def step_impl(context, mensaje):
    time.sleep(3)
    mensaje_form = context.driver.find_element_by_id("mensaje").text
    context.test.assertEquals(mensaje_form, mensaje)


@then(u'el sistema manda un mensaje de error diciendo "{error}".')
def step_impl(context, error):
    time.sleep(3)
    mensajes_error_form = context.driver.find_elements_by_tag_name("li")
    mensajes = [mensaje.text for mensaje in mensajes_error_form]
    context.test.assertIn(error, mensajes)
