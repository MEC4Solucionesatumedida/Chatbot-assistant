# main.py

import openai
from utils.modules import create_assistant, get_assistant, start_new_chat, add_message, get_messages_in_chat, run_chat

# Configura tu clave API de OpenAI
openai.api_key = ''

# Crea un nuevo asistente
assistant = create_assistant(
    client=openai,
    name="CRM",
    description="Chatbot que registra solicitudes de productos de los clientes.",
    instructions="Eres un asistente virtual que debe registrar un producto que necesito que importes, nombre del producto más las características necesarias para buscarlos online. Sólo debes registrar el producto, sus características y los datos generales del cliente (Nombre, Ciudad de residencia y email). Saludar y despedirse amablemente.",
    tools=[],
    model="gpt-3.5-turbo-16k"
)

print("Asistente creado:", assistant)

# Obtiene el asistente por su ID (puedes usar el ID del asistente creado anteriormente)
# assistant = get_assistant(openai, "ID_DEL_ASISTENTE")

# Inicia un nuevo chat
thread = start_new_chat(openai)

# Agrega mensajes al chat
add_message(openai, thread, "Hola, ¿cómo estás?")
add_message(openai, thread, "Cuéntame más sobre ti.")

# Obtiene los mensajes en el chat
messages = get_messages_in_chat(openai, thread)
for message in messages.data:
    print(f"{message.role}: {message.content}")
print("Chat iniciado:", thread)

# Ejecuta el chat con el asistente
run = run_chat(openai, thread, assistant)
# main.py