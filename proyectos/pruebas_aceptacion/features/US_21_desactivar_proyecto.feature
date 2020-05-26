Característica: Desactivar Proyecto
    Como director operativo
    quiero desactivar el proyecto
    para realizar otros de mayor prioridad.


    Escenario: Proyecto desactivado exitosamente
        Dado que deseo desactivar el proyecto "Emprendiminto"
        Cuando presiono el botón “Desactivar”
        Entonces te redirije a la lista de los proyectos, donde ya aparecera el proyecto desactivado.

    Escenario: Error al desactivar el proyecto
        Dado que deseo desactivar el proyecto "Empredimiento"
        Cuando intente encontrar el botón "Desactivar"
        Entonces no encuentra el botón "Desactivar" ya que ya esta desactivado, vuelve a cargar la lista.