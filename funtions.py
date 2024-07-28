import mysql.connector
import os
import datetime

class functions():

    def proyeccion_ventas(self):
            
            '''Funcion que retorna la proyeccion de ventas de la empresa'''
    
            query = f"SELECT fecha, valor FROM proyeccion"
            data_list = self.get_data_from_db(query)
            for item in data_list:
                item['fecha'] = item['fecha'].strftime('%Y-%m')
            text = ""
            for item in data_list:
                text += f"\n- Fecha: {item['fecha']}, Valor: {item['valor']}"
            return text

    def empresas_competidoras(self):

        '''Funcion que retorna las empresas competidoras de la empresa'''
        
        query = f"SELECT Empresa, Ventas_2022, Ventas_2023 FROM Ventas_anuales_rivales"
        return self.get_data_from_db(query)
    
    def ventas_empresa(self):

        '''Funcion que retorna la informacion de ventas de la empresa'''

        query = f"SELECT fecha, valor FROM ventas_empresa_mensual"
        data_list = self.get_data_from_db(query)
        for item in data_list:
            item['fecha'] = item['fecha'].strftime('%Y-%m')
        text = ""
        for item in data_list:
            text += f"\n- Fecha: {item['fecha']}, Valor: {item['valor']}"
        return text
    
    def modelos_mas_vendidos(self):
            
            '''Funcion que retorna los modelos mas vendidos de las empresas competidoras'''
    
            query = f"SELECT Marca, Modelo, Colores FROM Modelos_mas_vendidos"
            return self.get_data_from_db(query)
    
    def ventas_toyota(self):

        '''Funcion que retorna las ventas de Toyota'''

        query = f"SELECT Mes, Ventas FROM Toyota_ventas_mensuales_2023"
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