import os
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN", "8816171451:AAFP7W0p2L5f8k3R2XvNqLm9oTjHs4uYdE1Q")

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is Live!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("James Tips Bot LIVE! Send /tips")

async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Today Tips: Over 1.5 Goals! ✅")

def run_bot():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("tips", tips))
    application.run_polling()

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
