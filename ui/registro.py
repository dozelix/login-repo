import streamlit as st
import servicio.auth_service as auth

def render_registro():
    st.subheader("Formulario de Registro")
    with st.form("registro"):
        user = st.text_input("Usuario")
        pw = st.text_input("Contraseña", type="password")
        
        if st.form_submit_button("Crear Cuenta"):
            # La UI solo llama al Servicio
            exito, mensaje = auth.validar_registro(user, pw)
            if exito:
                st.success(mensaje)
            else:
                st.warning(mensaje)
    
    if st.button("Ir al Login"):
        st.session_state.vista = "login"
        st.rerun()