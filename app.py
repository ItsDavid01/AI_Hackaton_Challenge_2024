import streamlit as st
import time
import random
import chatbot as cb
import funtions as ft

bot = cb.chatBot()
fun = ft.functions()
functions_name = [fun.empresas_competidoras, fun.ventas_empresa, fun.modelos_mas_vendidos, fun.ventas_toyota, fun.informacion_no_disponible]
bot.inicializar(functions_name)

if "bot" not in st.session_state:
    st.session_state.bot = bot

def createStream(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.1)

st.title("Chat with us")
initial_response = "Bienvenido a Luxor, soy tu asistente virtual ¿En que puedo ayudarte? Pregunta acerca de nuestros heviculos, servicios, garantía y mas"
temp_response = ["Si tienes más preguntas, aquí estoy para ayudarte!",
                "Si necesitas ayuda adicional, no dudes en preguntar!",
                "¿En qué más puedo ayudarte?",
                "Ha sido un placer ayudarte, ¿alguna u otra pregunta?"]

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
    bot_response = st.session_state.bot.get_response(prompt)
    with st.chat_message("Assistant"):
        st.write_stream(createStream(bot_response))
    st.session_state.messages.append(["Assistant", bot_response])
    st.rerun()