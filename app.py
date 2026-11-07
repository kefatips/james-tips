from flask import Flask, request
import csv, os, requests
from datetime import datetime
app = Flask(__name__)
NL = chr(10)
WHATSAPP_LINK = "https://wa.me/message/CFCJWLOZ7IWZK1"
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
def send_telegram(text):
    if not BOT_TOKEN or not CHAT_ID:
        return False
    try:
        u = "https://api.telegram.org/bot"
        u = u + BOT_TOKEN + "/sendMessage"
        r = requests.post(u, json={"chat_id": CHAT_ID, "text": text}, timeout=10)
        return r.status_code == 200
    except Exception as e:
        print(e)
        return False
@app.route("/")
def home():
    h = "<!DOCTYPE html><html><head>"
    h = h + "<meta name='viewport' content='width=device-width, initial-scale=1'>"
    h = h + "<title>Zorak Loans</title><style>"
    h = h + "*{box-sizing:border-box;font-family:Arial,sans-serif}"
    h = h + "body{margin:0;background:#eef1f5;padding:15px}"
    h = h + ".top{text-align:center;color:#0f7a55;font-size:26px;font-weight:900;padding:10px}"
    h = h + ".top span{color:#111}"
    h = h + ".card{max-width:420px;margin:0 auto;background:white;border-radius:20px;padding:22px 18px}"
    h = h + ".card h2{text-align:center;margin:0;font-size:20px}"
    h = h + ".sub{text-align:center;font-size:12px;color:#888;margin:8px 0 20px}"
    h = h + ".calc{background:#f8f9fb;border-radius:16px;padding:16px}"
    h = h + ".row{display:flex;justify-content:space-between;font-weight:bold;font-size:14px;margin-top:12px}"
    h = h + ".row b{color:#2563eb}"
    h = h + "input[type=range]{width:100%;margin:12px 0 4px;accent-color:#2563eb}"
    h = h + ".minmax{display:flex;justify-content:space-between;font-size:12px;color:#999}"
    h = h + ".monthly{background:#eef4ff;border-radius:14px;text-align:center;padding:14px;margin-top:16px}"
    h = h + ".monthly small{color:#666;font-size:12px}"
    h = h + ".monthly div{color:#2563eb;font-size:30px;font-weight:900;margin-top:4px}"
    h = h + ".btn{display:block;text-align:center;background:linear-gradient(90deg,#2563eb,#7c3aed)"
    h = h + ";color:white;text-decoration:none;padding:15px;border-radius:30px;font-weight:900;margin-top:18px}"
    h = h + ".features{display:flex;justify-content:space-between;text-align:center;margin-top:20px}"
    h = h + ".features div{flex:1;font-size:11px;color:#666}"
    h = h + ".features span{font-size:28px;display:block}"
    h = h + "select{width:100%;padding:12px;border-radius:10px;border:1px solid #ddd;margin-top:12px}"
    h = h + ".wa2{display:block;text-align:center;background:#25D366;color:white"
    h = h + ";text-decoration:none;padding:13px;border-radius:30px;font-weight:bold;margin-top:12px}"
    h = h + "</style></head><body>"
    h = h + "<div class='top'>Zorak<span> Loans</span></div>"
    h = h + "<div class='card'>"
    h = h + "<h2>Get Your Loan Approved Fast</h2>"
    h = h + "<div class='sub'>Quick approval - Competitive rates - Flexible terms</div>"
    h = h + "<div class='calc'>"
    h = h + "<div style='text-align:center;font-weight:bold;'>Loan Calculator</div>"
    h = h + "<label style='display:block;margin-top:14px;font-size:13px;color:#555;'>Country</label>"
    h = h + "<select id='country' onchange='updateAll()'>"
    h = h + "<option value='Zimbabwe'>Zimbabwe</option>"
    h = h + "<option value='Zambia'>Zambia</option>"
    h = h + "<option value='Tanzania'>Tanzania</option></select>"
    h = h + "<div class='row'><span>Loan Amount</span><b id='amtLabel'>$5,000</b></div>"
    h = h + "<input type='range' id='amount' min='100' max='5000' value='5000' step='100' oninput='updateAll()'>"
    h = h + "<div class='minmax'><span id='minLabel'>$100</span><span id='maxLabel'>$5,000</span></div>"
    h = h + "<div class='row'><span>Loan Term</span><b id='termLabel'>12 months</b></div>"
    h = h + "<input type='range' id='term' min='6' max='60' value='12' oninput='updateAll()'>"
    h = h + "<div class='minmax'><span>6 months</span><span>60 months</span></div>"
    h = h + "<div class='monthly'><small>Monthly Payment</small><div id='monthly'>$434.94</div></div>"
    h = h + "</div>"
    h = h + "<a class='btn' href='/apply-form' id='applyBtn'>APPLY NOW</a>"
    h = h + "<a class='wa2' href='" + WHATSAPP_LINK + "'>Chat on WhatsApp Instead</a>"
    h = h + "<div class='features'>"
    h = h + "<div><span>Fast</span>Fast Approval<br>Within 24 hours</div>"
    h = h + "<div><span>Low</span>Low Rates<br>From 8%</div>"
    h = h + "<div><span>Safe</span>Secure<br>Bank-level</div></div>"
    h = h + "<p style='text-align:center;font-size:12px;color:#888;margin-top:15px;'>"
    h = h + "We will never ask for your PIN or OTP.</p></div>"
    h = h + "<script>function updateAll(){"
    h = h + "var c=document.getElementById('country').value;"
    h = h + "var sym='$';"
    h = h + "if(c=='Zambia')sym='K';"
    h = h + "if(c=='Tanzania')sym='TSh ';"
    h = h + "var amt=parseInt(document.getElementById('amount').value);"
    h = h + "var term=parseInt(document.getElementById('term').value);"
    h = h + "document.getElementById('amtLabel').innerText=sym+amt.toLocaleString();"
    h = h + "document.getElementById('minLabel').innerText=sym+'100';"
    h = h + "document.getElementById('maxLabel').innerText=sym+'5,000';"
    h = h + "document.getElementById('termLabel').innerText=term+' months';"
    h = h + "var r=0.08/12;"
    h = h + "var monthly=amt*r/(1-Math.pow(1+r,-term));"
    h = h + "document.getElementById('monthly').innerText=sym+monthly.toFixed(2);"
    h = h + "document.getElementById('applyBtn').href='/apply-form?amount='+amt+'&country='+c+'&term='+term;"
    h = h + "}updateAll();</script></body></html>"
    return h
