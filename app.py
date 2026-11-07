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
        u = "https://api.telegram.org/bot" + BOT + "/sendMessage"
        r = requests.post(u, json={"chat_id": CHAT, "text": t}, timeout=10)
        return r.status_code == 200
    except Exception as e:
        print(e)
        return False
@app.route("/")
@app.route("/api")
def home():
    h = """<!DOCTYPE html><html><head>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<title>Zorak Loans</title>
<style>
body{margin:0;background:#eef1f5;padding:15px;font-family:Arial}
.top{text-align:center;color:#0f7a55;font-size:26px;font-weight:900}
.card{max-width:420px;margin:auto;background:white;border-radius:20px;padding:22px 18px}
.btn{display:block;text-align:center;background:#2563eb;color:white;text-decoration:none;padding:15px;border-radius:30px;font-weight:900}
.wa2{display:block;text-align:center;background:#25D366;color:white;text-decoration:none;padding:13px;border-radius:30px;font-weight:bold;margin-top:12px}
.calc{background:#f8f9fb;border-radius:16px;padding:16px}
.monthly{background:#eef4ff;border-radius:
