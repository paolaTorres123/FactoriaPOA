Característica: Listar usuarios
    Como director operativo 
    deseo poder ver una lista de los usuarios registrados en el sistema
    para poder gestionarlos.

    Escenario: Listado de usuarios exitoso
        Dado que inicio sesión en el sistema como Director operativo
        Cuando doy click en el botón del menú "Usuarios"
        Y doy click en el botón de "Usuarios registrados"
        Entonces puedo ver al usuario "cultEmprendedora" en la lista.

    Escenario: Usuario no se encuentra en la lista
        Dado que inicio sesión en el sistema como Director operativo
        Cuando doy click en el botón del menú "Usuarios"
        Y doy click en el botón de "Usuarios registrados"
        Entonces no puedo ver al usuario "ecosistemaE" en la lista.