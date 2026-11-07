from flask import Flask, request, render_template_string
import csv, os, requests
from datetime import datetime

app = Flask(__name__)

WHATSAPP_LINK = "https://wa.me/message/CFCJWLOZ7IWZK1"
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_to_telegram(text):
    if not BOT_TOKEN or not CHAT_ID:
        print("Telegram not configured")
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": text},
            timeout=10
        )
    except Exception as e:
        print("Telegram error:", e)

FORM_HTML = f"""
<h2>Zorak Loan Application</h2>
<p>Fill this form and we will call you back. We will never ask for your PIN or OTP.</p>
<form method="POST" action="/apply">
  Full Name: <br><input name="name" required><br><br>
  Phone: <br><input name="phone" placeholder="+260 / +263 / +255" required><br><br>
  Email: <br><input name="email" type="email"><br><br>
  Country: <br>
  <select name="country" id="country" onchange="updateCurrency()" required>
    <option value="">Select Country</option>
    <option value="Zambia">Zambia</option>
    <option value="Zimbabwe">Zimbabwe</option>
    <option value="Tanzania">Tanzania</option>
  </select><br><br>
  Loan Amount <span id="currencyLabel">(Select country first)</span>: <br>
  <input name="amount" type="number" required><br><br>
  <label><input type="checkbox" required> I agree to be contacted about my application.</label><br><br>
  <button type="submit">Submit Application</button>
</form>
<br>
<a href="{WHATSAPP_LINK}" target="_blank"><button>Chat on WhatsApp Instead</button></a>
<script>
function updateCurrency() {{
  var c = document.getElementById("country").value;
  var label = document.getElementById("currencyLabel");
  if (c == "Zambia") label.innerText = "(Kwacha - ZMW)";
  else if (c == "Zimbabwe") label.innerText = "(USD - $)";
  else if (c == "Tanzania") label.innerText = "(Shilling - TSh)";
  else label.innerText = "(Select country first)";
}}
</script>
"""

@app.route("/")
@app.route("/api")
def home():
    return render_template_string(FORM_HTML)

@app.route("/apply", methods=["POST"])
@app.route("/api/apply", methods=["POST"])
def apply():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    email = request.form.get("email", "").strip()
    country = request.form.get("country", "").strip()
    amount = request.form.get("amount", "").strip()

    if not name or not phone or not country or not amount:
        return "Please fill all required fields. <a href='/'>Go back</a>", 400

    with open("leads.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), name, phone, email, country, amount])

    currency = "ZMW" if country == "Zambia" else "USD" if country == "Zimbabwe" else "TSh"
    msg = f"New Zorak Loan Lead\n\nName: {name}\nPhone: {phone}\nEmail: {email}\nCountry: {country}\nAmount: {amount} {currency}"
    send_to_telegram(msg)

    return f"""
    <h2>Thank you, {name}!</h2>
    <p>Your application for {amount} {currency} was received.</p>
    <p>We will call you on {phone} to continue. Please do not share your PIN or OTP with anyone.</p>
    <p><a href="{WHATSAPP_LINK}">Click here to chat to us on WhatsApp</a></p>
    <a href="/">Back to form</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
