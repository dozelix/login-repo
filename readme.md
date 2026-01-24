# **Sistema de Autenticación Modular (Arquitectura de 4 Capas \- Web)**

Este proyecto es una **plantilla profesional de login y registro** que ha evolucionado de una estructura monolítica en Streamlit a una **arquitectura web desacoplada**. Utiliza **FastAPI** como orquestador del backend y una interfaz moderna basada en **HTML5, CSS3 y JavaScript nativo**.  
El diseño sigue los principios de **Clean Architecture**, permitiendo que la lógica de negocio y la persistencia de datos sean totalmente independientes de la interfaz de usuario.

## **Estructura del Proyecto**

```python
LOGIN/  
│  
├── app.py                 \# Servidor API REST (FastAPI) y ruteo de estáticos  
├── .env                   \# Variables de entorno (Credenciales de base de datos)  
├── requirements.txt       \# Dependencias del sistema (FastAPI, Bcrypt, etc.)  
│  
├── frontend/              \# CAPA DE PRESENTACIÓN (Web Nativa)  
│    ├── login.html        \# Formulario de acceso  
│    ├── register.html     \# Formulario de nuevo usuario  
│    ├── style.css         \# Estética visual (Paleta Ocre/Arena)  
│    └── auth\_logic.js     \# Lógica de cliente y sanitización XSS  
│  
├── servicio/              \# CAPA DE SERVICIO (Lógica de Negocio)  
│    └── auth\_service.py   \# Hashing Bcrypt y validaciones de seguridad  
│  
├── persistencia/          \# CAPA DE DATOS (MySQL)  
│    └── db\_manager.py     \# Consultas parametrizadas y gestión de conexión  
│  
└── modelos/               \# CAPA DE ENTIDADES  
     └── usuario.py        \# Objeto Usuario (Estructura de datos)
```

## **Tecnologías y Capas**

### **1\. Capa de Presentación (frontend/)**

Se ha migrado a un entorno web estándar. El archivo auth\_logic.js actúa como mediador, gestionando las peticiones asíncronas (fetch) hacia la API y realizando la limpieza de datos en el cliente para prevenir ataques de inyección básica.

### **2\. Capa de Servicio (servicio/)**

Contiene la lógica crítica. Aquí se procesa el cifrado de contraseñas mediante **Bcrypt** antes de enviarlas a la base de datos, asegurando que la información sensible nunca se almacene en texto plano.

### **3\. Capa de Persistencia (persistencia/)**

Encargada de la comunicación con **MySQL**. Utiliza técnicas de **consultas parametrizadas** para blindar el sistema contra ataques de **Inyección SQL**.

## **Instalación y Ejecución**

1. **Configurar la Base de Datos:** 

```console
   Crea un archivo .env en la raíz con tus credenciales:  
   DB\_HOST=localhost  
   DB\_USER=tu\_usuario  
   DB\_PASS=tu\_password  
   DB\_NAME=tu\_base\_de\_datos
```

2. **Instalar Dependencias:**  

```python
   pip install \-r requirements.txt
```

3. **Lanzar el Servidor:**  

```console
   uvicorn app:app \--reload
```

   *Accede a http://localhost:8000 para ver la interfaz de usuario.*

## **🔐 Seguridad Implementada**

* **Sanitización XSS:** Control de caracteres especiales en el frontend antes de la transmisión.  
* **Bcrypt Hashing:** Implementación de *salts* aleatorios para la protección de identidades.  
* **CORS Enabled:** Configuración de middleware en FastAPI para permitir comunicación segura entre origen y destino.  
* **Arquitectura Desacoplada:** Facilita la auditoría de seguridad al separar claramente la entrada de datos de la ejecución de procesos.

**Autor:** DøzzeL  
*Desarrollo enfocado en modularidad, escalabilidad y buenas prácticas de ingeniería de software.*