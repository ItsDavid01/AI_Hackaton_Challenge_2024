import mysql.connector

class functions():

    def empresas_competidoras(self):
        return f"Las empresas competidoras son: {self.get_data_from_db()}"
    
    def informacion_no_disponible(self):
        return "Informacion no disponible"

    def get_data_from_db(self):
        conn = mysql.connector.connect(
            host="viaduct.proxy.rlwy.net",
            user="root",
            password="ggDyJRwjffNWsZvbZZdiYzUOzomENxFd",
            database="railway",
            port=25264
        )
        cursor = conn.cursor(dictionary=True)
        query = f"SELECT * FROM empresas_comp"
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result