import hashlib
import streamlit as st

# Simulación de tabla de base de datos
if 'DB_USUARIOS' not in st.session_state:
    st.session_state.DB_USUARIOS = {
        "admin": "e183794396656711719b678125cf15f7956358c56643666f28148b5252b47e8e"
    }

def generar_hash(texto: str) -> str:
    return hashlib.sha256(texto.encode()).hexdigest()

def buscar_usuario(username: str):
    """Retorna el hash si existe, sino None."""
    return st.session_state.DB_USUARIOS.get(username)

def guardar_usuario(username, password_plana):
    """Guarda al usuario con su contraseña ya protegida."""
    try:
        hash_pw = generar_hash(password_plana)
        st.session_state.DB_USUARIOS[username] = hash_pw
        return True
    except Exception:
        return False