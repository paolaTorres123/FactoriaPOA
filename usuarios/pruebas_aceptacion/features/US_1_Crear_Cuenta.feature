Característica: Crear cuenta
    Como director operativo
    quiero poder crear una cuenta de usuario
    para poder ingresar al sistema.

    Escenario: Datos correctos
        Dado que ingreso a la sección del sistema para crear una cuenta de usuario
        Y completo los datos correctos como usuario: "dirOperativo", correo electrónico: "dir_operativa@factoria.com" , contraseña: "F@@ctoria12", la confirmación de la contraseña: "F@@ctoria12", indico que es director operativo, nombre: "Laura", primer_apellido: "Ruelas" y telefono: "4941056009"
        Cuando presiono el botón de "Crear cuenta"
        Entonces el sistema muestra el mensaje "Cuenta creada con éxito, el propietario de la cuenta debe verificar su correo electrónico para activar su cuenta."
        Y puedo ver en la lista de usuarios al usuario "dirOperativo" que acabo de crear.

    Escenario: Correo electrónico duplicado
        Dado que ingreso a la sección del sistema para crear una cuenta de usuario
        Y completo los datos correctos como usuario: "dirOperativoc", correo electrónico: "dir_operativa@factoria.com" , contraseña: "F@@ctoria12", la confirmación de la contraseña: "F@@ctoria12", indico que es director operativo, nombre: "Laura", primer_apellido: "Ruelas" y telefono: "4941056009"
        Cuando presiono el botón de "Crear cuenta"
        Entonces el sistema muestra el mensaje de error: "El correo electrónico ingresado ya se encuentra registrado en el sistema. Favor de verificarlo."

    Escenario: Usuario inválido
        Dado que ingreso a la sección del sistema para crear una cuenta de usuario
        Y completo los datos correctos como usuario: "dirOperativo", correo electrónico: "dir_operativa@factoria.com" , contraseña: "F@@ctoria12", la confirmación de la contraseña: "F@@ctoria12", indico que es director operativo, nombre: "Laura", primer_apellido: "Ruelas" y telefono: "4941056009"
        Cuando presiono el botón de "Crear cuenta"
        Entonces el sistema muestra el mensaje de error: "El usuario ingresado ya se encuentra registrado en el sistema, favor de verificarlo."

    Escenario: Nombre de usuario incorrecto
        Dado que ingreso a la sección del sistema para crear una cuenta de usuario
        Y completo los datos correctos como usuario: "dirOperativo1", correo electrónico: "dir_operativa@factoria.com" , contraseña: "F@@ctoria12", la confirmación de la contraseña: "F@@ctoria12", indico que es director operativo, nombre: "Laura", primer_apellido: "Ruelas" y telefono: "4941056009"
        Cuando presiono el botón de "Crear cuenta"
        Entonces el sistema muestra el mensaje de error "El nombre de usuario no sigue el formato solicitado, favor de verificarlo."

    Escenario: Contraseña inválida
        Dado que ingreso a la sección del sistema para crear una cuenta de usuario
        Y completo los datos correctos como usuario: "dirOperativo", correo electrónico: "dir_operativa@factoria.com" , contraseña: "factoria12", la confirmación de la contraseña: "F@@ctoria12", indico que es director operativo, nombre: "Laura", primer_apellido: "Ruelas" y telefono: "4941056009"
        Cuando presiono el botón de "Crear cuenta"
        Entonces el sistema muestra el mensaje de error "La contraseña no sigue el formato solicitado: 8 - 50 caracteres mínimo (una mayúscula, una minúscula, un número y un símbolo)."