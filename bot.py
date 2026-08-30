import os
from flask import Flask, request
import telegram
from telegram.ext import Application, CommandHandler

TOKEN = "8816171451:AAF0747baP6QAEGYecRtWFw3OwjrJFaKi4Y"
BOT_URL = "https://james-tips.onrender.com"

app = Flask(__name__)
bot_app = Application.builder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("🔥 James Tips Bot is LIVE! 🔥\n\nUse /tips")

async def tips(update, context):
    await update.message.reply_text("⚽ Today's Tips Loading...\n\n18+ Gamble responsibly")

bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CommandHandler("tips", tips))

@app.route("/")
def home():
    return "Bot is Live! Go to Telegram and send /start"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.update_queue.put_nowait(update)
    return "ok"

if __name__ == "__main__":
    import asyncio
    async def set_webhook():
        await bot_app.bot.set_webhook(url=f"{BOT_URL}/{TOKEN}")
        print("Webhook set!")
    asyncio.run(set_webhook())
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
