Característica: Cerrar sesión
    Como director operativo 
    deseo poder cerrar mi sesión en el sistema 
    Para tener más seguridad por si alguien utiliza mi computadora después de mí.

    Escenario: Cierre de sesión exitoso
        Dado que inicié sesión en el sistema y deseo cerrar mi sesión
        Cuando presiono el botón de "Cerrar Sesión"
        Entonces el sistema pregunta lo siguiente: "¿Estás seguro de que deseas cerrar la sesión?", al confirmar, la sesión es cerrada
        Y me redirije a la pégina de Inicio de Sesión

    Escenario: Cierre de sesión cancelado
        Dado que inicié sesión en el sistema y deseo cerrar mi sesión
        Cuando presiono el botón de "Cerrar Sesión"
        Entonces el sistema pregunta lo siguiente: "¿Estás seguro de que deseas cerrar la sesión?", al no confirmar la operación, la sesión no es cerrada
        Y puedo seguir viendo mi nombre de usuario: "directorOperativo" en la parte superior de la pantalla.
