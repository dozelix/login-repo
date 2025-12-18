import mysql.connector
import os
from dotenv import load_dotenv

# Cargamos las variables del .env
load_dotenv()

class DBManager:
    def __init__(self):
        # Leemos las credenciales que pusimos en el .env
        self.config = {
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', '3306'),
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASS', ''),
            'database': os.getenv('DB_NAME', 'generic_db')
        }

    def _conectar(self):
        """Crea una conexión nueva a la base de datos."""
        return mysql.connector.connect(**self.config)

    def buscar_usuario(self, username):
        """Busca un usuario por su nombre y retorna sus datos."""
        conn = self._conectar()
        cursor = conn.cursor(dictionary=True) # Retorna diccionarios en lugar de tuplas
        
        query = "SELECT * FROM usuarios WHERE username = %s"
        cursor.execute(query, (username,))
        usuario = cursor.fetchone()
        
        cursor.close()
        conn.close()
        return usuario

    def guardar_usuario(self, username, password_hash):
        """Inserta un nuevo usuario con su contraseña ya hasheada."""
        try:
            conn = self._conectar()
            cursor = conn.cursor()
            
            query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, password_hash))
            
            conn.commit() # Importante para guardar cambios
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error en persistencia: {e}")
            return False

# Instancia global para ser usada por el servicio
db_manager = DBManager()