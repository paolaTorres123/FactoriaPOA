Característica: Creación de programas
    Como director operativo del sistema
    deseo poder agregar nuevos programas junto con su año fiscal y características generales
    para poder administrar sus recursos, subprogramas, proyectos, actividades, metas, etc. 

    Escenario: Datos en formato correcto
        Dado que ingreso los datos correctos como; nombre del programa: "Emprendimiento Social"; Año del ejercicio fiscal: "2019"; Recurso Asignado: "1000000.00"; Fuente: "Estatal"; Status: "Activo"; Partida Presupuestal y Monto: [numero: "3000", nombre: "servicios", monto:"500000.00"]; Tipo Apoyo: "Trimestral"; Número de actividades: "4"; Beneficiarios: "500"; Hombres: "250"; Mujeres: "250"; Rango edad: "Jóvenes (18 a 29 años)"; Número de actividades: "4"; Beneficiarios: "1500"; Hombres: "250"; Mujeres: "999"; Rango edad: "Jóvenes (18 a 29 años)"; Tipo Programa: "Apoyo"   
        Cuando presiono el botón "Crear Programa" 
        Entonces el sistema permite ver el siguiente mensaje "Programa creado con éxito".

    Escenario: Año de ejercicio fiscal en formato incorrecto
        Dado que ingreso los datos incorrectos como; nombre del programa: "Emprendimiento Social"; Año del ejercicio fiscal: "500008"; Recurso Asignado: "1000000.00"; Fuente: "Estatal"; Status: "Activo"; Partida Presupuestal y Monto: [numero: "3000", nombre: "servicios", monto:"500000.00"]; Tipo Apoyo: "Trimestral"; Número de actividades: "4"; Beneficiarios: "500"; Hombres: "250"; Mujeres: "250"; Rango edad: "Jóvenes (18 a 29 años)"; Número de actividades: "4"; Beneficiarios: "7500"; Hombres: "250"; Mujeres: "250"; Rango edad: "Jóvenes (18 a 29 años)"; Tipo Programa: "Apoyo"  
        Cuando presiono el botón "Crear Programa" 
        Entonces el sistema permite ver el mensaje siguiente "El formato del año fiscal es incorrecto, debe ser indicado con un número de 4 dígitos".

    Escenario: Recurso asignado en formato incorrecto
        Dado que ingreso los datos como; nombre del programa: "Emprendimiento Social"; Año del ejercicio fiscal: "2019"; Recurso Asignado: "7999999999.99"; Fuente: "Estatal"; Status: "Activo"; Partida Presupuestal y Monto: [numero: "3000", nombre: "servicios", monto:"500000.00"]; Tipo Apoyo: "Trimestral"; Número de actividades: "4"; Beneficiarios: "500"; Hombres: "250"; Mujeres: "250"; Rango edad: "Jóvenes (18 a 29 años)"; Número de actividades: "4"; Beneficiarios: "500"; Hombres: "250"; Mujeres: "250"; Rango edad: "Jóvenes (18 a 29 años)"; Tipo Programa: "Apoyo"
        Cuando presiono el botón "Crear Programa" 
        Entonces puedo ver el mensaje "El formato del recurso asignado es incorrecto, debe ser indicado con un número (indicando la cantidad)".

    Escenario: Número de actividades en formato incorrecto
        Dado que ingreso los datos como; nombre del programa: "Emprendimiento Social"; Año del ejercicio fiscal: "2019"; Recurso Asignado: "2000000.00"; Fuente: "Estatal"; Status: "Activo"; Partida Presupuestal y Monto: [numero: "3000", nombre: "servicios", monto:"500000.00"]; Tipo Apoyo: "Trimestral"; Número de actividades: "909"; Beneficiarios: "500"; Hombres: "250"; Mujeres: "250"; Rango edad: "Jóvenes (18 a 29 años)"; Número de actividades: "4"; Beneficiarios: "500"; Hombres: "250"; Mujeres: "250"; Rango edad: "Jóvenes (18 a 29 años)"; Tipo Programa: "Apoyo"   
        Cuando presiono el botón "Crear Programa" 
        Entonces el sistema permite ver el mensaje "El formato del número de actividades es incorrecto, debe ser indicado con un número".

    Escenario: Número de beneficiarios en formato incorrecto 
        Dado que ingreso los datos como; nombre del programa: "Emprendimiento Social"; Año del ejercicio fiscal: "2019"; Recurso Asignado: "2000000.00"; Fuente: "Estatal"; Status: "Activo"; Partida Presupuestal y Monto: [numero: "3000", nombre: "servicios", monto:"500000.00"]; Tipo Apoyo: "Trimestral"; Número de actividades: "6"; Beneficiarios: "9999999"; Hombres: "250"; Mujeres: "250"; Rango edad: "Jóvenes (18 a 29 años)"; Número de actividades: "4"; Beneficiarios: "500"; Hombres: "250"; Mujeres: "250"; Rango edad: "Jóvenes (18 a 29 años)"; Tipo Programa: "Apoyo"
        Cuando presiono el botón "Crear Programa" 
        Entonces el sistema permite ver el mensaje "El formato del número de beneficiario es incorrecto, debe ser indicado con un número".
