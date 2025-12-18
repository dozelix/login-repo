```markdown
# 🛡️ Sistema de Autenticación Modular (Arquitectura de 4 Capas)

Este proyecto implementa un sistema de **login y registro profesional** utilizando **Python** y **Streamlit**, siguiendo un modelo de **arquitectura limpia** organizada en capas de responsabilidad. eso implica que es la base para iniciar sesion en app webs con css o derivados( su arquitectura de capas permite mudar facilmente el entorno grafico) 

---

## 🏗️ Estructura del Proyecto
```

```

PROYECTO/
│
├── app.py                 # Punto de entrada y orquestador de rutas
│
├── ui/                    # CAPA DE PRESENTACIÓN
│    └── registro_view.py   # Gestión de formularios y eventos visuales
│
├── servicio/              # CAPA DE SERVICIO (Lógica de Negocio)
│    └── auth_service.py    # Validación de reglas y coordinación de procesos
│
├── persistencia/          # CAPA DE DATOS
│    └── db_manager.py      # Hashing y comunicación con la base de datos
│
└── modelos/               # CAPA DE ENTIDADES
     └── usuario.py         # Definición del objeto Usuario


```

---

## 🛠️ Descripción de las Capas

### 1. **Capa de Presentación (ui/)**
- Contiene exclusivamente el entorno gráfico (**Streamlit**).
- No realiza validaciones de seguridad ni toca la base de datos.
- Su única función es capturar los datos del usuario y mostrar los mensajes de respuesta enviados por la capa de servicio.

### 2. **Capa de Servicio (servicio/)**
- Es el **"cerebro"** de la aplicación.
- Aquí residen las **Reglas de Negocio**:
  - ¿La contraseña cumple con los requisitos de seguridad?
  - ¿El usuario es apto para el registro?
- Traduce errores técnicos a mensajes comprensibles para el usuario final.

### 3. **Capa de Persistencia (persistencia/)**
- Se encarga del **almacenamiento**.
- Funcionalidades:
  - Hashing **SHA-256** de las contraseñas.
  - Gestión de búsqueda y escritura en la base de datos (simulada en `st.session_state`). (se remplazo el hash de hashlib por bcrypt)

### 4. **Capa de Modelos (modelos/)**
- Define el **"idioma común"** que hablan todas las capas.
- Al usar una clase `Usuario`, los datos viajan de forma estructurada y predecible por todo el sistema.

---

##  Instalación y Ejecución

1. Clonar el repositorio y entrar en la carpeta del proyecto:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd PROYECTO
   ```

2. Instalar dependencias:
   ```bash
   pip install streamlit password-validator
   ```

3. Ejecutar la aplicación:
   ```bash
   streamlit run app.py
   ```

---

##  Seguridad Implementada

- **Hashing de Contraseñas:** Nunca se almacenan contraseñas en texto plano.  
- **Validación de Complejidad:** Uso de `password-validator` para exigir mayúsculas, símbolos y números.  
- **Prevención de Duplicados:** Verificación de existencia de usuario antes de permitir el registro.  
- **Desacoplamiento:** La interfaz no tiene acceso directo a los datos, evitando manipulaciones accidentales.  

---

##  Enfoque del Proyecto

Este sistema fue desarrollado con un enfoque en:
- **Mantenibilidad:** Código modular y desacoplado.  
- **Escalabilidad:** Fácil de extender con nuevas reglas de negocio o persistencia real (ej. bases de datos SQL/NoSQL).  
- **Profesionalismo:** Arquitectura limpia y organizada por capas.  

---

##  Próximos Pasos

- Integración con una base de datos real (SQLite, PostgreSQL, MongoDB).  
- Implementación de recuperación de contraseñas.  
- Gestión de roles y permisos de usuario.  

---

 **Autor:** Proyecto diseñado con enfoque profesional en arquitectura modular y seguridad.
```

---
