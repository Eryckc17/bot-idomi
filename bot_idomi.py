import telebot
import requests
from bs4 import BeautifulSoup
import time
from threading import Thread
from flask import Flask
import os

# 1. Configuración de Flask para Render
app = Flask(__name__)

@app.route('/')
def health_check():
    return "IDOMI-BOT VIGILANTE ACTIVO", 200

# 2. Tu configuración de Telegram
TOKEN = '8627174315:AAGKTN6-WLuBqyFPZxoVatP_L7rrRq14iJA'
CHAT_ID = '644581238'
URL_PORTAL = 'https://www.dgcp.gob.do/visualizar-procesos/'

bot = telebot.TeleBot(TOKEN)

# 3. Función de búsqueda (Vigilancia)
def buscar_bucle():
    while True:
        try:
            response = requests.get(URL_PORTAL, timeout=20)
            if response.status_code == 200:
                contenido = response.text.lower()
                # Términos clave para IDOMI SRL
                if any(x in contenido for x in ["lona", "asfaltica", "impermeabilizacion"]):
                    bot.send_message(CHAT_ID, "🚨 ¡ALERTA IDOMI! Se detectó un proceso relevante en el portal de la DGCP.")
            print("Chequeo de portal completado...")
        except Exception as e:
            print(f"Error en vigilancia: {e}")
        time.sleep(1800) # Revisa cada 30 minutos

if __name__ == "__main__":
    # Iniciamos el bucle de búsqueda en un hilo separado
    t = Thread(target=buscar_bucle)
    t.daemon = True
    t.start()
    
    bot.send_message(CHAT_ID, "🚀 IDOMI-BOT EN LÍNEA (MODO NUBE). Vigilando portal cada 30 min.")
    
    # Iniciamos el servidor web en el puerto que pide Render
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
