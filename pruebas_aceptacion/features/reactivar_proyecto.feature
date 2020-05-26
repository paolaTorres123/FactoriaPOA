Característica: Reactivar Proyecto
    Como encargada de subprograma 
    quiero reactivar el proyecto
    para  poder realizar las actividades correspondientes.


    Escenario: Reactivación exitosa.
        Dado que deseo reactivar el proyecto "Emprendimiento"
        Cuando  presiono el botón “Activar”
        Entonces te redirije a la lista de los proyectos, donde ya aparecera el proyecto activado.

    Escenario: Error de reactivación del proyecto.
        Dado que deseo reactivar el proyecto "Emprendimiento"
        Cuando intente encontrar el botón “Activar”
        Entonces no se encuentra el botón "Activado" ya que el proyecto ya estaba activado, vuelve a cargar la lista.

