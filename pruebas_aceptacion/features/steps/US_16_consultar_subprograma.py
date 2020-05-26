from behave import given, when, then
import time
from environment import login


@given(u'que necesito saber si el subprograma "{subp}" '
       u'está activado')
def step_impl(context, subp):
    login(context)
    context.driver.get(context.urlBase + "subprograma/")
    rows = context.driver.find_elements_by_tag_name('tr')
    time.sleep(2)
    for row in rows[1:]:
        if row.find_elements_by_tag_name('td')[1].text == subp:
            context.btn_ver = row.\
                find_element_by_id('btn_detalles')
            break


@when(u'presione el botón "Ver" del subprograma')
def step_impl(context):
    context.btn_ver.click()


@then(
    u'el sistema muestra la información porgrama: "{nombre_prog}", '
    u'nombre: "{nombre_subp}", presupuesto "{presupuesto}"'
    u', responsable: "{responsable}", estatus "{estatus}"')
def step_impl(context, nombre_prog, nombre_subp, presupuesto,
              responsable, estatus):
    time.sleep(2)
    context.test.assertEqual(
        context.driver.find_element_by_id(
            'id_nombre').text, nombre_subp
    )
    context.test.assertEqual(
        context.driver.find_element_by_id(
            'id_programa').text, nombre_prog
    )
    context.test.assertEqual(
        context.driver.find_element_by_id(
            'id_presupuesto').text, presupuesto
    )
    context.test.assertEqual(
        context.driver.find_element_by_id(
            'id_responsable').text, responsable
    )
    context.test.assertEqual(
        context.driver.find_element_by_id(
            'id_estatus').text, estatus
    )