@app.route("/apply-form")
def form():
    h = "<!DOCTYPE html><html><head>"
    h = h + "<meta name='viewport' content='width=device-width, initial-scale=1'>"
    h = h + "<title>Apply - Zorak Loans</title><style>"
    h = h + "*{box-sizing:border-box;font-family:Arial,sans-serif}"
    h = h + "body{margin:0;background:#eef1f5;padding:15px}"
    h = h + ".card{max-width:420px;margin:0 auto;background:white;border-radius:20px;padding:22px}"
    h = h + "h2{text-align:center;margin:0}"
    h = h + "p{text-align:center;color:#888;font-size:13px}"
    h = h + "label{display:block;margin-top:15px;font-size:13px;font-weight:bold}"
    h = h + "input,select{width:100%;padding:13px;border:1px solid #ddd;border-radius:10px;margin-top:6px}"
    h = h + ".btn{width:100%;background:linear-gradient(90deg,#2563eb,#7c3aed);color:white;border:none"
    h = h + ";padding:15px;border-radius:30px;font-weight:900;margin-top:20px;font-size:16px}"
    h = h + ".wa{display:block;text-align:center;background:#25D366;color:white;text-decoration:none"
    h = h + ";padding:13px;border-radius:30px;font-weight:bold;margin-top:12px}"
    h = h + "</style></head><body><div class='card'>"
    h = h + "<h2>Apply Now</h2>"
    h = h + "<p>We will call you back. We never ask for PIN or OTP.</p>"
    h = h + "<form method='POST' action='/apply'>"
    h = h + "<label>Full Name</label><input name='name' required placeholder='Full name'>"
    h = h + "<label>Phone Number</label><input name='phone' required placeholder='+260 / +263 / +255'>"
    h = h + "<label>Email (Optional)</label><input name='email' type='email' placeholder='you@gmail.com'>"
    h = h + "<label>Country</label><select name='country' required>"
    h = h + "<option value=''>Select Country</option>"
    h = h + "<option value='Zambia'>Zambia</option>"
    h = h + "<option value='Zimbabwe'>Zimbabwe</option>"
    h = h + "<option value='Tanzania'>Tanzania</option></select>"
    h = h + "<label>Loan Amount</label><input name='amount' id='amountInput' type='number' required>"
    h = h + "<label>Loan Term (months)</label><input name='term' id='termInput' type='number' value='12'>"
    h = h + "<label>Purpose of Loan</label><select name='purpose' required>"
    h = h + "<option value=''>Select Purpose</option>"
    h = h + "<option value='Business'>Business / Boost My Business</option>"
    h = h + "<option value='School Fees'>School Fees / Education</option>"
    h = h + "<option value='Medical'>Medical / Hospital Bills</option>"
    h = h + "<option value='Rent'>Rent / House</option>"
    h = h + "<option value='Agriculture'>Agriculture / Farming</option>"
    h = h + "<option value='Car'>Car / Transport</option>"
    h = h + "<option value='Personal'>Personal / Family Needs</option>"
    h = h + "<option value='Other'>Other</option></select>"
    h = h + "<label><input type='checkbox' required style='width:auto;'> I agree to be contacted</label>"
    h = h + "<button class='btn'>SUBMIT APPLICATION</button></form>"
    h = h + "<a class='wa' href='" + WHATSAPP_LINK + "'>Chat on WhatsApp Instead</a>"
    h = h + "<br><a href='/' style='display:block;text-align:center;'>Back to Calculator</a></div>"
    h = h + "<script>var p=new URLSearchParams(window.location.search);"
    h = h + "if(p.get('amount'))document.getElementById('amountInput').value=p.get('amount');"
    h = h + "if(p.get('term'))document.getElementById('termInput').value=p.get('term');"
    h = h + "if(p.get('country')){document.querySelector('select[name=country]').value=p.get('country');}"
    h = h + "</script></body></html>"
    return h
