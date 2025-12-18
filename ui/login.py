import streamlit as st
import persistencia.db_manager as db

def render_login():
    """Dibuja el entorno gráfico de login y gestiona su interacción."""
    st.markdown("<h1>INICIAR SESIÓN</h1>", unsafe_allow_html=True)
    
    with st.form("form_login"):
        user = st.text_input("Usuario")
        pw = st.text_input("Contraseña", type="password")
        
        if st.form_submit_button("ENTRAR"):
            # Validación de identidad (Capa de Datos)
            if db.verificar_credenciales(user, pw):
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("¿No tienes cuenta? Regístrate"):
        st.session_state.vista = 'registro'
        st.rerun()