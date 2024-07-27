import chatbot as cb
import funtions as ft

bot = cb.chatBot()

fun = ft.functions()

functions_name = [fun.empresas_competidoras]

bot.inicializar(functions_name)

print(f"\n {bot.get_response("Hola, me podrias decir cuales son las empresas competidoras actualmente pero de aviacion?")}")

for content in bot.get_history():
    print(content.role, "-", [type(part).to_dict(part) for part in content.parts])
    print("-" * 80)
