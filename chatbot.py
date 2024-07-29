import os
import google.generativeai as gemai

class chatBot:
    def __init__(self):
        self.history = []
        self.intruccion = """
        
Eres un asistente especializado en apoyar a los empleados del sector comercial de nuestra empresa automovilística llamada Luxor. Tu función principal es responder consultas relacionadas con ventas, marketing, competencias del mercado y cualquier otro aspecto del sector automovilístico. Debes dirigirte a nuestros empleados de manera formal y profesional en todo momento.

Instrucciones Específicas:

Alcance de las Consultas: Responderás únicamente a preguntas que se encuentren en nuestra base de datos. No responderás a consultas fuera de estos temas.
Confirmación de Consulta Satisfactoria: Cada vez que respondas satisfactoriamente a una consulta, incluirás un mensaje preguntando si el usuario desea continuar.
Formato de Respuesta: Si la base de datos proporciona un JSON o diccionario, lo traducirás en forma de lista para facilitar su comprensión.
Acceso Restringido: Operarás exclusivamente con la información proporcionada por nuestra base de datos interna, sin acceso a fuentes externas.

"""
    def inicializar(self, functions_name):
        gemai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        # Load the model (models/gemini-1.5-flash, models/gemini-1.5-pro-latest, models/gemini-1.5-pro, models/gemini-1.0-pro)
        gem = gemai.GenerativeModel("models/gemini-1.5-pro", system_instruction=self.intruccion, tools=functions_name)
        self.bot = gem.start_chat(history=self.history, enable_automatic_function_calling=True)

    def get_history(self):
        return self.bot.history
    
    def get_response(self, question):
        response = self.bot.send_message(question)
        return response