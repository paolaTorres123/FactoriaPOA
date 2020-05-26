Característica: Alta subprograma
    Como director del programa
    deseo dar de alta un subprograma
    Para poder asignarle un presupuesto.

    Escenario: Subprograma agregado exitosamente
        Dado que ingreso los datos porgrama: "Programa ejemplo", nombre: "Subprograma ejemplito", presupuesto "77770", responsable: "sirMario" para crear un subprograma
        Cuando presione el botón "Guardar"
        Entonces el sistema manda un mensaje diciendo "Subprograma agregado exitosamente".

    Escenario: Error en la creación de subprograma
        Dado que ingreso los datos porgrama: "ejemplo - 2019", nombre: "Sub", presupuesto "77770", responsable: "sir_m" para crear un subprograma
        Cuando presione el botón "Guardar"
        Entonces el sistema manda un mensaje de error diciendo "El nombre debe ser de por lo menos 5 caracteres.".