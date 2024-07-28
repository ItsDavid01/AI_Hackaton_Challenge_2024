
import chatbot as cb
import funtions as ft

bot = cb.chatBot()

fun = ft.functions()

functions_name = [fun.empresas_competidoras]

bot.inicializar(functions_name)

print(f"\n {bot.get_response("Hola, me podrias decir cuales son las empresas competidoras actualmente pero de aviacion?")}")

