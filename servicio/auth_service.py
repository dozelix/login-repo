import bcrypt
from password_validator import PasswordValidator
# Importamos la capa de persistencia (que definiremos en el siguiente paso)
import persistencia.db_manager as db

def _configurar_reglas():
    """Define qué hace que una contraseña sea válida."""
    schema = PasswordValidator()
    schema.min(8).has().uppercase().has().digits().has().symbols()
    return schema

def generar_hash(password_plana: str) -> str:
    """Convierte texto plano en un hash seguro con sal aleatoria."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_plana.encode('utf-8'), salt).decode('utf-8')

def validar_registro(username, password):
    """Lógica para registrar un usuario nuevo."""
    if not username or not password:
        return False, "Faltan datos obligatorios."
    
    # 1. Consultar a persistencia si el usuario existe
    if db.buscar_usuario(username):
        return False, "El nombre de usuario ya está ocupado."
    
    # 2. Validar complejidad de la clave
    validador = _configurar_reglas()
    if not validador.validate(password):
        return False, "Clave débil: requiere 8 caracteres, mayúscula, número y símbolo."
    
    # 3. Hashear y enviar a guardar
    pw_hash = generar_hash(password)
    if db.guardar_usuario(username, pw_hash):
        return True, "Registro exitoso."
    
    return False, "Error al conectar con la base de datos."

def intentar_login(username, password):
    """Verifica si las credenciales son correctas."""
    if not username or not password:
        return False
    
    # Pedimos los datos a la capa de persistencia
    usuario_db = db.buscar_usuario(username)
    
    if usuario_db:
        # bcrypt.checkpw compara la clave plana con el hash almacenado
        # (Extrayendo automáticamente la 'salt' del hash)
        return bcrypt.checkpw(
            password.encode('utf-8'), 
            usuario_db['password'].encode('utf-8')
        )
    return False