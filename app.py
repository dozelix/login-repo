from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from servicio.auth_service import intentar_login, validar_registro
import os

# Crear la app
app = FastAPI(title="Servidor de Autenticación Seguro")

# --- CONFIGURACIÓN DE SEGURIDAD (CORS) - DEBE SER LO PRIMERO ---
# Permitir CORS desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir cualquier origen
    allow_credentials=False,  # False cuando se usa allow_origins=["*"]
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=600,
)

# --- MODELOS DE DATOS ---
class UserAuth(BaseModel):
    username: str
    password: str

# --- RUTAS DE API (DEBEN IR ANTES DE MONTAR ESTÁTICOS) ---

@app.post("/login")
async def login(data: UserAuth):
    try:
        print(f"DEBUG: Intento de login para usuario: {data.username}")
            resultado = intentar_login(data.username, data.password)
        print(f"DEBUG: Resultado de intentar_login: {resultado}")
        if resultado:
            print(f"DEBUG: Login exitoso para {data.username}")
            return {"status": "success", "message": "Autenticación exitosa"}
        print(f"DEBUG: Credenciales incorrectas para {data.username}")
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    except HTTPException:
        raise
    except Exception as e:
        print(f"ERROR en login: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.post("/registro")
async def registro(data: UserAuth):
    try:
        exito, mensaje = validar_registro(data.username, data.password)
        if exito:
            return {"status": "success", "message": mensaje}
        raise HTTPException(status_code=400, detail=mensaje)
    except Exception as e:
        print(f"Error en registro: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/api/dashboard")
async def dashboard_api():
    """Endpoint de API para validar sesión en dashboard"""
    return {"status": "authenticated"}

# --- RUTAS DE PÁGINAS HTML ---

@app.get("/")
async def root():
    """Redirige al login"""
    return FileResponse("static/login.html")

@app.get("/home")
async def home_page():
    """Página de login"""
    return FileResponse("static/login.html")

@app.get("/dashboard-page")
async def dashboard_page():
    """Página del dashboard"""
    return FileResponse("static/dashboard.html")

# --- RUTAS DE ARCHIVOS ESTÁTICOS (Frontend) ---
# MONTAR ESTÁTICOS AL FINAL
app.mount("/static", StaticFiles(directory="static"))

# Para ejecutar: uvicorn app:app --reload
