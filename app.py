from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from servicio import auth_service # Tu lógica profesional existente

app = FastAPI(title="Servidor de Autenticación Seguro")

# --- CONFIGURACIÓN DE SEGURIDAD (CORS) ---
# Permite que tus archivos HTML se comuniquen con este servidor Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción, limita esto a tu dominio
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELOS DE DATOS ---
class UserAuth(BaseModel):
    username: str
    password: str

# --- ENDPOINTS (Rutas que reemplazarán a render_login y render_registro) ---

@app.post("/login")
async def login(data: UserAuth):
    """Reemplaza la lógica de render_login"""
    import persistencia.db_manager as db
    if db.verificar_credenciales(data.username, data.password):
        return {"status": "success", "message": "Autenticación exitosa"}
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")

@app.post("/registro")
async def registro(data: UserAuth):
    """Reemplaza la lógica de render_registro"""
    exito, mensaje = auth_service.validar_registro(data.username, data.password)
    if exito:
        return {"status": "success", "message": mensaje}
    raise HTTPException(status_code=400, detail=mensaje)

# Para ejecutar: uvicorn app:app --reload