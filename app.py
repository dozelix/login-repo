import streamlit as st
import logging
from ui.login import render_login
from ui.registro import render_registro

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Sistema de Acceso Seguro", 
    page_icon="🛡️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CAPA DE ESTILO (CSS Inyectado) ---
def aplicar_estilos_profesionales():
    """
    Inyecta el diseño visual para mantener la coherencia estética
    sin ensuciar los módulos de lógica o interfaz.
    """
    st.markdown("""
    <style>
        /* Fondo con degradado profundo */
        .stApp {
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        }
        
        /* Contenedor tipo Glassmorphism para los formularios */
        div.stForm {
            background: rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 20px !important;
            padding: 3rem !important;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
        }

        /* Títulos y etiquetas en blanco */
        h1, h2, h3, label, p, span {
            color: #ffffff !important;
            font-family: 'Inter', 'Segoe UI', sans-serif;
        }

        /* Inputs modernos */
        .stTextInput input {
            background-color: rgba(255, 255, 255, 0.07) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 10px !important;
        }

        /* Botón de acción principal */
        .stButton button {
            width: 100%;
            background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%) !important;
            color: white !important;
            font-weight: 700 !important;
            border: none !important;
            border-radius: 10px !important;
            text-transform: uppercase;
            transition: 0.3s ease all !important;
        }

        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0, 242, 254, 0.3) !important;
        }

        /* Ocultar elementos innecesarios de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def main():
    """
    Punto de entrada de la aplicación.
    Solo gestiona el estado y el enrutamiento entre vistas.
    """
    aplicar_estilos_profesionales()
    
    # 1. Inicialización de Estados Globales
    if 'autenticado' not in st.session_state:
        st.session_state.autenticado = False
    if 'vista' not in st.session_state:
        st.session_state.vista = 'login'

    # 2. Lógica de Enrutamiento (Router)
    try:
        if st.session_state.autenticado:
            # Vista una vez logueado
            st.title("🚀 Panel de Control")
            st.write("Bienvenido al área segura de la aplicación.")
            
            if st.sidebar.button("Cerrar Sesión"):
                st.session_state.autenticado = False
                st.rerun()
        else:
            # Selección de capa de presentación basada en el estado
            if st.session_state.vista == 'login':
                render_login()
            elif st.session_state.vista == 'registro':
                render_registro()
                
    except Exception as e:
        # Blindaje final: El usuario nunca ve el error técnico
        logging.critical(f"Error crítico en el orquestador principal: {str(e)}")
        st.error("Lo sentimos, el sistema no puede cargar en este momento. Inténtelo más tarde.")

if __name__ == "__main__":
    main()