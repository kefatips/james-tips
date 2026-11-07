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
@app.route("/")
@app.route("/api")
def home():
    t = ""
    t = t + "<h1>Zorak Loans</h1>"
    t = t + "<p>Country: <select id=c>"
    t = t + "<option>Zambia</option>"
    t = t + "<option>Zimbabwe</option>"
    t = t + "<option>Tanzania</option>"
    t = t + "<option>Ghana</option>"
    t = t + "</select></p>"
    t = t + "<p>Amount: <input id=a value=5000></p>"
    t = t + "<p>Term: <input id=n value=12></p>"
    t = t + "<p>Monthly: <b id=m></b></p>"
    t = t + "<button onclick=calc()>"
    t = t + "Calculate</button>"
    t = t + "<p><a href=/apply-form>"
    t = t + "APPLY NOW</a></p>"
    t = t + "<p><a href=" + WA + ">"
    t = t + "WhatsApp</a></p>"
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
    t = t + "<h1>Apply Now</h1>"
    t = t + "<form method=POST action=/apply>"
    t = t + "<p>Name: <input name=name required></p>"
    t = t + "<p>Phone: <input name=phone required></p>"
    t = t + "<p>Email: <input name=email></p>"
    t = t + "<p>Country: <select name=country>"
    t = t + "<option>Zambia</option>"
    t = t + "<option>Zimbabwe</option>"
    t = t + "<option>Tanzania</option>"
    t = t + "<option>Ghana</option>"
    t = t + "</select></p>"
    t = t + "<p>Amount: <input name=amount required></p>"
    t = t + "<p>Term: <input name=term value=12></p>"
    t = t + "<p>Purpose: <select name=purpose>"
