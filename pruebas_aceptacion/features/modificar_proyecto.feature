Característica: Modificar proyecto
    Como director operativo
    Deseo modificar el  nombre del proyecto
    Para poder nombrarlo de otra manera.


    Escenario: Proyecto modificado exitosamente
        Dado que quiero modificar el proyecto "Emprendimiento" por "Emprendimiento en llamas"
        Cuando presione el botón "Guardar cambios"
        Entonces te redirige a la lista de proyectos para que se vea el cambio.

    Escenario: Datos modificados incorrectos
        Dado que quiero modificar el "Emprendimineto" por "Er"
        Cuando presione el botón "Guardar cambios"
        Entonces se muestra el mensaje "Error de longitud mínima" el marca el error
        Y te redirige al formulario.