@app.route("/apply", methods=["POST"])
def apply():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    email = request.form.get("email", "").strip()
    country = request.form.get("country", "").strip()
    amount = request.form.get("amount", "").strip()
    term = request.form.get("term", "").strip()
    purpose = request.form.get("purpose", "").strip()
    if not name or not phone or not country or not amount:
        return "Fill all fields <a href='/apply-form'>Back</a>", 400
    with open("leads.csv", "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([datetime.now().isoformat(), name, phone, email, country, amount, term, purpose])
    cur = "ZMW"
    if country == "Zimbabwe":
        cur = "USD"
    if country == "Tanzania":
        cur = "TSh"
    msg = "New Zorak Loan Lead"
    msg = msg + NL + NL + "Name: " + name
    msg = msg + NL + "Phone: " + phone
    msg = msg + NL + "Email: " + email
    msg = msg + NL + "Country: " + country
    msg = msg + NL + "Amount: " + amount + " " + cur
    msg = msg + NL + "Term: " + term + " months"
    msg = msg + NL + "Purpose: " + purpose
    send_telegram(msg)
    t = "<h2>Thank you, " + name + "!</h2>"
    t = t + "<p>Amount: " + amount + " " + cur + "</p>"
    t = t + "<p>Purpose: " + purpose + "</p>"
    t = t + "<p>We will call you on " + phone + "</p>"
    return t
@app.route("/test-telegram")
def test():
    if not BOT_TOKEN:
        return "BOT_TOKEN MISSING"
    if not CHAT_ID:
        return "CHAT_ID MISSING"
    u = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
    r = requests.post(u, json={"chat_id": CHAT_ID, "text": "Test OK"}, timeout=10)
    return "Status: " + str(r.status_code)
@app.route("/health")
def health():
    return "OK"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
