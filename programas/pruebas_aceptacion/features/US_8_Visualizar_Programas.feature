Característica: Visualización de programas
    Como director operativo del sistema
    deseo poder visualizar los programas existentes
    para poder ver la información de dichos programas y poder trabajar sobre ellos

    Escenario: Selección de programa existente
        Dado que el director operativo se encuentra logueado en el sistema
        Cuando presione el botón hacia la lista de programas
        Entonces el director puede ver el programa "Cultura Emprendedora" en la lista.

    Escenario: Selección de programa no existente
        Dado que el director operativo se encuentra logueado en el sistema
        Cuando presione el botón hacia la lista de programas
        Entonces el director no puede ver el programa "Cultura Emprendedora Juvenil" en la lista.