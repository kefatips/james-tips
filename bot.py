import os, sys, traceback
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8816171451:AAF0747baP6QAEGYecRtWFw3OwjrJFaKi4Y"
print("--- BOT.PY STARTED ---", flush=True)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is Live! Go to Telegram /start"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 JAMES TIPS LIVE! 🔥\n\nSend /tips")

async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚽ Tip: Over 1.5 - Stake small\n\n18+ Gamble responsibly")

def run_bot():
    try:
        print(">>> Starting Bot Polling...", flush=True)
        application = ApplicationBuilder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("tips", tips))
        print(">>> Polling...", flush=True)
        application.run_polling(drop_pending_updates=True)
    except Exception as e:
        print(f"!!! BOT CRASHED: {e}", flush=True)
        traceback.print_exc()

if __name__ == "__main__":
    import threading
    t = threading.Thread(target=run_bot, daemon=False)
    t.start()
    print(">>> Flask starting...", flush=True)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
