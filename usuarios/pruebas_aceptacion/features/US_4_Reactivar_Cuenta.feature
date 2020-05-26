Característica: Reactivar cuenta
    Como director operativo
    deseo poder reactivar la cuenta de usuario de un encargado de subprograma
    para que le sea posible realizar sus actividades correspondientes.

    Escenario: Reactivación exitosa
        Dado que inicio sesión en el sistema como Director operativo
        Y me dirijo a la lista de usuarios
        Cuando encuentro el usuario "cultEmprendedora" y presiono el botón de "Reactivar cuenta"
        Entonces el sistema muestra el mensaje "Cuenta activada con éxito." indicando que la reactivación fue exitosa.

    Escenario: Cuenta ya activada
        Dado que inicio sesión en el sistema como Director operativo
        Y me dirijo a la lista de usuarios
        Cuando encuentro el usuario "cultEmprendedora"
        Entonces no puedo encontrar el botón de "Reactivar" ya que la cuenta se encuentra activada.