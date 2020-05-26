from behave import given, when, then


@given(u'que ingreso los datos correctos como; nombre del programa:'
       + ' "{nombre_programa}"; Año del ejercicio fiscal: "{anio_fiscal}";'
       + ' Recurso Asignado: "{recurso_asignado}"; Fuente: "{fuente}"; '
       + 'Status: "{status}"; Partida Presupuestal y Monto: [numero:'
       + ' "{numero_partida_presupuestal}", nombre:'
       + ' "{nombre_partida_presupuestal}", '
       + 'monto:"{monto_partida_presupuestal}"]; Tipo Apoyo: "{tipo_apoyo}";'
       + ' Número de actividades: "{numero_actividades}"; Beneficiarios:'
       + ' "{numero_beneficiarios}"; Hombres: "{numero_hombres}"; Mujeres:'
       + ' "{numero_mujeres}"; Rango edad: "{rango_edad}"; Número de'
       + ' actividades: "{numero_actividades_mr}"; Beneficiarios:'
       + ' "{numero_beneficiarios_mr}"; Hombres: "{numero_hombres_mr}";'
       + ' Mujeres: "{numero_mujeres_mr}"; Rango edad: "{rango_edad_mr}";'
       + ' Tipo Programa: "{tipo_programa}"')
def step_impl(context, nombre_programa, anio_fiscal, recurso_asignado,
              fuente, status, numero_partida_presupuestal,
              nombre_partida_presupuestal, monto_partida_presupuestal,
              tipo_apoyo, numero_actividades, numero_beneficiarios,
              numero_hombres, numero_mujeres, rango_edad,
              numero_actividades_mr, numero_beneficiarios_mr,
              numero_hombres_mr, numero_mujeres_mr, rango_edad_mr,
              tipo_programa):
    # Página a donde debo de acceder
    context.driver.get(context.url+'programa/nuevo')
    context.driver.find_element_by_id('id_nombre').send_keys(nombre_programa)
    context.driver.find_element_by_id('id_anio_ejercicio_fiscal').clear()
    context.driver.find_element_by_id(
        'id_anio_ejercicio_fiscal').send_keys(anio_fiscal)
    context.driver.find_element_by_id('id_recurso_asignado').clear()
    context.driver.find_element_by_id(
        'id_recurso_asignado').send_keys(recurso_asignado)
    context.driver.find_element_by_id('id_fuente').send_keys(fuente)
    context.driver.find_element_by_id('id_tipo').send_keys(tipo_apoyo)
    context.driver.find_element_by_id('id_status').send_keys(status)
    # context.driver.find_element_by_id('id_partida_presupuestal').send_keys(nombre_partida_presupuestal)
    context.driver.find_element_by_id('id_numero_actividades_mp').clear()
    context.driver.find_element_by_id('id_numero_beneficiarios_mp').clear()
    context.driver.find_element_by_id('id_numero_hombres_mp').clear()
    context.driver.find_element_by_id('id_numero_mujeres_mp').clear()
    context.driver.find_element_by_id(
        'id_numero_actividades_mp').send_keys(numero_actividades)
    context.driver.find_element_by_id(
        'id_numero_beneficiarios_mp').send_keys(numero_beneficiarios)
    context.driver.find_element_by_id(
        'id_numero_hombres_mp').send_keys(numero_hombres)
    context.driver.find_element_by_id(
        'id_numero_mujeres_mp').send_keys(numero_mujeres)
    # context.driver.find_element_by_id('id_edad_mp').clear()
    context.driver.find_element_by_id('id_edad_mp').send_keys(rango_edad)
    context.driver.find_element_by_id('id_numero_actividades_r_mr').clear()
    context.driver.find_element_by_id('id_numero_beneficiarios_r_mr').clear()
    context.driver.find_element_by_id(
        'id_numero_actividades_r_mr').send_keys(numero_actividades_mr)
    context.driver.find_element_by_id(
        'id_numero_beneficiarios_r_mr').send_keys(numero_beneficiarios_mr)
    context.driver.find_element_by_id('id_numero_hombres_r_mr').clear()
    context.driver.find_element_by_id(
        'id_numero_hombres_r_mr').send_keys(numero_hombres_mr)
    context.driver.find_element_by_id('id_numero_mujeres_r_mr').clear()
    context.driver.find_element_by_id(
        'id_numero_mujeres_r_mr').send_keys(numero_mujeres_mr)
    # context.driver.find_element_by_id('id_edad_mr').clear()
    context.driver.find_element_by_id('id_edad_r_mr').send_keys(rango_edad_mr)
    context.driver.find_element_by_id(
        'id_tipo_programa_p').send_keys(tipo_programa)
    context.driver.find_element_by_id(
        'id_nombre_partida').send_keys(nombre_partida_presupuestal)
    context.driver.find_element_by_id('id_numero_partida').clear()
    context.driver.find_element_by_id(
        'id_numero_partida').send_keys(numero_partida_presupuestal)
    context.driver.find_element_by_id('id_monto_partida').clear()
    context.driver.find_element_by_id(
        'id_monto_partida').send_keys(monto_partida_presupuestal)
    print('FUNCIONA')


