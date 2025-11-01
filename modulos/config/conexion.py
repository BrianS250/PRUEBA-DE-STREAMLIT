import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='b5k8qe39grnzi1klvygs-mysql.services.clever-cloud.com',
            user='uleip8mubm6efqsx',
            password='hZosZ0z3KhmOSkoAGb1z',
            database='b5k8qe39grnzi1klvygs',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None

