Característica: Dar de alta proyecto 
    Como encargado director operativo
    Deseo dar de alta un proyecto  
    Para asignarle los recursos necesarios.

    Escenario:Proyecto creado exitosa
        Dado que ingreso los datos correctos para crear un proyecto como; nombre proyecto: "Emprendimiento"; nombre_actividad: "Juegos"; unidad de medida: "Congresos"; cantidad "3"; saldo: "120000"
        Cuando presione el botón  "Crear proyecto"
        Entonces puedo ver el proyecto "Emprendimiento" en la lista de proyectos.

    Escenario: No es posible crear el proyecto por campos incompletos
        Dado que ingreso los datos incorrectos para crear un proyecto como; nombre proyecto: "!@#$12455"; nombre_actividad: "Juegos"; unidad de medida: "Congresos"; cantidad "3"; saldo: "120000"
        Cuando presiono el botón "Crear proyecto"
        Entonces el sistema manda un mensaje diciendo "Formato sólo se aceptan letras :"