@when(u'presiono el botón "Crear Programa"')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-primary').click()
    # pass


@then(u'el sistema permite ver el siguiente mensaje "{mensaje_exito}".')
def step_impl(context, mensaje_exito):
    context.test.assertIn(mensaje_exito, context.driver.page_source)


@given(u'que ingreso los datos incorrectos como; nombre del programa:'
       + ' "{nombre_programa}"; Año del ejercicio fiscal: "{anio_fiscal}";'
       + ' Recurso Asignado: "{recurso_asignado}"; Fuente: "{fuente}";'
       + ' Status: "{status}"; Partida Presupuestal y Monto: [numero:'
       + ' "{numero_partida_presupuestal}", nombre:'
       + ' "{nombre_partida_presupuestal}",'
       + ' monto:"{monto_partida_presupuestal}"]; Tipo Apoyo:'
       + ' "{tipo_apoyo}"; Número de actividades: "{numero_actividades}";'
       + ' Beneficiarios: "{numero_beneficiarios}"; Hombres:'
       + ' "{numero_hombres}"; Mujeres: "{numero_mujeres}"; Rango edad:'
       + ' "{rango_edad}"; Número de actividades: "{numero_actividades_mr}";'
       + ' Beneficiarios: "{numero_beneficiarios_mr}"; Hombres:'
       + ' "{numero_hombres_mr}"; Mujeres: "{numero_mujeres_mr}"; Rango edad:'
       + ' "{rango_edad_mr}"; Tipo Programa: "{tipo_programa}"')
