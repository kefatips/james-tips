from flask import Flask, request
import csv, os, requests, urllib.parse
from datetime import datetime

app = Flask(__name__)

WHATSAPP_LINK = 'https://wa.me/message/CFCJWLOZ7IWZK1'
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
SHEET_WEBHOOK = os.environ.get('SHEET_WEBHOOK', '')
WHATSAPP_PHONE = os.environ.get('WHATSAPP_PHONE', '')
WHATSAPP_APIKEY = os.environ.get('WHATSAPP_APIKEY', '')

def send_to_telegram(text):
    if not BOT_TOKEN or not CHAT_ID:
        return False
    try:
        r = requests.post('https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage', json={'chat_id': CHAT_ID, 'text': text}, timeout=10)
        print('Telegram status:', r.status_code)
        return r.status_code == 200
    except Exception as e:
        print('Telegram error:', e)
        return False

def send_to_sheet(data):
    if not SHEET_WEBHOOK:
        return False
    try:
        r = requests.post(SHEET_WEBHOOK, json=data, timeout=10)
        print('Sheet status:', r.status_code)
        return True
    except Exception as e:
        print('Sheet error:', e)
        return False

def send_to_whatsapp(text):
    if not WHATSAPP_PHONE or not WHATSAPP_APIKEY:
        return False
    try:
        url = f"https://api.callmebot.com/whatsapp.php?phone={WHATSAPP_PHONE}&text={urllib.parse.quote(text)}&apikey={WHATSAPP_APIKEY}"
        r = requests.get(url, timeout=15)
        print('WhatsApp status:', r.status_code)
        return True
    except Exception as e:
        print('WhatsApp error:', e)
        return False

HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zorak Loans - Fast Loans</title>
<style>
* { box-sizing: border-box; font-family: Arial, sans-serif; }
body { margin: 0; background: #f2f5f9; color:#111; }
.topbar { background:#0f2a1e; color:white; text-align:center; padding:8px; font-size:12px; }
.top { text-align: center; color: #0f7a55; font-size: 28px; font-weight: 900; padding: 14px 0 4px; }
.top span { color: #111; }
.tag { text-align:center; font-size:12px; color:#666; }
.card { max-width: 460px; margin: 16px auto; background: white; border-radius: 22px; padding: 22px 18px; box-shadow: 0 8px 30px rgba(0,0,0,0.08); }
.card h2 { text-align: center; margin: 0; font-size: 22px; }
.sub { text-align: center; font-size: 13px; color: #666; margin: 8px 0 16px; }
.badges { display:flex; gap:8px; justify-content:center; margin:10px 0; }
.badges span { background:#e8f5ee; color:#0f7a55; font-size:11px; font-weight:700; padding:6px 10px; border-radius:20px; }
.calc { background: #f8f9fb; border-radius: 16px; padding: 16px; }
.row { display: flex; justify-content: space-between; font-weight: bold; font-size: 14px; margin-top: 12px; }
.row b { color: #2563eb; }
input[type=range] { width: 100%; margin: 12px 0 4px; accent-color: #2563eb; }
.minmax { display: flex; justify-content: space-between; font-size: 12px; color: #999; }
.monthly { background: #eef4ff; border-radius: 14px; text-align: center; padding: 14px; margin-top: 16px; }
.monthly small { color: #666; font-size: 12px; }
.monthly div { color: #2563eb; font-size: 32px; font-weight: 900; margin-top: 4px; }
.btn { display: block; text-align: center; background: linear-gradient(90
