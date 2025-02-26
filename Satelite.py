## Prueva de API DeepSeak

import requests

# Configuración de la API
API_URL = "https://api.deepseek.com"  # Revisa la URL correcta en la documentación
API_KEY = "sk-3bfdcfe5d6fa40bdbc72256678ec3f5d"  # Reemplaza con tu API Key

# Función para enviar un mensaje al chatbot
def enviar_mensaje(mensaje, historial=[]):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",  # Revisa el modelo correcto en la documentación
        "messages": historial + [{"role": "user", "content": mensaje}]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Bucle de conversación
historial = []
print("¡Hola! Soy tu chatbot. Escribe 'salir' para terminar.")
while True:
    user_input = input("Tú: ")
    if user_input.lower() == 'salir':
        break

    respuesta = enviar_mensaje(user_input, historial)
    if respuesta:
        print(f"Chatbot: {respuesta}")
        historial.append({"role": "user", "content": user_input})
        historial.append({"role": "assistant", "content": respuesta})
    else:
        print("Hubo un error al obtener la respuesta del chatbot.")