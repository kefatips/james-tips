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
@app.route("/api")
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
    h = h + "
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
