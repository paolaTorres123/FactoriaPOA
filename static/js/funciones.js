function crearCuentaModal(usuario) {
    var form = document.formulario;
    form.submit();

    document.getElementById('btnAceptar').href="/usuarios/";
    document.getElementById('pModal').innerHTML="Cuenta del usuario <strong>"+usuario+"</strong> creada con éxito.";
}

function cerrarSesion(url) {
    document.getElementById('btnCerrar').href=url;
    document.getElementById('modal').click();
    document.getElementById('texto').innerHTML="¿Estás seguro de que deseas cerrar la sesión?";
}