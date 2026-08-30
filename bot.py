from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, ContextTypes, filters, CallbackQueryHandler
TOKEN = "8816171451:AAH4qPykEt-MSCUHQfJMwoqRKfq37-lSScc"
NAME, GAME = range(2)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("WELCOME TO JAMES TIPS! What's your name?")
    return NAME
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text
    keyboard = [[InlineKeyboardButton("3+ ODDS - 500 KES", callback_data="1")],[InlineKeyboardButton("5+ ODDS - 1000 KES", callback_data="2")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"Nice! Choose package:", reply_markup=reply_markup)
    return GAME
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"LIPA M-PESA: 0720860503 Amount: {query.data}00 KES\nSend screenshot after pay!")
    return ConversationHandler.END
app = ApplicationBuilder().token(TOKEN).build()
conv = ConversationHandler(entry_points=[CommandHandler('start', start)], states={NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)], GAME: [CallbackQueryHandler(button_click)]}, fallbacks=[])
app.add_handler(conv)
print("RUNNING")
app.run_polling()
