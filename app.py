from flask import Flask, request
import csv, os, requests
from datetime import datetime
app = Flask(__name__)
NL = chr(10)
WA = "https://wa.me/message/"
WA = WA + "CFCJWLOZ7IWZK1"
BOT = os.environ.get("BOT_TOKEN")
CHAT = os.environ.get("CHAT_ID")
def send_t(t):
    if not BOT:
        return False
    if not CHAT:
        return False
    try:
        u = "https://api.telegram.org/bot"
        u = u + BOT + "/sendMessage"
        d = {"chat_id": CHAT, "text": t}
        r = requests.post(u, json=d, timeout=10)
        return r.status_code == 200
    except:
        return False
def style():
    s = ""
    s = s + "<style>"
    s = s + "body{margin:0;font-family:Arial;"
    s = s + "background:#f2f7f2;color:#111}"
    s = s + ".top{background:#0a5c36;color:#fff;"
    s = s + "padding:18px;text-align:center}"
    s = s + ".top b{font-size:24px;letter-spacing:1px}"
    s = s + ".top span{color:#ffc107}"
    s = s + ".wrap{max-width:520px;margin:16px auto;"
    s = s + "padding:0 14px}"
    s = s + ".card{background:#fff;border-radius:16px;"
    s = s + "padding:20px;box-shadow:0 4px 20px #0001}"
    s = s + "h1{margin:0 0 6px;font-size:26px}"
    s = s + "p{margin:10px 0}"
    s = s + "input,select{width:100%;padding:12px;"
    s = s + "border:1px solid #ddd;border-radius:10px;"
    s = s + "box-sizing:border-box;font-size:16px}"
    s = s + ".btn{display:block;text-align:center;"
    s = s + "background:#0a5c36;color:#fff;padding:14px;"
    s = s + "border-radius:12px;text-decoration:none;"
    s = s + "font-weight:bold;border:0;width:100%;"
    s = s + "font-size:17px;cursor:pointer}"
    s = s + ".btn2{background:#ffc107;color:#111}"
    s = s + ".row{display:flex;gap:10px}"
    s = s + ".row div{flex:1}"
    s = s + ".pill{display:inline-block;background:#e8f5ee;"
    s = s + "padding:6px 10px;border-radius:20px;"
    s = s + "font-size:13px;margin:2px}"
    s = s + ".big{font-size:28px;font-weight:bold;"
    s = s + "color:#0a5c36}"
    s = s + ".muted{color:#666;font-size:14px}"
    s = s + "</style>"
    return s
def top():
    t = ""
    t = t + "<div class=top>"
    t = t + "<b>ZORAK <span>LOANS</span></b>"
    t = t + "<div class=muted style=color:#d8eedd>"
    t = t + "Fast Loans - Zambia | Zimbabwe"
    t = t + " | Tanzania | Ghana</div></div>"
    return t
@app.route("/")
@app.route("/api")
def home():
    t = ""
    t = t + style()
    t = t + top()
    t = t + "<div class=wrap><div class=card>"
    t = t + "<h1>Need cash today?</h1>"
    t = t + "<p class=muted>Apply in 2 mins."
    t = t + " Get answer on WhatsApp.</p>"
    t = t + "<span class=pill>✅ No paperwork</span>"
    t = t + "<span class=pill>⚡ Same day</span>"
    t = t + "<span class=pill>🔒 Safe</span>"
    t = t + "<p>Country</p>"
    t = t + "<select id=c>"
    t = t + "<option>Zambia</option>"
    t = t + "<option>Zimbabwe</option>"
    t = t + "<option>Tanzania</option>"
    t = t + "<option>Ghana</option>"
    t = t + "</select>"
    t = t + "<div class=row><div>"
    t = t + "<p>Amount</p>"
    t = t + "<input id=a value=5000>"
    t = t + "</div><div>"
    t = t + "<p>Term (months)</p>"
    t = t + "<input id=n value=12>"
    t = t + "</div></div>"
    t = t + "<p>Your Monthly Payment</p>"
    t = t + "<div class=big id=m></div>"
    t = t + "<p class=muted>8% interest."
    t = t + " Example only.</p>"
    t = t + "<button class=btn onclick=calc()>"
    t = t + "Calculate</button><br>"
    t = t + "<a class='btn btn2' href=/apply-form>"
    t = t + "APPLY NOW →</a><br>"
    t = t + "<a class=btn href=" + WA + ">"
    t = t + "Chat on WhatsApp</a>"
    t = t + "</div><br><div class=card>"
    t = t + "<h3>How it works</h3>"
    t = t + "<p>1. Fill form - 2 mins</p>"
    t = t + "<p>2. We call you - 30 mins</p>"
    t = t + "<p>3. Cash in your account</p>"
    t = t + "</div></div>"
    t = t + "<script>function calc(){"
    t = t + "var a=document.getElementById('a').value;"
    t = t + "var n=document.getElementById('n').value;"
    t = t + "var r=0.08/12;"
    t = t + "var m=a*r/(1-Math.pow(1+r,-n));"
    t = t + "document.getElementById('m')"
    t = t + ".innerText=m.toFixed(2)}"
    t = t + "calc()</script>"
    return t
