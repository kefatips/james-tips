from flask import Flask, request
import csv, os, requests
from datetime import datetime
app = Flask(__name__)
NL = chr(10)
WA = "https://wa.me/message/CFCJWLOZ7IWZK1"
BOT = os.environ.get("BOT_TOKEN")
CHAT = os.environ.get("CHAT_ID")
def send_t(t):
    if not BOT or not CHAT:
        return False
    try:
        u = "https://api.telegram.org/bot"
        u = u + BOT + "/sendMessage"
        r = requests.post(u, json={"chat_id": CHAT, "text": t}, timeout=10)
        return r.status_code == 200
    except:
        return False
@app.route("/")
@app.route("/api")
def home():
    return "<h1>Zorak Loans</h1><p>Country: <select id=c><option>Zimbabwe</option><option>Zambia</option><option>Tanzania</option><option>Ghana</option></select></p><p>Amount: <input id=a type=number value=5000></p><p>Term: <input id=t type=number value=12> months</p><p>Monthly: <b id=m></b></p><button onclick=calc()>Calculate</button><p><a href=/apply-form>APPLY NOW</a></p><p><a href=" + WA + ">WhatsApp</a></p><script>function calc(){var a=document.getElementById('a').value;var t=document.getElementById('t').value;var r=0.08/12;var m=a*r/(1-Math.pow(1+r,-t));document.getElementById('m').innerText=m.toFixed(2)}calc()</script>"
@app.route("/apply-form")
@app.route("/api/apply-form")
def form():
    return "<h1>Apply Now</h1><form method=POST action=/apply><p>Name: <input name=name required></p><p>Phone: <input name=phone required></p><p>Email: <input name=email></p><p>Country: <select name=country required><option>Zambia</option><option>Zimbabwe</option><option>Tanzania</option><option>Ghana</option></select></p><p>Amount: <input name=amount type=number required></p><p>Term: <input name=term type=number value=12></p><p>Purpose: <select name=purpose><option>Business</option><option>School Fees</option><option>Medical</option><option>Rent</option><option>Other</option></select></p><button>SUBMIT</button></form><p><a href=" + WA + ">WhatsApp Instead</a></p>"
@app.route("/apply", methods=["POST"])
@app.route("/api/apply", methods=["POST"])
def apply():
    n = request.form.get("name", "")
    p = request.form.get("phone", "")
    e = request.form.get("email", "")
    c =untry'))"
    h = h + "document."
    h = h + "getElement"
    h = h + "ById('cSel')"
    h = h + ".value=p.get('country');"
    h = h + "</script></body></html>"
    return h
@app.route("/apply", methods=["POST"])
@app.route("/api/apply", methods=["POST"])
def apply():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    email = request.form.get("email", "").strip()
    country = request.form.get("country", "").strip()
    amount = request.form.get("amount", "").strip()
    term = request.form.get("term", "").strip()
    purpose = request.form.get("purpose", "").strip()
    if not name or not phone or not country or not amount:
        return "Fill all fields", 400
    with open("leads.csv", "a", newline="") as f:
        w = csv.writer(f)
        d = datetime.now().isoformat()
        row = [d, name, phone]
        row = row + [email, country]
        row = row + [amount, term]
        row = row + [purpose]
        w.writerow(row)
    cur = "ZMW"
    if country == "Zimbabwe":
        cur = "USD"
    if country == "Tanzania":
        cur = "TSh"
    if country == "Ghana":
        cur = "GHS"
    msg = "New Zorak Loan Lead"
    msg = msg + NL + NL + "Name: " + name
    msg = msg + NL + "Phone: " + phone
    msg = msg + NL + "Email: " + email
    msg = msg + NL + "Country: " + country
    msg = msg + NL + "Amount: " + amount + " " + cur
    msg = msg + NL + "Term: " + term + " months"
    msg = msg + NL + "Purpose: " + purpose
    send_t(msg)
    t = "<!DOCTYPE html><html><head>"
    t = t + "<meta name='viewport'"
    t = t + " content='width=device-width,"
    t = t + " initial-scale=1'>"
    t = t + "<style>body{margin:0;"
    t = t + "background:#eef1f5;"
    t = t + "padding:15px;"
    t = t + "font-"
    t = t + "family:Arial}"
    t = t + ".card{max-width:420px;"
    t = t + "margin:40px auto;"
    t = t + "background:white;"
    t = t + "border-radius:20px;"
    t = t + "padding:30px;"
    t = t + "text-align:center}"
    t = t + ".btn{display:block;"
    t = t + "background:#2563eb;"
    t = t + "color:white;"
    t = t + "text-decoration:none;"
    t = t + "padding:15px;"
    t = t + "border-radius:30px;"
    t = t + "font-weight:900;"
    t = t + "margin-top:20px}"
    t = t + "</style></head><body>"
    t = t + "<div class='card'>"
    t = t + "<h2>Thank you, " + name + "!</h2>"
    t = t + "<p>Amount: " + amount + " " + cur + "</p>"
    t = t + "<p>Purpose: " + purpose + "</p>"
    t = t + "<p>We will call you on " + phone + "</p>"
    t = t + "<a class='btn' href='/'>"
    t = t + "Apply Another</a>"
    t = t + "</div></body></html>"
    return t
@app.route("/test-telegram")
@app.route("/api/test-telegram")
def test():
    if not BOT:
        return "BOT_TOKEN MISSING"
    if not CHAT:
        return "CHAT_ID MISSING"
    u = "https://api.telegram.org/bot" + BOT + "/sendMessage"
    r = requests.post(u, json={"chat_id": CHAT, "text": "Test OK"}, timeout=10)
    return "Status: " + str(r.status_code)
@app.route("/health")
@app.route("/api/health")
def health():
    return "OK"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
