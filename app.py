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
    h = "<h1>Zorak Loans</h1>"
    h = h + "<p>Fast loans in Zambia, Zimbabwe, Tanzania</p>"
    h = h + "<p>From 8 percent, approved in 24 hours</p>"
    h = h + "<a href='/apply-form'>APPLY NOW</a><br><br>"
    h = h + "<a href='" + WHATSAPP_LINK + "'>Chat on WhatsApp</a>"
    h = h + "<p>We never ask for PIN or OTP.</p>"
    return h
@app.route("/apply-form")
def form():
    h = "<h2>Apply Now</h2>"
    h = h + "<form method='POST' action='/apply'>"
    h = h + "Name<br><input name='name' required><br><br>"
    h = h + "Phone<br><input name='phone' required><br><br>"
    h = h + "Email<br><input name='email'><br><br>"
    h = h + "Country<br><select name='country' required>"
    h = h + "<option value=''>Select</option>"
    h = h + "<option>Zambia</option>"
    h = h + "<option>Zimbabwe</option>"
    h = h + "<option>Tanzania</option></select><br><br>"
    h = h + "Amount<br><input name='amount' required><br><br>"
    h = h + "Term months<br><input name='term' value='12'><br><br>"
    h = h + "Purpose of Loan<br><select name='purpose' required>"
    h = h + "<option value=''>Select Purpose</option>"
    h = h + "<option>Business</option>"
    h = h + "<option>School Fees</option>"
    h = h + "<option>Medical</option>"
    h = h + "<option>Rent</option>"
    h = h + "<option>Agriculture</option>"
    h = h + "<option>Car</option>"
    h = h + "<option>Personal</option>"
    h = h + "<option>Other</option></select><br><br>"
    h = h + "<button>SUBMIT</button></form>"
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
    msg = "New
