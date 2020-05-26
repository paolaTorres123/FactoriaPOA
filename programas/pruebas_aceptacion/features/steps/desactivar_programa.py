from behave import given, when, then
import time


@given(u'que deseo desactivar/suspender un programa y selecciono'
       + ' uno de los programas existentes como "{nombre_programa}"')
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


@when(u'presiono el botón de "Suspender programa"')
def step_impl(context):
    for programa in context.programas_g:
        if programa[1].text == context.nombre_programa:
            programa[6].find_element_by_class_name('btn-danger').click()
            break


@then(u'el sistema muestra el mensaje "{mensaje_suspension}" y el sistema '
      + 'libera los recursos vinculados con dicho programa.')
def step_impl(context, mensaje_suspension):
    time.sleep(2)
    mensaje_exito = context.driver.find_element_by_id('mensaje').text
    context.test.assertEqual(mensaje_suspension, mensaje_exito)


@when(u'deseo desactivar/suspender un programa y selecciono uno de los'
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


@when(u'intento presionar el botón de "Desactivar programa"')
def step_impl(context):
    for programa in context.programas_g:
        if programa[1].text == context.nombre_programa:
            programa[6].find_element_by_class_name('btn-primary').click()
            break


@then(u'no puedo de encontrar el botón de "{nombre_boton}" ya que el programa'
      + ' se encuentra desactivado')
def step_impl(context, nombre_boton):
    button = context.programas_g[1][6].find_element_by_tag_name('a').text
    context.test.assertNotEqual(button, nombre_boton)


@when(u'presiono el botón de "Desactivar programa"')
def step_impl(context):
    for programa in context.programas_g:
        if programa[1].text == context.nombre_programa:
            programa[6].find_element_by_class_name('btn-primary').click()
            break