@app.route("/apply-form")
@app.route("/api/apply-form")
def form():
    t = ""
    t = t + style()
    t = t + top()
    t = t + "<div class=wrap><div class=card>"
    t = t + "<h1>Apply Now</h1>"
    t = t + "<p class=muted>2 mins. No fees to apply.</p>"
    t = t + "<form method=POST action=/apply>"
    t = t + "<p>Full Name</p>"
    t = t + "<input name=name required placeholder='John Banda'>"
    t = t + "<p>Phone / WhatsApp</p>"
    t = t + "<input name=phone required placeholder='+260...'>"
    t = t + "<p>Email (optional)</p>"
    t = t + "<input name=email placeholder='you@mail.com'>"
    t = t + "<p>Country</p>"
    t = t + "<select name=country>"
    t = t + "<option>Zambia</option>"
    t = t + "<option>Zimbabwe</option>"
    t = t + "<option>Tanzania</option>"
    t = t + "<option>Ghana</option>"
    t = t + "</select>"
    t = t + "<div class=row><div>"
    t = t + "<p>Amount</p>"
    t = t + "<input name=amount required value=5000>"
    t = t + "</div><div>"
    t = t + "<p>Term</p>"
    t = t + "<input name=term value=12>"
    t = t + "</div></div>"
    t = t + "<p>Purpose</p>"
    t = t + "<select name=purpose>"
    t = t + "<option>Business</option>"
    t = t + "<option>School Fees</option>"
    t = t + "<option>Medical</option>"
    t = t + "<option>Rent</option>"
    t = t + "<option>Other</option>"
    t = t + "</select><br><br>"
    t = t + "<button class=btn>SUBMIT APPLICATION</button>"
    t = t + "</form><br>"
    t = t + "<a class=btn href=" + WA + ">"
    t = t + "WhatsApp Instead</a>"
    t = t + "</div></div>"
    return t
@app.route("/apply", methods=["POST"])
@app.route("/api/apply", methods=["POST"])
def apply():
    n = request.form.get("name", "")
    p = request.form.get("phone", "")
    e = request.form.get("email", "")
    c = request.form.get("country", "")
    a = request.form.get("amount", "")
    tm = request.form.get("term", "")
    pu = request.form.get("purpose", "")
    if not n:
        return "Fill name", 400
    if not p:
        return "Fill phone", 400
    if not a:
        return "Fill amount", 400
    with open("leads.csv", "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([datetime.now().isoformat(), n, p, e, c, a, tm, pu])
    cur = "ZMW"
    if c == "Zimbabwe":
        cur = "USD"
    if c == "Tanzania":
        cur = "TSh"
    if c == "Ghana":
        cur = "GHS"
    m = "New Zorak Lead" + NL
    m = m + "Name: " + n + NL
    m = m + "Phone: " + p + NL
    m = m + "Country: " + c + NL
    m = m + "Amount: " + a + " " + cur + NL
    m = m + "Term: " + tm + NL
    m = m + "Purpose: " + pu
    send_t(m)
    t = ""
    t = t + style()
    t = t + top()
    t = t + "<div class=wrap>
