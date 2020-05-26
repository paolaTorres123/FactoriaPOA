from behave import given, when, then
import time
from environment import login


@given(u'que el director operativo se encuentra logueado en el sistema')
def step_impl(context):
    # pass
    login(context)
    # context.driver.get(context.url+'programa')


@when(u'presione el botón hacia la lista de programas')
def step_impl(context):
    time.sleep(1)
    context.driver.find_elements_by_id('btnProgramas')[1].click()
    time.sleep(1)
    context.driver.find_elements_by_id('btnListaProgramas')[1].click()


@then(u'el director puede ver el programa "{nombre_programa}" en la lista.')
def step_impl(context, nombre_programa):
    time.sleep(2)
    rows = context.driver.find_elements_by_tag_name('tr')
    programas = []
    for row in rows[1:]:
        td_programa = row.find_elements_by_tag_name('td')
        programas.append(td_programa[1].text)
    context.test.assertIn(nombre_programa, programas)


@then(u'el director no puede ver el programa "{nombre_programa}" en la lista.')
def step_impl(context, nombre_programa):
    time.sleep(2)
    rows = context.driver.find_elements_by_tag_name('tr')
    programas = []
    for row in rows[1:]:
        td_programa = row.find_elements_by_tag_name('td')
        programas.append(td_programa[1].text)
    context.test.assertNotIn(nombre_programa, programas)
