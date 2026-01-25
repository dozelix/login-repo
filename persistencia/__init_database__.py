"""
Script de inicialización de base de datos.
Ejecutar este archivo UNA SOLA VEZ para crear la estructura necesaria.
"""
import mysql.connector
import os
import sys
from dotenv import load_dotenv

# Agregar el directorio padre al path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Cargamos las variables del .env
load_dotenv()

def crear_tabla_usuarios():
    """Crea la tabla 'usuarios' si no existe."""
    
    # Configuración desde .env
    config = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': os.getenv('DB_PORT', '3306'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASS', ''),
        'database': os.getenv('DB_NAME', 'generic_db')
    }
    
    print("=" * 50)
    print("INICIALIZADOR DE BASE DE DATOS")
    print("=" * 50)
    print(f"Conectando a MySQL en {config['host']}:{config['port']}...")
    
    try:
        # Conectar al servidor MySQL (sin especificar bd primero)
        conn = mysql.connector.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['password']
        )
        cursor = conn.cursor()
        
        # 1. Crear la base de datos si no existe
        db_name = config['database']
        print(f"Creando base de datos '{db_name}' si no existe...")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute(f"USE {db_name}")
        
        # 2. Crear la tabla usuarios
        print("Creando tabla 'usuarios'...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """)
        
        conn.commit()
        
        # 3. Insertar usuario de prueba (opcional)
        print("\n¿Deseas insertar un usuario de prueba? (s/n)")
        respuesta = input("> ").strip().lower()
        
        if respuesta == 's':
            from servicio.auth_service import generar_hash
            test_user = input("Nombre de usuario de prueba: ").strip()
            test_pass = input("Contraseña de prueba: ").strip()
            
            if test_user and test_pass:
                hashed = generar_hash(test_pass)
                cursor.execute(
                    "INSERT INTO usuarios (username, password) VALUES (%s, %s)",
                    (test_user, hashed)
                )
                conn.commit()
                print(f" Usuario de prueba '{test_user}' creado exitosamente!")
        
        cursor.close()
        conn.close()
        
        print("\n" + "=" * 50)
        print(" INICIALIZACIÓN COMPLETA")
        print("=" * 50)
        print(f"Base de datos: {db_name}")
        print("Tabla: usuarios")
        print("\nPróximo paso: Ejecutar el servidor con:")
        print("  uvicorn app:app --reload")
        
    except mysql.connector.Error as err:
        print(f"\nERROR DE CONEXIÓN: {err}")
        print("\nVerifica que:")
        print("  1. MySQL esté ejecutándose")
        print("  2. Las credenciales en .env sean correctas")
        print("  3. El puerto sea el correcto (default: 3306)")

if __name__ == "__main__":
    crear_tabla_usuarios()

