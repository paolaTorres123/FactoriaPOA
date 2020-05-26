Característica: Editar información de usuario
    Como director operativo
    deseo poder modificar la información de mi perfil de usuario 
    para tener mis datos actualizados.

    Escenario: Datos modificados correctamente
        Dado que inicio sesión en el sistema
        Y doy click en el botón de "Editar mi perfil"
        Cuando modifico el número de teléfono: "4921001234"
        Y presiono el botón de "Guardar cambios"
        Entonces el sistema muestra el mensaje de "Perfil de usuario modificado exitosamente."

    Escenario: Datos modificados incorrectamente
        Dado que inicio sesión en el sistema
        Y doy click en el botón de "Editar mi perfil"
        Cuando modifico el número de teléfono: "492100123"
        Cuando presiono el botón de "Guardar cambios"
        Entonces el sistema muestra el mensaje de error "El número telefónico debe contener 10 dígitos."