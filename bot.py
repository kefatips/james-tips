import os
import threading
from flask import Flask
import telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME", "@JamesTips")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
app = Flask(__name__)

# --- Your existing bot handlers ---
# (Keep all your @bot.message_handler code here)
# I'll add basic ones so it replies at least

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f"Sawa {message.from_user.first_name}! 🔍 Verifying...\n\nPlease send screenshot of M-PESA message to {CHANNEL_USERNAME}\nI will confirm in 2 mins and send games! 🎰🔥\n\nKeep your M-PESA code ready!")

@bot.message_handler(content_types=['photo', 'text'])
def handle_all(message):
    if message.text and message.text.startswith('/'): 
        return
    # Forward to admin etc - keep your original logic
    bot.reply_to(message, "✅ Screenshot received! Checking payment...\nAdmin @JamesTips will confirm in 2 minutes.")

# --- Flask for Render Web Service ---
@app.route('/')
def home():
    return "James Tips Bot is Running! ✅"

def run_bot():
    print(">>> Starting Bot Polling...")
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            print(f"Polling error: {e}")
            continue

if __name__ == "__main__":
    # Start bot in background thread
    threading.Thread(target=run_bot, daemon=True).start()
    print(">>> Flask starting...")
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
