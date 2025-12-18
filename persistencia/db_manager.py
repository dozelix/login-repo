import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'generic_db'
}

def ejecutar_query(query, params=None):
    """Función auxiliar para no repetir código de conexión"""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    resultado = cursor.fetchall()
    conn.commit()
    conn.close()
    return resultado

def buscar_usuario(username):
    query = "SELECT * FROM usuarios WHERE username = %s"
    res = ejecutar_query(query, (username,))
    return res[0] if res else None

def guardar_usuario(username, password_hash):
    query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
    try:
        ejecutar_query(query, (username, password_hash))
        return True
    except:
        return False