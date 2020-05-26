from behave import given, when, then
import time
from environment import login


@given(u'que selecciono el tipo de reporte '
       u'que deseo generar "{modelo_rep}"')
def step_impl(context, modelo_rep):
    login(context)
    context.driver.get(context.urlBase + "reportes/")
    time.sleep(3)
    context.driver.find_element_by_id("miSelect") \
        .send_keys(modelo_rep)


@when(u'presiono el botón de "Generar PDF"')
def step_impl(context):
    context.driver \
        .find_element_by_id("btn_genera_pdf").click()


@then(u'el sistema me muestra el reporte que '
      u'solicité de manera visual.')
def step_impl(context):
    pdf = context.driver \
        .find_element_by_tag_name("embed")
    context.test.assertIsNotNone(pdf)


@given(u'que deseo visualizar el reporte de "{tipo_reporte}"')
def step_impl(context, tipo_reporte):
    login(context)
    context.driver.get(context.urlBase + "reportes/")
    time.sleep(3)
    context.driver.find_element_by_id("miSelect") \
        .send_keys(tipo_reporte)


@then(u'el sistema me muestra el reporte seleccionado.')
def step_impl(context):
    pdf = context.driver \
        .find_element_by_tag_name("embed")
    context.test.assertIsNotNone(pdf)
