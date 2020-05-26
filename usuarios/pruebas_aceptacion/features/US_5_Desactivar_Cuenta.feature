Característica: Desactivar cuenta
    Como director operativo
    deseo poder desactivar la cuenta de usuario de un encargado de subprograma
    para que ya no le sea posible ingresar al sistema.

    Escenario: Desactivación exitosa
        Dado que inicio sesión en el sistema como Director operativo
        Y me dirijo a la lista de usuarios
        Cuando encuentro el usuario "cultEmprendedora" y presiono el botón de Desactivar cuenta
        Entonces el sistema muestra el mensaje "Cuenta desactivada con éxito." indicando que la desactivación fue exitosa.

    Escenario: Cuenta ya activada
        Dado que inicio sesión en el sistema como Director operativo
        Y me dirijo a la lista de usuarios
        Cuando encuentro el usuario "cultEmprendedora"
        Entonces no puedo encontrar el botón de "Desactivar" ya que la cuenta se encuentra desactivada.