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
    h = h + "body{margin:0;"
    h = h + "background:#eef1f5;"
    h = h + "padding:15px;"
    h = h + "font-"
    h = h + "family:Arial}"
    h = h + ".top{text-align:center;"
    h = h + "color:#0f7a55;"
    h = h + "font-size:26px;"
    h = h + "font-weight:900}"
    h = h + ".card{max-width:420px;"
    h = h + "margin:auto;"
    h = h + "background:white;"
    h = h + "border-radius:20px;"
    h = h + "padding:22px 18px}"
    h = h + ".btn{display:block;"
    h = h + "text-align:center;"
    h = h + "background:#2563eb;"
    h = h + "color:white;"
    h = h + "text-decoration:none;"
    h = h + "padding:15px;"
    h = h + "border-radius:30px;"
    h = h + "font-weight:900}"
    h = h + ".wa2{display:block;"
    h = h + "text-align:center;"
    h = h + "background:#25D366;"
    h = h + "color:white;"
    h = h + "text-decoration:none;"
    h = h + "padding:13px;"
    h = h + "border-radius:30px;"
    h = h + "font-weight:bold;"
    h = h + "margin-top:12px}"
    h = h + ".calc{background:#f8f9fb;"
    h = h + "border-radius:16px;"
    h = h + "padding:16px}"
    h = h + ".monthly{background:#eef4ff;"
    h = h + "border-radius:14px;"
    h = h + "text-align:center;"
    h = h + "padding:14px;"
    h = h + "margin-top:16px}"
    h = h + ".monthly div{color:#2563eb;"
    h = h + "font-size:30px;"
    h = h + "font-weight:900}"
    h = h + "select{width:100%;"
    h = h + "padding:12px;"
    h = h + "
