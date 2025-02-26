## Prueva de API DeepSeak

# Configuración de la API
API_URL = "https://api.deepseek.com/v1/chat/completions"  # Revisa la URL correcta en la documentación
API_KEY = "sk-3bfdcfe5d6fa40bdbc72256678ec3f5d"  # Reemplaza con tu API Key

import requests

def chat_with_deepseek(prompt):
    url = API_URL  # URL de la API de DeepSeek
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",  # Modelo de DeepSeek que deseas utilizar
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"
    
def main():
    print("Bienvenido al Chatbot de DeepSeek. Escribe 'salir' para terminar la conversación.")
    
    while True:
        user_input = input("Tú: ")
        
        if user_input.lower() == 'salir':
            print("Chatbot: ¡Adiós!")
            break
        
        response = chat_with_deepseek(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()