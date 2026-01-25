function mostrarRegistro() {
    document.getElementById('login-view').classList.add('hidden');
    document.getElementById('registro-view').classList.remove('hidden');
}

function mostrarLogin() {
    document.getElementById('registro-view').classList.add('hidden');
    document.getElementById('login-view').classList.remove('hidden');
}
function mostarInicio(){
    window.location.href = "/frontend/inicio.html";
}


// Aquí podrías luego capturar los datos del form
document.getElementById('form_login').onsubmit = (e) => {
    e.preventDefault();
    console.log("Intentando entrar...");
};