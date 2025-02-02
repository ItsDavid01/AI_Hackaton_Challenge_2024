import streamlit as st
import time
import random
import chatbot as cb
import funtions as ft
import google.generativeai.types.generation_types as gemError
import google.api_core.exceptions as gooApiError

def createStream(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.1)
        
def intializeBot():
    bot = cb.chatBot()
    fun = ft.functions(st.secrets.HOST, st.secrets.USER, st.secrets.PASSWORD, st.secrets.DATABASE, st.secrets.PORT)
    functions_name = [fun.empresas_competidoras, fun.modelos_mas_vendidos, fun.ventas_toyota, fun.informacion_no_disponible, fun.ventas_generales_empresa_mensual, fun.detalles_ventas,
                      fun.proyeccion_ventas, fun.vehiculos_luxor, fun.clientes_luxor]
    bot.inicializar(functions_name, st.secrets.GOOGLE_API_KEY)
    return bot

if "bot" not in st.session_state:
    st.session_state.bot = intializeBot()

st.title("Asistente Virtual de Luxor:")
st.subheader("Tu Guía Experta en Ventas y Marketing Automotriz")
initial_response = "Bienvenido a Luxor, soy tu asistente virtual ¿En que puedo ayudarte? Pregunta acerca de nuestros vehículos, servicios, garantía y más"
temp_response = ["Si tienes más preguntas, aquí estoy para ayudarte!",
                "Si necesitas ayuda adicional, no dudes en preguntar!",
                "¿En qué más puedo ayudarte?",
                "Ha sido un placer ayudarte, ¿alguna u otra pregunta?"]

with st.sidebar:
    st.subheader("Opciones adicionales", divider="gray")
    st.markdown("limpiar conversación")
    resetChat = st.button("Limpiar")
    st.markdown(''':red[Recuerda que esta accion es irreversible]''')
    if resetChat:
        st.session_state.messages = [["Assistant", initial_response]]   

if "messages" not in st.session_state:
    st.session_state.messages = [["Assistant", initial_response]]

for message in st.session_state.messages:
    with st.chat_message(message[0]):
        st.write(message[1])

prompt = st.chat_input("Ask Away!")

if prompt:
    with st.chat_message("User"):
        st.write(prompt)
    st.session_state.messages.append(["User", prompt])
    try:
        bot_response = st.session_state.bot.get_response(prompt).text
    except gemError.StopCandidateException:
        try:
            bot_response = st.session_state.bot.get_response(prompt).text
        except:
            bot_response = "Lamento los incovenientes, por favor ¿Podría ser más específico en su pregunta?"
            
    except gooApiError.ResourceExhausted:
        bot_response = "Lo sentimos, los recursos disponibles para procesar su solicitud se han agotado temporalmente. Por favor, intente nuevamente más tarde. Si el problema persiste, contacte al soporte técnico de Luxor."
       
    except Exception as e: 
        bot_response = "Lo siento, algo salió mal. Por favor, inténtalo de nuevo."
        print(e)
    
    with st.chat_message("Assistant"):
        st.write_stream(createStream(bot_response))
    st.session_state.messages.append(["Assistant", bot_response])
    st.rerun()