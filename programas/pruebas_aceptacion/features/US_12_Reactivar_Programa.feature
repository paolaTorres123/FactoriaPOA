Característica: Reactivación de programas
    Como director operativo del sistema
    deseo poder reactivar los programas existentes que se encuentran desactivados
    para poder volver a poner en marcha los programas en cuestión, reasignar los recursos y características a ellos.

    Escenario: Reactivación exitosa de Programa
        Dado que inicio sesión en el sistema como Director operativo
        Y deseo reactivar un programa y selecciono uno de los programas que se encuentra suspendido como "Cultura Emprendedora"
        Cuando presiono el botón de "Reactivar programa"
        Entonces el sistema muestra el mensaje "Programa seleccionado reactivado con éxito".

    Escenario: Programa que ya se encuentra activado
        Dado que inicio sesión en el sistema como Director operativo
        Cuando deseo reactivar un programa y selecciono uno de los programas existentes como "Cultura Emprendedora"
        Entonces no puedo de encontrar el botón de "Reactivar" ya que el programa se encuentra reactivado
