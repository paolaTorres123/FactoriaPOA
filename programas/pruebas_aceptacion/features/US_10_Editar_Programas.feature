Característica: Edición de programas
    Como director operativo del sistema
    deseo poder editar los datos de los programas creados anteriormente  
    para tener actualizados los datos de los mismos y modificarlos en caso de existir cambios en la información.

    Escenario: Datos modificados correctamente programas
        Dado que inicio sesión en el sistema para ir a la sección de programas
        Y deseo modificar el programa "Emprendimiento Social"
        Y presiono el botón "Editar"
        Y que modifico el nombre del programa anterior por: "Emprendimiento Social Juvenil"
        Cuando presiono el botón de "Guardar cambios" en la edición
        Entonces el sistema permite ver el mensaje de "Programa modificado exitosamente." en edición.

    Escenario: Datos modificados incorrectamente
        Dado que inicio sesión en el sistema para ir a la sección de programas
        Y deseo modificar el programa "Emprendimiento Social"
        Y presiono el botón "Editar"
        Y que modifico el número de beneficiarios anterior por: "9000003"
        Cuando presiono el botón de "Guardar cambios" en la edición
        Entonces el sistema permite ver el mensaje de "El formato del número de beneficiario es incorrecto, debe ser indicado con un número".
