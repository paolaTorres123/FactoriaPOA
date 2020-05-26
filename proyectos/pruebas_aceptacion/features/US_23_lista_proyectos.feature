Característica: Ver proyecto
    Como director operativo
    quiero ver el proyecto
    para consultar los detalles.


    Escenario: Visualización del proyecto exitosa
        Dado que ingreso al sistema
        Cuando doy click en el botón de "Proyectos"
        Entonces se muestra la información del proyecto "Emprendimiento" en la lista.

    Escenario: Proyecto no se encuentra en la lista
        Dado que ingreso al sistema
        Cuando doy click en el botón de "Proyectos"
        Entonces no puedo ver al proyecto "Emprendedor" en la lista.