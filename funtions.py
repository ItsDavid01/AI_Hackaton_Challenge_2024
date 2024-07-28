import mysql.connector
import os

class functions():

    def empresas_competidoras(self):

        '''Funcion que retorna las empresas competidoras de la empresa'''
        
        query = f"SELECT empresas_comp_name, ventas_anuales FROM empresas_comp"
        return self.get_data_from_db(query)
    
    def informacion_no_disponible(self):
        return "Informacion no disponible"

    def get_data_from_db(self, query):
        conn = mysql.connector.connect(
            host="viaduct.proxy.rlwy.net",
            user="root",
            password="ggDyJRwjffNWsZvbZZdiYzUOzomENxFd",
            database="railway",
            port=25264
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result