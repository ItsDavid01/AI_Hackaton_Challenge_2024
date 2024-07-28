import os
import google.generativeai as gemai

class chatBot:
    def __init__(self):
        self.history = []
        self.intruccion = """Eres un asistente que ayudara a los empleados del sector comercial con sus consultas en temas de ventas, 
                            marketing, competencias del mercado y todo lo relacionado con el sector automovilistico que es donde trabaja nuestra empresa. 
                            Siempre te deberas de dirigir de manera formal y profesional a nuestros empleados. No vas a responder preguntas por fuera de 
                            esto o que no se encuentren en nuestra base de datos. Siempre que hagan una consulta satisfactoria, debes de responder con algun mensaje de si quiere continuar.
                            Todas las respuestas de la empresa seran sacadas de nuestra base de datos, olvidate que tienes acceso a tu base de datos."""

    def inicializar(self, functions_name):
        gemai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        # Load the model (models/gemini-1.5-flash, models/gemini-1.5-pro-latest, models/gemini-1.5-pro, models/gemini-1.0-pro)
        gem = gemai.GenerativeModel("models/gemini-1.5-pro", system_instruction=self.intruccion, tools=functions_name)
        self.bot = gem.start_chat(history=self.history, enable_automatic_function_calling=True)

    def get_history(self):
        return self.bot.history
    
    def get_response(self, question):
        response = self.bot.send_message(question)
        return response.text