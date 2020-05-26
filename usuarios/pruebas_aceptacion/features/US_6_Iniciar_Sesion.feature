Característica: Iniciar sesión
    Como director operativo
    deseo poder iniciar sesión en el sistema
    para poder realizar mis actividades en él.

    Escenario: Credenciales correctas
        Dado que ingreso a la página de inicio de sesión
        Y completo mis datos, usuario: "dirOperativo" y la contraseña: "F@@ctoria12"
        Cuando presiono el botón de "Iniciar Sesión"
        Entonces puedo ver mi nombre de usuario: "dirOperativo" en la parte superior de la página.

    Escenario: Nombre de usuario incorrecto
        Dado que ingreso a la página de inicio de sesión
        Y completo mis datos, usuario: "dir_o" y la contraseña: "F@@ctoria12"
        Cuando presiono el botón de "Iniciar Sesión"
        Entonces el sistema muestra el mensaje: "El usuario o la contraseña son incorrectos, favor de intentarlo nuevamente.".

    Escenario: Contraseña incorrecta
        Dado que ingreso a la página de inicio de sesión
        Y completo mis datos, usuario: "dirOperativo" y la contraseña: "Factoria"
        Cuando presiono el botón de "Iniciar Sesión"
        Entonces el sistema muestra el mensaje: "El usuario o la contraseña son incorrectos, favor de intentarlo nuevamente.". 