from behave import given, when, then
import time
from environment import login


@given(u'que deseo modificar el subprograma "{nombre_subp}"')
def step_impl(context, nombre_subp):
    login(context)
    context.driver.get(context.urlBase + "subprograma/")
    time.sleep(3)
    rows = context.driver.find_elements_by_tag_name('tr')
    for row in rows[1:]:
        r = row.find_elements_by_tag_name('td')
        id = r[0].text
        nombre = r[1].text
        if nombre == nombre_subp:
            context.driver.get(
                context.urlBase + f"subprograma/editar/{id}"
            )
            break


@when(u'cambio los datos porgrama: "{nombre_prog}", '
      u'nombre: "{nombre_subp}", '
      u'presupuesto "{presupuesto}", '
      u'responsable: "{responsable}"')
def step_impl(context, nombre_prog,
              nombre_subp, presupuesto,
              responsable):
    time.sleep(5)
    context.driver.find_element_by_id("id_programa") \
        .send_keys(nombre_prog)

    subp_nom = context.driver \
        .find_element_by_id("id_nombre")
    subp_nom.clear()
    subp_nom.send_keys(nombre_subp)

    subp_pre = context.driver \
        .find_element_by_id("id_presupuesto")
    subp_pre.clear()
    subp_pre.send_keys(presupuesto)

    context.driver.find_element_by_id("id_responsable") \
        .send_keys(responsable)


@when(u'presiono el botón "Guardar"')
def step_impl(context):
    context.driver.find_element_by_id("btn_guardar").click()


@then(u'se muestra un mensaje diciendo "{mensaje_exito}".')
def step_impl(context, mensaje_exito):
    time.sleep(2)
    mensaje_form = context.driver. \
        find_element_by_id("mensaje").text
    context.test.assertEquals(mensaje_form, mensaje_exito)


@when(u'cambio los datos nombre: "{nom}", '
      u'presupuesto "{pres}"')
def step_impl(context, nom, pres):
    time.sleep(2)
    subp_nom = context.driver. \
        find_element_by_id("id_nombre")
    subp_nom.clear()
    subp_nom.send_keys(nom)

    subp_pre = context.driver. \
        find_element_by_id("id_presupuesto")
    subp_pre.clear()
    subp_pre.send_keys(pres)


@then(u'se muestran los errores "{mensaje_1}","{mensaje_2}" '
      u'y te marca donde fueron los errores.')
def step_impl(context, mensaje_1, mensaje_2):
    time.sleep(2)
    mensajes_error_form = context.driver.find_elements_by_tag_name("li")
    mensajes = [mensaje.text for mensaje in mensajes_error_form]
    context.test.assertIn(mensaje_1, mensajes)
    context.test.assertIn(mensaje_2, mensajes)


# -----------------------DESACTIVAR/ACTIVAR
@when(u'cambie el estatus a "{estatus}"')
def step_impl(context, estatus):
    time.sleep(2)
    context.driver.find_element_by_id("id_estatus") \
        .send_keys(estatus)
