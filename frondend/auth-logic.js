/**
 * auth_logic.js - Capa de Presentación (Lógica de Cliente)
 * Este script gestiona la captura, limpieza y envío de datos al backend.
 */

// Configuración del servidor - usar URL relativa
const API_URL = "";  // URL vacía = mismo servidor y puerto

/**
 * Sanitiza los inputs para evitar inyecciones básicas de scripts (XSS)
 */
function limpiarInput(texto) {
    const div = document.createElement('div');
    div.textContent = texto;
    return div.innerHTML;
}

/**
 * Gestión del Inicio de Sesión
 */
async function handleLogin() {
    const userRaw = document.getElementById('user').value;
    const passRaw = document.getElementById('pass').value;

    // Validación básica de campos vacíos
    if (!userRaw || !passRaw) {
        alert("Por favor, completa todos los campos.");
        return;
    }

    const payload = {
        username: limpiarInput(userRaw),
        password: passRaw // La contraseña se envía plana pero debe viajar por HTTPS
    };

    try {
        const response = await fetch(`${API_URL}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        if (response.ok) {
            alert("Acceso concedido. Redirigiendo...");
            // Aquí manejarías el token de sesión o redirección
            window.location.href = "/static/inicio.html";
        } else {
            alert(`Error: ${result.detail || "Credenciales incorrectas"}`);
        }
    } catch (error) {
        console.error("Error de conexión:", error);
        alert("No se pudo conectar con el servidor de seguridad.");
    }
}

/**
 * Gestión del Registro de Usuarios
 */
async function handleRegister() {
    const userRaw = document.getElementById('reg-user').value;
    const passRaw = document.getElementById('reg-pass').value;
    const confirmRaw = document.getElementById('reg-pass-confirm').value;

    // 1. Validación de coincidencia de claves (Seguridad en el cliente)
    if (passRaw !== confirmRaw) {
        alert("Las contraseñas no coinciden.");
        return;
    }

    // 2. Validación de longitud mínima (siguiendo tu auth_service.py)
    if (passRaw.length < 8) {
        alert("La contraseña debe tener al menos 8 caracteres.");
        return;
    }

    const payload = {
        username: limpiarInput(userRaw),
        password: passRaw
    };

    try {
        const response = await fetch(`${API_URL}/registro`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        if (response.ok) {
            alert(result.message || "Cuenta creada con éxito.");
            window.location.href = "/static/login.html";
        } else {
            alert(`Error en registro: ${result.detail}`);
        }
    } catch (error) {
        alert("Error crítico al procesar el registro.");
    }
}