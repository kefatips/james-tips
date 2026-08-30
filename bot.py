from flask import Flask
import threading
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes, ConversationHandler

TOKEN = "8816171451:AAH4qPykEt-MSCUHQfJMwoqRKfq37-1kTg9s"

NAME, GAME = range(2)

# Keep-alive for Render
app_web = Flask(__name__)
@app_web.route('/')
def home(): return "JAMES TIPS LIVE!"
def run_web(): app_web.run(host='0.0.0.0', port=10000)
threading.Thread(target=run_web, daemon=True).start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("WELCOME TO JAMES TIPS 🔥\n\nWhat is your name?")
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text
    keyboard = [
        [InlineKeyboardButton("3+ ODDS - 500 KES", callback_data='500')],
        [InlineKeyboardButton("5+ ODDS - 1000 KES", callback_data='1000')],
        [InlineKeyboardButton("💰 Check Balance", callback_data='balance')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"Nice! {update.message.text} Choose Package:", reply_markup=reply_markup)
    return GAME

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'balance':
        await query.edit_message_text("💰 Balance: 0 KES\n\nLIPA M-PESA: 0712 345 678\nTill: James Tips")
    else:
        await query.edit_message_text(f"LIPA M-PESA: 0712345678\n\nAmount: {query.data} KES\n\nSend screenshot after payment to @JamesTipsAdmin")
    return ConversationHandler.END

app = ApplicationBuilder().token(TOKEN).build()
conv = ConversationHandler(entry_points=[CommandHandler('start', start)], states={NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)], GAME: [CallbackQueryHandler(button_click)]}, fallbacks=[])
app.add_handler(conv)
print("RUNNING")
app.run_polling()
