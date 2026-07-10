# **Sistema de Autenticación Modular (Arquitectura de 4 Capas - Web)**

Plantilla profesional de login y registro con **FastAPI** + **MySQL**, inspirada en **Clean Architecture** (4 capas). Sin CSS incluido — tú defines el estilo en tu propio `static/style.css`.

## **Estructura del Proyecto**

```
LOGIN/
│
├── app.py                 # Servidor API REST (FastAPI) y ruteo de estáticos
├── .env.example           # Plantilla de variables de entorno (copia a .env)
├── requirements.txt       # Dependencias (FastAPI, Bcrypt, mysql-connector)
│
├── static/                # CAPA DE PRESENTACIÓN (Web Nativa)
│    ├── login.html        # Formulario de acceso
│    ├── register.html     # Formulario de nuevo usuario
│    ├── dashboard.html    # Página posterior al login
│    └── auth-logic.js     # Lógica de cliente y sanitización XSS
│
├── servicio/              # CAPA DE SERVICIO (Lógica de Negocio)
│    └── auth_service.py   # Hashing Bcrypt y validaciones de seguridad
│
├── persistencia/          # CAPA DE DATOS (MySQL)
│    └── db_manager.py     # Consultas parametrizadas y gestión de conexión
│
└── modelos/               # CAPA DE ENTIDADES
     └── usuario.py        # Objeto Usuario (Estructura de datos)
```

## **Tecnologías y Capas**

### **1\. Capa de Presentación (static/)**

Sin CSS incluido por defecto. Crea tu propio `static/style.css` y enlázalo desde los HTML. El archivo `auth-logic.js` gestiona las peticiones fetch y sanitización XSS.

El flujo de autenticación completo incluye:
- **login.html:** Formulario de acceso
- **register.html:** Formulario de registro con validación de complejidad de contraseña
- **dashboard.html:** Página posterior al login, con botón de cerrar sesión

### **2\. Capa de Servicio (servicio/)**

Contiene la lógica crítica. Aquí se procesa el cifrado de contraseñas mediante **Bcrypt** antes de enviarlas a la base de datos, asegurando que la información sensible nunca se almacene en texto plano.

### **3\. Capa de Persistencia (persistencia/)**

Encargada de la comunicación con **MySQL**. Utiliza técnicas de **consultas parametrizadas** para blindar el sistema contra ataques de **Inyección SQL**.

## **Flujo de Usuario**

1. **Registro:** El usuario accede a `/register.html`, completa el formulario con username y contraseña (mínimo 8 caracteres, mayúscula, número y símbolo). El sistema valida y guarda en la base de datos.

2. **Login:** El usuario accede a `/login.html`, ingresa sus credenciales. El sistema verifica contra MySQL y retorna éxito o error.

3. **Dashboard:** Tras login exitoso, el usuario es redirigido a `/dashboard-page`.

## **Instalación y Ejecución**

1. **Configurar la Base de Datos:** 

   ```console
   cp .env.example .env
   ```
   Edita `.env` con tus credenciales MySQL.

2. **Instalar Dependencias:**  

```python
   pip install \-r requirements.txt
```

3. **Lanzar el Servidor:**  

```console
   uvicorn app:app \--reload
```

   *Accede a http://localhost:8000 para ver la interfaz de usuario.*

## **Seguridad Implementada**

* **Sanitización XSS:** Control de caracteres especiales en el frontend antes de la transmisión.  
* **Bcrypt Hashing:** Implementación de *salts* aleatorios para la protección de identidades.  
* **CORS Enabled:** Configuración de middleware en FastAPI para permitir comunicación segura entre origen y destino.  
* **Arquitectura Desacoplada:** Facilita la auditoría de seguridad al separar claramente la entrada de datos de la ejecución de procesos.

**Autor:** DøzzeL  
*Desarrollo enfocado en modularidad, escalabilidad y buenas prácticas de ingeniería de software.*