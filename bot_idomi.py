import telebot
import requests
from bs4 import BeautifulSoup
import time
from threading import Thread
from flask import Flask # Añadimos esto

# Configuración de Flask para engañar a Render
app = Flask('')
@app.route('/')
def home():
    return "IDOMI Vigilante está vivo"

def run_web():
    app.run(host='0.0.0.0', port=8080)

# TU CÓDIGO DEL BOT (Igual que antes)
TOKEN = '8627174315:AAGKTN6-WLuBqyFPZxoVatP_L7rrRq14iJA'
CHAT_ID = '644581238'
URL_PORTAL = 'https://www.dgcp.gob.do/visualizar-procesos/'
bot = telebot.TeleBot(TOKEN)

def buscar():
    while True:
        try:
            res = requests.get(URL_PORTAL, timeout=15)
            if "lona" in res.text.lower() or "asfaltica" in res.text.lower():
                bot.send_message(CHAT_ID, "🚨 ALERTA IDOMI: Se encontró proceso en el portal.")
        except:
            pass
        time.sleep(1800)

if __name__ == "__main__":
    # Lanzamos la web y el bot al mismo tiempo
    t = Thread(target=buscar)
    t.start()
    bot.send_message(CHAT_ID, "🚀 IDOMI-BOT EN LÍNEA (RENDER + WEB).")
    run_web()
