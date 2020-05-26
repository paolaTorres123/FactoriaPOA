Característica: Desactivar subprograma
    Como   encargado de subprograma
    Deseo  desactivar un subprograma
    Para   no tomarlo en cuenta ya que hubo un error y no se llevará acabo.


    Escenario: Subprograma desactivado exitosamente
        Dado que deseo modificar el subprograma "Subprograma ejemplito"
        Cuando  cambie el estatus a "Inactivo"
        Y presiono el botón "Guardar"
        Entonces se muestra un mensaje diciendo "Datos del subprograma modificados correctamente".