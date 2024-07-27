import mysql.connector
import os

class functions():

    def empresas_competidoras(self):
        return f"{self.get_data_from_db()}"
    
    def informacion_no_disponible(self):
        return "Informacion no disponible"

    def get_data_from_db(self, ventas_anuales = None):
        conn = mysql.connector.connect(
            host="viaduct.proxy.rlwy.net",
            user="root",
            password="ggDyJRwjffNWsZvbZZdiYzUOzomENxFd",
            database="railway",
            port=25264
        )
        cursor = conn.cursor(dictionary=True)
        if (ventas_anuales):
            query = f"SELECT * FROM empresas_comp WHERE ventas_anuales >= {ventas_anuales}"
        query = f"SELECT * FROM empresas_comp"
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result