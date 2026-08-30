import telebot
import os
from flask import Flask
import threading

BOT_TOKEN = os.environ.get("BOT_TOKEN") or "8816171451:AAF0747baP6QAEGYecRtWFw3OwjrJFaKi4Y"
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)
users = {}

packages = {
    "1": "3+ ODDS - 500 KES\nSure 3 games daily",
    "2": "5+ ODDS - 1000 KES\nVIP 5 odds",
    "3": "10+ ODDS - 2000 KES\nMega 10 odds",
    "4": "HT/FT + CORRECT SCORE - 3000 KES\nBig money",
    "5": "JACKPOT 15 GAMES - 1500 KES\nMidweek & weekend"
}

@app.route('/')
def home():
    return "Ecco Games Hub Live!"

@bot.message_handler(commands=['start'])
def start(m):
    chat_id = m.chat.id
    users[chat_id] = {"step": "name"}
    bot.send_message(chat_id, "🎮 WELCOME TO ECCO GAMES HUB 🎮\n\nI sell 100% SURE betting tips daily! 💯\nNo lose, pure profit 🔥\n\nWhat's your name? 😊")

@bot.message_handler(func=lambda m: True)
def handle(m):
    chat_id = m.chat.id
    text = m.text.strip()
    if chat_id not in users:
        bot.send_message(chat_id, "Type /start bro")
        return

    step = users[chat_id].get("step")
    name = users[chat_id].get("name", "bro")

    if step == "name":
        users[chat_id]["name"] = text
        users[chat_id]["step"] = "package"
        bot.send_message(chat_id, f"Nice {text}! 🤝 Choose package:\n\n1. 🔥 3+ ODDS - 500 KES\nSure 3 games daily\n\n2. 💰 5+ ODDS - 1000 KES\nVIP 5 odds\n\n3. 🚀 10+ ODDS - 2000 KES\nMega 10 odds\n\n4. 👑 HT/FT + CORRECT SCORE - 3000 KES\nBig money\n\n5. 🎯 JACKPOT 15 GAMES - 1500 KES\nMidweek & weekend\n\nJust type number 1-5")

    elif step == "package":
        if text not in ["1","2","3","4","5"]:
            bot.send_message(chat_id, "Type 1, 2, 3, 4 or 5 bro")
            return
        users[chat_id]["package"] = text
        users[chat_id]["step"] = "paid"
        sel = packages[text]
        bot.send_message(chat_id, f"Perfect choice {name}! ✅\n\nYou selected:\n👑 {sel}\n\n💳 LIPA NA M-PESA:\nSend to: 0738792626\nAmount: See above\n\nAfter paying, type PAID + M-PESA code\nExample: PAID QGHI2345\n\nI will send games instantly! 🎯")

    elif step == "paid":
        if "PAID" in text.upper():
            users[chat_id]["step"] = "verify"
            bot.send_message(chat_id, f"Sawa {name}! 🔍 Verifying...\n\nPlease forward M-PESA SMS to me. I will confirm in 2 mins and send games! 🎰🔥")
        else:
            bot.send_message(chat_id, "After paying, type PAID + M-PESA code\nExample: PAID QGHI2345")

    elif step == "verify":
        bot.send_message(chat_id, "Received! Checking now...")

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
