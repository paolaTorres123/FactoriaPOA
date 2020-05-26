from behave import given, when, then
import time


@given(u'deseo reactivar un programa y selecciono uno de los programas'
       + ' que se encuentra suspendido como "{nombre_programa}"')
def step_impl(context, nombre_programa):
    context.nombre_programa = nombre_programa
    time.sleep(1)
    context.driver.find_elements_by_id('btnProgramas')[1].click()
    time.sleep(1)
    context.driver.find_elements_by_id('btnListaProgramas')[1].click()
    time.sleep(3)
    rows = context.driver.find_elements_by_tag_name('tr')
    programas = []
    programas_g = []
    for row in rows[1:]:
        td_programa = row.find_elements_by_tag_name('td')
        programas.append(td_programa[1].text)
        programas_g.append(td_programa)
    context.programas_g = programas_g
    context.test.assertIn(nombre_programa, programas)


@when(u'presiono el botón de "Reactivar programa"')
def step_impl(context):
    for programa in context.programas_g:
        if programa[1].text == context.nombre_programa:
            programa[6].find_element_by_class_name('btn-primary').click()
            break


@then(u'el sistema muestra el mensaje "{mensaje_reactivacion}".')
def step_impl(context, mensaje_reactivacion):
    time.sleep(2)
    mensaje_exito = context.driver.find_element_by_id('mensaje').text
    context.test.assertEqual(mensaje_reactivacion, mensaje_exito)


@when(u'deseo reactivar un programa y selecciono uno de los'
      + ' programas existentes como "{nombre_programa}"')
def step_impl(context, nombre_programa):
    context.nombre_programa = nombre_programa
    time.sleep(1)
    context.driver.find_elements_by_id('btnProgramas')[1].click()
    time.sleep(1)
    context.driver.find_elements_by_id('btnListaProgramas')[1].click()
    time.sleep(3)
    rows = context.driver.find_elements_by_tag_name('tr')
    programas = []
    programas_g = []
    for row in rows[1:]:
        td_programa = row.find_elements_by_tag_name('td')
        programas.append(td_programa[1].text)
        programas_g.append(td_programa)
    context.programas_g = programas_g
    context.test.assertIn(nombre_programa, programas)


@then(u'no puedo de encontrar el botón de "{nombre_boton}" ya que'
      + ' el programa se encuentra reactivado')
def step_impl(context, nombre_boton):
    button = context.programas_g[1][6].find_element_by_tag_name('a').text
    context.test.assertNotEqual(button, nombre_boton)