def step_impl(context, nombre_programa, anio_fiscal, recurso_asignado,
              fuente, status, numero_partida_presupuestal,
              nombre_partida_presupuestal, monto_partida_presupuestal,
              tipo_apoyo, numero_actividades, numero_beneficiarios,
              numero_hombres, numero_mujeres, rango_edad,
              numero_actividades_mr, numero_beneficiarios_mr,
              numero_hombres_mr, numero_mujeres_mr, rango_edad_mr,
              tipo_programa):
    context.driver.get(context.url+'programa/nuevo')
    context.driver.find_element_by_id('id_nombre').send_keys(nombre_programa)
    context.driver.find_element_by_id('id_anio_ejercicio_fiscal').clear()
    context.driver.find_element_by_id(
        'id_anio_ejercicio_fiscal').send_keys(anio_fiscal)
    context.driver.find_element_by_id('id_recurso_asignado').clear()
    context.driver.find_element_by_id(
        'id_recurso_asignado').send_keys(recurso_asignado)
    context.driver.find_element_by_id('id_fuente').send_keys(fuente)
    context.driver.find_element_by_id('id_tipo').send_keys(tipo_apoyo)
    context.driver.find_element_by_id('id_status').send_keys(status)
    # context.driver.find_element_by_id('id_partida_presupuestal').send_keys(nombre_partida_presupuestal)
    context.driver.find_element_by_id('id_numero_actividades_mp').clear()
    context.driver.find_element_by_id('id_numero_beneficiarios_mp').clear()
    context.driver.find_element_by_id('id_numero_hombres_mp').clear()
    context.driver.find_element_by_id('id_numero_mujeres_mp').clear()
    context.driver.find_element_by_id(
        'id_numero_actividades_mp').send_keys(numero_actividades)
    context.driver.find_element_by_id(
        'id_numero_beneficiarios_mp').send_keys(numero_beneficiarios)
    context.driver.find_element_by_id(
        'id_numero_hombres_mp').send_keys(numero_hombres)
    context.driver.find_element_by_id(
        'id_numero_mujeres_mp').send_keys(numero_mujeres)
    # context.driver.find_element_by_id('id_edad_mp').clear()
    context.driver.find_element_by_id('id_edad_mp').send_keys(rango_edad)
    context.driver.find_element_by_id('id_numero_actividades_r_mr').clear()
    context.driver.find_element_by_id('id_numero_beneficiarios_r_mr').clear()
    context.driver.find_element_by_id(
        'id_numero_actividades_r_mr').send_keys(numero_actividades_mr)
    context.driver.find_element_by_id(
        'id_numero_beneficiarios_r_mr').send_keys(numero_beneficiarios_mr)
    context.driver.find_element_by_id('id_numero_hombres_r_mr').clear()
    context.driver.find_element_by_id(
        'id_numero_hombres_r_mr').send_keys(numero_hombres_mr)
    context.driver.find_element_by_id('id_numero_mujeres_r_mr').clear()
    context.driver.find_element_by_id(
        'id_numero_mujeres_r_mr').send_keys(numero_mujeres_mr)
    # context.driver.find_element_by_id('id_edad_mr').clear()
    context.driver.find_element_by_id('id_edad_r_mr').send_keys(rango_edad_mr)
    context.driver.find_element_by_id(
        'id_tipo_programa_p').send_keys(tipo_programa)
    context.driver.find_element_by_id(
        'id_nombre_partida').send_keys(nombre_partida_presupuestal)
    context.driver.find_element_by_id('id_numero_partida').clear()
    context.driver.find_element_by_id(
        'id_numero_partida').send_keys(numero_partida_presupuestal)
    context.driver.find_element_by_id('id_monto_partida').clear()
    context.driver.find_element_by_id(
        'id_monto_partida').send_keys(monto_partida_presupuestal)

    print('FUNCIONA 2')


@then(u'el sistema permite ver el mensaje siguiente "{mensaje_error}".')
def step_impl(context, mensaje_error):
    context.test.assertIn(mensaje_error, context.driver.page_source)
    # pass


@given(u'que ingreso los datos como; nombre del programa:'
       + ' "{nombre_programa}"; Año del ejercicio fiscal:'
       + ' "{anio_fiscal}"; Recurso Asignado: "{recurso_asignado}";'
       + ' Fuente: "{fuente}"; Status: "{status}"; Partida Presupuestal'
       + ' y Monto: [numero: "{numero_partida_presupuestal}", nombre:'
       + ' "{nombre_partida_presupuestal}",'
       + ' monto:"{monto_partida_presupuestal}"]; Tipo Apoyo: "{tipo_apoyo}";'
       + ' Número de actividades: "{numero_actividades}"; Beneficiarios:'
       + ' "{numero_beneficiarios}"; Hombres: "{numero_hombres}"; Mujeres:'
       + ' "{numero_mujeres}"; Rango edad: "{rango_edad}"; Número de'
       + ' actividades: "{numero_actividades_mr}"; Beneficiarios:'
       + ' "{numero_beneficiarios_mr}"; Hombres: "{numero_hombres_mr}";'
       + ' Mujeres: "{numero_mujeres_mr}"; Rango edad: "{rango_edad_mr}";'
       + ' Tipo Programa: "{tipo_programa}"')
