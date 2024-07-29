import mysql.connector
import streamlit as st

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
    
    def ventas_generales_empresa_mensual(self):

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
    
    def detalles_ventas(self):
             
        '''Funcion que retorna los detalles de las ventas'''
    
        query = f"SELECT Ventas.FechaVenta, Ventas.MetodoPago, Vehiculos.Marca, Vehiculos.Modelo, Vehiculos.Año, Vehiculos.Precio, Vehiculos.Stock, Vehiculos.Color, Vehiculos.Especificaciones FROM Ventas INNER JOIN Vehiculos ON Ventas.VehiculoID = Vehiculos.VehiculoID;"
        data_list = self.get_data_from_db(query)
        # Formateo de datos
        formatted_text = []
        for entry in data_list:
            formatted_text.append(
                f"Fecha de Venta: {entry['FechaVenta'].strftime('%d/%m/%Y')}\n"
                f"Metodo de Pago: {entry['MetodoPago']}\n"
                f"Marca: {entry['Marca']}\n"
                f"Modelo: {entry['Modelo']}\n"
                f"Año: {entry['Año']}\n"
                f"Precio: ${entry['Precio']:,.2f}\n"
                f"Stock: {entry['Stock']}\n"
                f"Color: {entry['Color']}\n"
                f"Especificaciones: {entry['Especificaciones']}\n\n"
            )
        return formatted_text

    def vehiculos_luxor(self):

        '''Funcion que retorna los vehiculos de la empresa'''

        query = f"SELECT Marca, Modelo, Año, Precio, Stock, Color, Especificaciones FROM Vehiculos"
        data_list = self.get_data_from_db(query)
        for vehiculo in data_list:
            text = f"{vehiculo['Precio']:,.2f}"
            vehiculo['Precio'] = f'${text}'
        return data_list
    
    def clientes_luxor(self):

        '''Funcion que retorna los clientes de la empresa'''

        query = f"SELECT Nombre, Apellido, CorreoElectronico, Telefono, Direccion FROM Clientes"
        return self.get_data_from_db(query)
    
    def informacion_no_disponible(self):
        return "Informacion no disponible"

    def get_data_from_db(self, query):
        conn = mysql.connector.connect(
            host=st.secrets.HOST,
            user=st.secrets.USER,
            password=st.secrets.PASSWORD,
            database=st.secrets.DATABASE,
            port=st.secrets.PORT
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result