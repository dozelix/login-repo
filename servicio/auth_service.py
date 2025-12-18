from password_validator import PasswordValidator
import persistencia.db_manager as db

def _configurar_reglas():
    schema = PasswordValidator()
    schema.min(8).has().uppercase().has().digits().has().symbols()
    return schema

def validar_registro(username, password):
    """
    Lógica de Negocio Centralizada.
    Coordina validaciones y llamadas a persistencia.
    """
    # 1. Validaciones básicas
    if not username or not password:
        return False, "Faltan datos obligatorios."
    
    # 2. Verificar disponibilidad
    if db.buscar_usuario(username):
        return False, "El nombre de usuario ya está ocupado."
    
    # 3. Validar complejidad
    validador = _configurar_reglas()
    if not validador.validate(password):
        fallos = validador.validate(password, report=True)
        return False, f"Clave débil. Requisitos faltantes: {', '.join(fallos)}"
    
    # 4. Ejecutar acción en persistencia
    if db.guardar_usuario(username, password):
        return True, "Registro exitoso."
    
    return False, "Error interno al guardar."

def intentar_login(username, password):
    """Coordina el proceso de autenticación."""
    if not username or not password:
        return False
    
    hash_almacenado = db.buscar_usuario(username)
    if hash_almacenado:
        return hash_almacenado == db.generar_hash(password)
    return False