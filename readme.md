
# Sistema de Autenticación Modular (Arquitectura de 4 Capas)

Este proyecto es una **plantilla profesional de login y registro** desarrollada con **Python** y **Streamlit**. Utiliza una **arquitectura limpia (Clean Architecture)** organizada en capas, lo que permite intercambiar el motor de base de datos o la interfaz gráfica con un esfuerzo mínimo.

---

## Estructura del Proyecto

```
LOGIN/
│
├── app.py                 # Orquestador principal y navegación
├── .env                   # Variables de entorno (Credenciales de DB)
├── requirements.txt       # Dependencias del proyecto
│
├── ui/                    # CAPA DE PRESENTACIÓN (Streamlit)
│    └── login_view.py     # Formularios y gestión de estados visuales
│
├── servicio/              # CAPA DE SERVICIO (Lógica de Negocio)
│    └── auth_service.py   # Validaciones, reglas de negocio y hashing
│
├── persistencia/          # CAPA DE DATOS (MySQL)
│    └── db_manager.py     # Consultas SQL y gestión de conexión
│
└── modelos/               # CAPA DE ENTIDADES
     └── usuario.py        # Clase Usuario (Estructura de datos)

```

---

##  Descripción de las Capas

### 1. **Capa de Presentación (ui/)**

Gestiona exclusivamente la interfaz con **Streamlit**. Captura los inputs del usuario y delega la responsabilidad de validación a la capa de servicio.

### 2. **Capa de Servicio (servicio/)**

El **"cerebro"** del sistema. Coordina las reglas de negocio:

* Validación de complejidad de clave con `password-validator`.
* Encriptación de contraseñas mediante **bcrypt**.
* Toma de decisiones basada en las respuestas de la base de datos.

### 3. **Capa de Persistencia (persistencia/)**

Encargada del acceso a datos. Implementa la conexión a **MySQL** utilizando variables de entorno para una configuración segura.

### 4. **Capa de Modelos (modelos/)**

Define el objeto `Usuario`, asegurando que los datos viajen de forma estandarizada entre la base de datos y la interfaz.

---

##  Instalación y Ejecución

1. **Clonar el proyecto:**
```bash
git clone <URL_DEL_REPOSITORIO>
cd LOGIN

```


2. **Configurar el entorno:**
modifica el archivo `.env` en la raíz con tus credenciales:
```env
DB_HOST=localhost
DB_USER=root
DB_PASS=tu_password
DB_NAME=generic_db

```


3. **Instalar dependencias:**
```bash
pip install -r requirements.txt

```


4. **Ejecutar la aplicación:**
```bash
streamlit run app.py

```



---

##  Seguridad de Nivel Profesional

* **Bcrypt Hashing:** Implementa *salts* aleatorios para proteger contra ataques de tablas arcoíris y fuerza bruta.
* **Variables de Entorno:** Uso de `python-dotenv` para mantener las credenciales fuera del código fuente.
* **Validación Robusta:** Reglas estrictas para contraseñas (min. 8 caracteres, mayúsculas, números y símbolos).
* **Inyección SQL:** Consultas parametrizadas para evitar ataques maliciosos a la base de datos.

---

##  Escalabilidad

Gracias al desacoplamiento, puedes:

* Cambiar MySQL por **PostgreSQL** o **SQLite** solo tocando la capa de persistencia.
* Cambiar Streamlit por **Flask/FastAPI** solo tocando la capa de presentación.

---

**Autor:** DøzzeL

*Enfoque en arquitectura limpia, modularidad y seguridad.*



