from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from servicio import auth_service
import os

# Crear la app
app = FastAPI(title="Servidor de Autenticación Seguro")

# --- CONFIGURACIÓN DE SEGURIDAD (CORS) - DEBE SER LO PRIMERO ---
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",  # Permitir cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
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
        from servicio.auth_service import intentar_login
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
        exito, mensaje = auth_service.validar_registro(data.username, data.password)
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
    return FileResponse("frondend/login.html")

@app.get("/home")
async def home_page():
    """Página de inicio de sesión"""
    return FileResponse("frondend/login.html")

@app.get("/dashboard-page")
async def dashboard_page():
    """Página del dashboard"""
    return FileResponse("frondend/inicio.html")

# --- RUTAS DE ARCHIVOS ESTÁTICOS (Frontend) ---
# MONTAR ESTÁTICOS AL FINAL
app.mount("/static", StaticFiles(directory="frondend"))

# Para ejecutar: uvicorn app:app --reload
