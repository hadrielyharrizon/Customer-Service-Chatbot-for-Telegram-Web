# app.py

from flask import Flask, request
from modules.telegram_bot import send_message

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if not data or "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    text = data["message"]["text"].lower()

    # Resposta simples
    if "horário" in text:
        send_message(chat_id, "Atendemos de segunda a sexta, das 9h às 18h.")
    elif "agendar" in text:
        send_message(chat_id, "Para agendar, envie o dia e horário desejado.")
    else:
        send_message(chat_id, "Desculpe, não entendi. Pode repetir?")

    return "ok"
