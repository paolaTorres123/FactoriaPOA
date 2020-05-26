Característica: Modificar información subprograma
    Como encargado de subprograma 
    deseo modificar el programa seleccionado 
    para cambiar el año fiscal ya que hubo un error.

    Escenario: Subprograma modificado correctamente
        Dado que deseo modificar el subprograma "Subprograma ejemplito"
        Cuando cambio los datos porgrama: "ejemplo - 2019", nombre: "SUBPROGRAMA GRANDE", presupuesto "4466", responsable: "sir_m"
        Y presiono el botón "Guardar"
        Entonces se muestra un mensaje diciendo "Datos del subprograma modificados correctamente".

    Escenario: Datos modificados incorrectamente
        Dado que deseo modificar el subprograma "SUBPROGRAMA GRANDE"
        Cuando cambio los datos nombre: "subp", presupuesto "-1"
        Y presiono el botón "Guardar"
        Entonces se muestran los errores "El nombre debe ser de por lo menos 5 caracteres.","No puede tener valores negativos" y te marca donde fueron los errores.