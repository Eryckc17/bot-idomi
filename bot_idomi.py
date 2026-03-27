import telebot
import requests
from bs4 import BeautifulSoup
import time

TOKEN = '8627174315:AAGKTN6-WLuBqyFPZxoVatP_L7rrRq14iJA'
CHAT_ID = '644581238'
URL_PORTAL = 'https://www.dgcp.gob.do/visualizar-procesos/'

bot = telebot.TeleBot(TOKEN)

def buscar():
    try:
        res = requests.get(URL_PORTAL, timeout=15)
        if "lona" in res.text.lower() or "asfaltica" in res.text.lower():
            bot.send_message(CHAT_ID, "🚨 ALERTA IDOMI: Se encontró proceso en el portal.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    bot.send_message(CHAT_ID, "🚀 IDOMI-BOT EN LÍNEA (RENDER).")
    while True:
        buscar()
        time.sleep(1800)
      
