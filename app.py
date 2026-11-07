from flask import Flask, request
import csv, os, requests
from datetime import datetime

app = Flask(__name__)

WHATSAPP_LINK = 'https://wa.me/message/CFCJWLOZ7IWZK1'
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

def send_to_telegram(text):
    if not BOT_TOKEN or not CHAT_ID:
        print('Telegram not configured')
        return False
    try:
        r = requests.post(
            'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage',
            json={'chat_id': CHAT_ID, 'text': text},
            timeout=10
        )
        print('Telegram status:', r.status_code, r.text)
        return r.status_code == 200
    except Exception as e:
        print('Telegram error:', e)
        return False

HOME_HTML = '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zorak Loans</title>
<style>
* { box-sizing: border-box; font-family: Arial, sans-serif; }
body { margin: 0; background: #eef1f5; padding: 15px; }
.top { text-align: center; color: #0f7a55; font-size: 26px; font-weight: 900; padding: 10px 0 15px; }
.top span { color: #111; }
.card { max-width: 420px; margin: 0 auto; background: white; border-radius: 20px; padding: 22px 18px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }
.card h2 { text-align: center; margin: 0; font-size: 20px; }
.sub { text-align: center; font-size: 12px; color: #888; margin: 8px 0 20px; }
.calc { background: #f8f9fb; border-radius: 16px; padding: 16px; }
.row { display: flex; justify-content: space-between; align-items: center; font-weight: bold; font-size: 14px; margin-top: 12px; }
.row b { color: #2563eb; }
input[type=range] { width: 100%; margin: 12px 0 4px; accent-color: #2563eb; }
.minmax { display: flex; justify-content: space-between; font-size: 12px; color: #999; }
.monthly { background: #eef4ff; border-radius: 14px; text-align: center; padding: 14px; margin-top: 16px; }
.monthly small { color: #666; font-size: 12px; }
.monthly div { color: #2563eb; font-size: 30px; font-weight: 900; margin-top: 4px; }
.btn { display: block; text-align: center; background: linear-gradient(90deg, #2563eb, #7c3aed); color: white; text-decoration: none; padding: 15px; border-radius: 30px; font-weight: 900; font-size: 16px; margin-top: 18px; }
.features { display: flex; justify-content: space-between; text-align: center; margin-top: 20px; }
.features div { flex: 1; font-size: 11px; color: #666; line-height: 1.4; }
.features span { font-size: 28px; display: block; }
.footer { text-align: center; font-size: 12px; color: #aaa; margin-top: 15px; }
select { width: 100%; padding: 12px; border-radius: 10px; border: 1px solid #ddd; margin-top: 12px; background: white; }
.wa2 { display: block; text-align: center; background: #25D366; color: white; text-decoration: none; padding: 13px; border-radius: 30px; font-weight: bold; margin-top: 12px; font-size: 14px; }
</style>
</head>
<body>
<div class="top">Zorak<span> Loans</span></div>
<div class="card">
  <h2>Get Your Loan Approved Fast</h2>
  <div class="sub">Quick approval - Competitive rates - Flexible terms</div>
  <div class="calc">
    <div style="text-align:center; font-weight:bold;">Loan Calculator</div>
    <label style="display:block; margin-top:14px; font-size:13px; color:#555;">Country</label>
    <select id="country" onchange="updateAll()">
      <option value="Zimbabwe">Zimbabwe</option>
      <option value="Zambia">Zambia</option>
      <option value="Tanzania">Tanzania</option>
    </select>
    <div class="row"><span>Loan Amount</span><b id="amtLabel">$5,000</b></div>
    <input type="range" id="amount" min="100" max="5000" value="5000" step="100" oninput="updateAll()">
    <div class="minmax"><span id="minLabel">$100</span><span id="maxLabel">$5,000</span></div>
    <div class="row"><span>Loan Term</span><b id="termLabel">12 months</b></div>
    <input type="range" id="term" min="6" max="60" value="12" oninput="updateAll()">
    <div class="minmax"><span>6 months</span><span>60 months</span></div>
    <div class="monthly"><small>Monthly Payment</small><div id="monthly">$434.94</div></div>
  </div>
  <a class="btn" href="/apply-form" id="applyBtn">APPLY NOW</a>
  <a class="wa2" href="WHATSAPP_LINK_HERE">Chat on WhatsApp Instead</a>
  <div class="features">
    <div><span>Fast</span>Fast Approval<br>Within 24 hours</div>
    <div><span>Low</span>Low Rates<br>From 8%</div>
    <div><span>Safe</span>Secure<br>Bank-level</div>
  </div>
  <p style="text-align:center;font-size:12px;color:#888;margin-top:15px;">We will never ask for your PIN or OTP.</p>
</div>
<div class="footer">2026 Zorak Loans</div>
<script>
function updateAll() {
  var c = document.getElementById("country").value;
  var sym = "$";
  if (c == "Zambia") sym = "K";
  if (c == "Tanzania") sym = "TSh ";
  var amt = parseInt(document.getElementById("amount").value);
  var term = parseInt(document.getElementById("term").value);
  document.getElementById("amtLabel").innerText = sym + amt.toLocaleString();
  document.getElementById("minLabel").innerText = sym + "100";
  document.getElementById("maxLabel").innerText = sym + "5,000";
  document.getElementById("termLabel").innerText = term + " months";
  var r = 0.08 / 12;
  var monthly = amt * r / (1 - Math.pow(1 + r, -term));
  document.getElementById("monthly").innerText = sym + monthly.toFixed(2);
  document.getElementById("applyBtn").href = "/apply-form?amount=" + amt + "&country=" + c + "&term=" + term;
}
updateAll();
</script>
</body>
</html>
'''
HOME_HTML = HOME_HTML.replace('WHATSAPP_LINK_HERE', WHATSAPP_LINK)

FORM_HTML = '''
<!DOCTYPE html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Apply - Zorak Loans</title>
<style>
* { box-sizing: border-box; font-family: Arial, sans-serif; }
body { margin: 0; background: #eef1f5; padding: 15px; }
.card { max-width: 420px; margin: 0 auto; background: white; border-radius: 20px; padding: 22px; }
h2 { text-align: center; margin: 0; }
p { text-align: center; color: #888; font-size: 13px; }
label { display: block; margin-top: 15px; font-size: 13px; font-weight: bold; }
input, select { width: 100%; padding: 13px; border: 1px solid #ddd; border-radius: 10px; margin-top: 6px; font-size: 15px; }
.btn { width: 100%; background: linear-gradient(90deg, #2563eb, #7c3aed); color: white; border: none; padding: 15px; border-radius: 30px; font-weight: 900; margin-top: 20px; font-size: 16px; cursor: pointer; }
.wa { display: block; text-align: center; background: #25D366; color: white; text-decoration: none; padding: 13px; border-radius: 30px; font-weight: bold; margin-top: 12px; }
</style>
</head>
<body>
<div class="card">
<h2>Apply Now</h2>
<p>We will call you back. We never ask for PIN or OTP.</p>
<form method="POST" action="/apply">
<label>Full Name</label><input name="name" required placeholder="Full name">
<label>Phone Number</label><input name="phone" required placeholder="+260 / +263 / +255">
<label>Email (Optional)</label><input name="email" type="email" placeholder="you@gmail.com">
<label>Country</label>
<select name="country" required>
<option value="">Select Country</option>
<option value="Zambia">Zambia</option>
<option value="Zimbabwe">Zimbabwe</option>
<option value="Tanzania">Tanzania</option>
</select>
<label>Loan Amount</label><input name="amount" id="amountInput" type="number" required placeholder="Enter amount">
<label>Loan Term (months)</label><input name="term" id="termInput" type="number" value="12">
<label><input type="checkbox" required style="width:auto;"> I agree to be contacted about my application</label>
<button class="btn">SUBMIT APPLICATION</button>
</form>
<a class="wa" href="WHATSAPP_LINK_HERE">Chat on WhatsApp Instead</a>
<br><a href="/" style="display:block;text-align:center;">Back to Calculator</a>
</div>
<script>
var p = new URLSearchParams(window.location.search);
if (p.get("amount")) document.getElementById("amountInput").value = p.get("amount");
if (p.get("term")) document.getElementById("termInput").value = p.get("term");
if (p.get("country")) { document.querySelector("select[name=country]").value = p.get("country"); }
</script>
</body>
</html>
'''
FORM_HTML = FORM_HTML.replace('WHATSAPP_LINK_HERE', WHATSAPP_LINK)

@app.route('/')
@app.route('/api')
def home():
    return HOME_HTML

@app.route('/apply-form')
def apply_form():
    return FORM_HTML

@app.route('/apply', methods=['POST'])
@app.route('/api/apply', methods=['POST'])
def apply():
    name = request.form.get('name', '').strip()
    phone = request.form.get('phone', '').strip()
    email = request.form.get('email', '').strip()
    country = request.form.get('country', '').strip()
    amount = request.form.get('amount', '').strip()
    term = request.form.get('term', '').strip()
    if not name or not phone or not country or not amount:
        return 'Please fill all required fields. <a href="/apply-form">Go back</a>', 400
    with open('leads.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), name, phone, email, country, amount, term])
    currency = 'ZMW' if country == 'Zambia' else 'USD' if country == 'Zimbabwe' else 'TSh'
    msg = 'New Zorak Loan Lead\n\nName: ' + name + '\nPhone: ' + phone + '\nEmail: ' + email + '\nCountry: ' + country + '\nAmount: ' + amount + ' ' + currency + '\nTerm: ' + term + ' months'
    send_to_telegram(msg)
    return '<div style="max-width:420px;margin:40px auto;font-family:Arial;text-align:center;padding:20px;background:white;border-radius:20px;"><h2 style="color:#2563eb;">Thank you, ' + name + '!</h2><p>Your application for ' + amount + ' ' + currency + ' for ' + term + ' months was received.</p><p>We will call you on ' + phone + '.</p><a href="' + WHATSAPP_LINK + '" style="display:block;background:#25D366;color:white;padding:14px;border-radius:30px;text-decoration:none;font-weight:bold;">Chat on WhatsApp</a><br><a href="/">Back to Calculator</a></div>'

@app.route('/test-telegram')
def test_telegram():
    if not BOT_TOKEN:
        return 'BOT_TOKEN is MISSING in Render. Go to Environment and add it.'
    if not CHAT_ID:
        return 'CHAT_ID is MISSING in Render. Go to Environment and add it.'
    url = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage'
    r = requests.post(url, json={'chat_id': CHAT_ID, 'text': 'Test from Zorak app - if you see this, Telegram is working!'}, timeout=10)
    return 'Status: ' + str(r.status_code) + '<br>Telegram says: ' + r.text + '<br>CHAT_ID: ' + CHAT_ID

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