def step_impl(context, nombre_programa, anio_fiscal, recurso_asignado, fuente,
              status, numero_partida_presupuestal,
              nombre_partida_presupuestal,
              monto_partida_presupuestal, tipo_apoyo, numero_actividades,
              numero_beneficiarios, numero_hombres, numero_mujeres,
              rango_edad, numero_actividades_mr, numero_beneficiarios_mr,
              numero_hombres_mr, numero_mujeres_mr, rango_edad_mr,
              tipo_programa):
    context.driver.get(context.url+'programa/nuevo')
    context.driver.find_element_by_id('id_nombre').send_keys(nombre_programa)
    context.driver.find_element_by_id('id_anio_ejercicio_fiscal').clear()
    context.driver.find_element_by_id(
        'id_anio_ejercicio_fiscal').send_keys(anio_fiscal)
    context.driver.find_element_by_id('id_recurso_asignado').clear()
    context.driver.find_element_by_id(
        'id_recurso_asignado').send_keys(recurso_asignado)
    context.driver.find_element_by_id('id_fuente').send_keys(fuente)
    context.driver.find_element_by_id('id_tipo').send_keys(tipo_apoyo)
    context.driver.find_element_by_id('id_status').send_keys(status)
    # context.driver.find_element_by_id('id_partida_presupuestal').send_keys(nombre_partida_presupuestal)
    context.driver.find_element_by_id('id_numero_actividades_mp').clear()
    context.driver.find_element_by_id('id_numero_beneficiarios_mp').clear()
    context.driver.find_element_by_id('id_numero_hombres_mp').clear()
    context.driver.find_element_by_id('id_numero_mujeres_mp').clear()
    context.driver.find_element_by_id(
        'id_numero_actividades_mp').send_keys(numero_actividades)
    context.driver.find_element_by_id(
        'id_numero_beneficiarios_mp').send_keys(numero_beneficiarios)
    context.driver.find_element_by_id(
        'id_numero_hombres_mp').send_keys(numero_hombres)
    context.driver.find_element_by_id(
        'id_numero_mujeres_mp').send_keys(numero_mujeres)
    # context.driver.find_element_by_id('id_edad_mp').clear()
    context.driver.find_element_by_id('id_edad_mp').send_keys(rango_edad)
    context.driver.find_element_by_id('id_numero_actividades_r_mr').clear()
    context.driver.find_element_by_id('id_numero_beneficiarios_r_mr').clear()
    context.driver.find_element_by_id(
        'id_numero_actividades_r_mr').send_keys(numero_actividades_mr)
    context.driver.find_element_by_id(
        'id_numero_beneficiarios_r_mr').send_keys(numero_beneficiarios_mr)
    context.driver.find_element_by_id('id_numero_hombres_r_mr').clear()
    context.driver.find_element_by_id(
        'id_numero_hombres_r_mr').send_keys(numero_hombres_mr)
    context.driver.find_element_by_id('id_numero_mujeres_r_mr').clear()
    context.driver.find_element_by_id(
        'id_numero_mujeres_r_mr').send_keys(numero_mujeres_mr)
    # context.driver.find_element_by_id('id_edad_mr').clear()
    context.driver.find_element_by_id('id_edad_r_mr').send_keys(rango_edad_mr)
    context.driver.find_element_by_id(
        'id_tipo_programa_p').send_keys(tipo_programa)
    context.driver.find_element_by_id(
        'id_nombre_partida').send_keys(nombre_partida_presupuestal)
    context.driver.find_element_by_id('id_numero_partida').clear()
    context.driver.find_element_by_id(
        'id_numero_partida').send_keys(numero_partida_presupuestal)
    context.driver.find_element_by_id('id_monto_partida').clear()
    context.driver.find_element_by_id(
        'id_monto_partida').send_keys(monto_partida_presupuestal)
    print('FUNCIONA 3')
    # pass


@then(u'puedo ver el mensaje "{mensaje_recurso_asignado_error}".')
def step_impl(context, mensaje_recurso_asignado_error):
    context.test.assertIn(mensaje_recurso_asignado_error,
                          context.driver.page_source)


@then(u'el sistema permite ver el mensaje "{mensaje_campos_error}".')
def step_impl(context, mensaje_campos_error):
    context.test.assertIn(mensaje_campos_error, context.driver.page_source)
