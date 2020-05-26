Característica: Desactivación de programas
    Como director operativo del sistema
    deseo poder desactivar los programas existentes
    para determinar si verdaderamente han cumplido su propósito y liberar los recursos y características asignados a ellos.

    Escenario: Desactivación/Suspensión exitosa
        Dado que inicio sesión en el sistema como Director operativo
        Y que deseo desactivar/suspender un programa y selecciono uno de los programas existentes como "Emprendimiento Social"
        Cuando presiono el botón de "Suspender programa"
        Entonces el sistema muestra el mensaje "Programa seleccionado se ha desactivado con éxito" y el sistema libera los recursos vinculados con dicho programa.

    Escenario: Programa que ya se encuentra desactivado/suspendido
        Dado que inicio sesión en el sistema como Director operativo
        Cuando deseo desactivar/suspender un programa y selecciono uno de los programas existentes como "Emprendimiento Social"
        Entonces no puedo de encontrar el botón de "Desactivar" ya que el programa se encuentra desactivado
