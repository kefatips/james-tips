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
    h
