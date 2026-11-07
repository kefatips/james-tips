from flask import Flask, request
import csv, os, requests, urllib.parse
from datetime import datetime

app = Flask(__name__)

WHATSAPP_LINK = 'https://wa.me/message/CFCJWLOZ7IWZK1'
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
# NEW - Add these in Render > Environment later
SHEET_WEBHOOK = os.environ.get('SHEET_WEBHOOK', '') # Google Apps Script URL
WHATSAPP_PHONE = os.environ.get('WHATSAPP_PHONE', '') # e.g 254720860503 no +
WHATSAPP_APIKEY = os.environ.get('WHATSAPP_APIKEY', '') # from CallMeBot

def send_to_telegram(text):
    if not BOT_TOKEN or not CHAT_ID:
        print('Telegram not configured')
        return False
    try:
        r = requests.post(
            'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage',
            json={'chat_id': CHAT_ID, 'text': text},
            timeout=10
        )
        print('Telegram status:', r.status_code)
        return r.status_code == 200
    except Exception as e:
        print('Telegram error:', e)
        return False

def send_to_sheet(data):
    if not SHEET_WEBHOOK:
        print('Sheet not configured')
        return False
    try:
        r = requests.post(SHEET_WEBHOOK, json=data, timeout=10)
        print('Sheet status:', r.status_code, r.text[:200])
        return True
    except Exception as e:
        print('Sheet error:', e)
        return False

def send_to_whatsapp(text):
    if not WHATSAPP_PHONE or not WHATSAPP_APIKEY:
        print('WhatsApp not configured')
        return False
    try:
        url = f"https://api.callmebot.com/whatsapp.php?phone={WHATSAPP_PHONE}&text={urllib.parse.quote(text)}&apikey={WHATSAPP_APIKEY}"
        r = requests.get(url, timeout=15)
        print('WhatsApp status:', r.status_code, r.text[:200])
        return True
    except Exception as e:
        print('WhatsApp error:', e)
        return False

HOME_HTML = '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zorak Loans - Fast Loans in Zambia, Zimbabwe & Tanzania</title>
<style>
* { box-sizing: border-box; font-family: 'Segoe UI', Arial, sans-serif; }
body { margin: 0; background: #f2f5f9; color:#111; }
.topbar { background:#0f2a1e; color:white; text-align:center; padding:8px; font-size:12px; }
.top { text-align: center; color: #0f7a55; font-size: 28px; font-weight: 900; padding: 14px 0 4px; }
.top span { color: #111; }
.tag { text-align:center; font-size:12px; color:#666; }
.card { max-width: 460px; margin: 16px auto; background: white; border-radius: 22px; padding: 22px 18px; box-shadow: 0 8px 30px rgba(0,0,0,0.08); }
.card h2 { text-align: center; margin: 0; font-size: 22px; line-height:1.3; }
.sub { text-align: center; font-size: 13px; color: #666; margin: 8px 0 16px; }
.badges { display:flex; gap:8px; justify-content:center; margin:10px 0; }
.badges span { background:#e8f5ee; color:#0f7a55; font-size:11px; font-weight:700; padding:6px 10px; border-radius:20px; }
.calc { background: #f8f9fb; border-radius: 16px; padding: 16px; }
.row { display: flex; justify-content: space-between; align-items: center; font-weight: bold; font-size: 14px; margin-top: 12px; }
.row b { color: #2563eb; }
input[type=range] { width: 100%; margin: 12px 0 4px; accent-color: #2563eb; }
.minmax { display: flex; justify-content: space-between; font-size: 12px; color: #999; }
.monthly { background: #eef4ff; border-radius: 14px; text-align: center; padding: 14px; margin-top: 16px; }
.monthly small { color: #666; font-size: 12px; }
.monthly div { color: #2563eb; font-size: 32px; font-weight: 900; margin-top: 4px; }
.btn { display: block; text-align: center; background: linear-gradient(90deg, #0f7a55, #2563eb); color: white; text-decoration: none; padding: 16px; border-radius: 30px; font-weight: 900; font-size: 16px; margin-top: 18px; }
.features { display: flex; justify-content: space-between; text-align: center; margin-top: 20px; gap:8px; }
.features div { flex: 1; font-size: 11px; color: #666; line-height: 1.4; background:#f8f9fb; padding:10px 4px; border-radius:12px; }
.features span { font-size: 26px; display: block; }
.testi { background:#fff8e1; border-radius:14px; padding:14px; margin-top:16px; font-size:13px; line-height:1.5; }
.testi b { color:#111; }
.faq { font-size:13px; color:#555; margin-top:14px; line-height:1.6; }
.faq b { color:#111; }
.footer { text-align: center; font-size: 12px; color: #aaa; margin: 15px 0 30px; }
select { width: 100%; padding: 12px; border-radius: 10px; border: 1px solid #ddd; margin-top: 12px; background: white; }
.wa2 { display: block; text-align: center; background: #25D366; color: white; text-decoration: none; padding: 14px; border-radius: 30px; font-weight: bold; margin-top: 12px; font-size: 14px; }
</style>
</head>
<body>
<div class="topbar">✅ Trusted by 2,400+ customers in Zambia • Zimbabwe • Tanzania | No hidden fees</div>
<div class="top">Zorak<span> Loans</span></div>
<div class="tag">Fast • Secure • Approved in 24 Hours</div>
<div class="card">
  <h2>Get Your Loan Approved Fast</h2>
  <div class="sub">Quick approval - Competitive rates from 8% - Flexible terms up to 60 months</div>
  <div class="badges"><span>⭐ 4.9/5 Rated</span><span>🔒 Bank-Level Secure</span><span>⚡ 24h Approval</span></div>
  <div class="calc">
    <div style="text-align:center; font-weight:bold;">Loan Calculator</div>
    <label style="display:block; margin-top:14px; font-size:13px; color:#555;">Country</label>
    <select id="country" onchange="
