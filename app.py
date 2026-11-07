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
        r = requests.post(
            'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage',
            json={'chat_id': CHAT_ID, 'text': text},
            timeout=10
        )
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
.card { max-width: 420px; margin: 0 auto; background: white; border-radius: 20px; padding: 22px 18px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }
.card h2 { text-align: center; margin: 0; font-size: 20px; }
.sub { text-align: center; font-size: 12px; color: #888; margin: 8px 0 20px; }
.calc { background: #f8f9fb; border-radius: 16px; padding: 16px; }
.row { display: flex; justify-content: space-between; align-items: center; font-weight: bold; font-size: 14px; margin-top: 12px;')
def test_telegram():
    if not BOT_TOKEN:
        return 'BOT_TOKEN is MISSING in Render. Go to Environment and add it.'
    if not CHAT_ID:
        return 'CHAT_ID is MISSING in Render. Go to Environment and add it.'
    url = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage'
    r = requests.post(url, json={'chat_id': CHAT_ID, 'text': 'Test from Zorak app - if you see this, Telegram is working!'}, timeout=10)
    return 'Status: ' + str(r.status_code) + '<br>Telegram says: ' + r.text + '<br>CHAT_ID: ' + CHAT_ID

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
