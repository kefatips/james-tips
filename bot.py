import os
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8816171451:AAF0747baP6QAEGYecRtWFw3OwjrJFaKi4Y"

app = Flask(__name__)

@app.route("/")
def home():
    return "James Tips Bot LIVE!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 James Tips Bot is LIVE!\n\nSend /tips for tips")

async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚽ Over 1.5 Goals Tip Today\n\n18+ Gamble responsibly")

def run_bot():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("tips", tips))
    print("Bot polling started...")
    application.run_polling()

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
