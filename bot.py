import telebot, os, time, threading
from flask import Flask

BOT_TOKEN = os.environ.get("BOT_TOKEN") or "8816171451:AAF0747baP6QAEGYecRtWFw3OwjrJFaKi4Y"
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)
users = {}
PHOTO = "IMG-20260831-WA3113.jpg"

pkgs = {
    "1": "3+ ODDS - 500 KES",
    "2": "5+ ODDS - 1000 KES",
    "3": "10+ ODDS - 2000 KES",
    "4": "HT/FT + CORRECT SCORE - 3000 KES",
    "5": "JACKPOT 15 GAMES - 1500 KES"
}

@app.route('/')
def home(): return "Ecco Live!"

@bot.message_handler(commands=['start'])
def start(m):
    cid=m.chat.id
    users[cid]={"step":"name","name":"","last":time.time(),"nags":0}
    cap="🎮 WELCOME TO ECCO GAMES HUB 🎮\n\n👇 SEE MY WINNING TODAY 👇\n\nI sell 100% SURE betting tips daily! 💯\nNo lose, pure profit 🔥\n\n📲 Contact: @eccocashnobot\n💳 Till: 0738792626\n\nWhat's your name? 😊"
    try:
        if os.path.exists(PHOTO):
            bot.send_photo(cid, open(PHOTO,'rb'), caption=cap)
        else:
            bot.send_message(cid, cap)
    except:
        bot.send_message(cid, cap)

@bot.message_handler(func=lambda m: True)
def h(m):
    cid=m.chat.id
    if cid not in users: return
    users[cid]["last"]=time.time(); users[cid]["nags"]=0
    t=m.text.strip(); s=users[cid].get("step"); name=users[cid].get("name","bro")
    if s=="name":
        users[cid]["name"]=t; users[cid]["step"]="package"
        bot.send_message(cid, f"Nice {t}! 🤝 Choose package:\n\n1. 🔥 3+ ODDS - 500 KES\n2. 💰 5+ ODDS - 1000 KES\n3. 🚀 10+ ODDS - 2000 KES\n4. 👑 HT/FT + CORRECT SCORE - 3000 KES\n5. 🎯 JACKPOT 15 GAMES - 1500 KES\n\nType 1-5")
    elif s=="package":
        if t not in ["1","2","3","4","5"]: bot.send_message(cid,"Type 1-5 bro"); return
        users[cid]["package"]=t; users[cid]["step"]="paid"
        bot.send_message(cid, f"Perfect choice {name}! ✅\n\nYou selected: {pkgs[t]}\n\n💳 LIPA NA M-PESA:\nSend to: 0738792626\n📲 @eccocashnobot\n\nAfter paying, type PAID + CODE\nEx: PAID QGHI2345")
    elif s=="paid":
        if "PAID" in t.upper():
            users[cid]["step"]="verify"
            bot.send_message(cid, f"Sawa {name}! 🔍 Verifying... Forward M-PESA to @JamesTips 🎰")
        else: bot.send_message(cid, "Type PAID + CODE")
    elif s=="verify": bot.send_message(cid, "Received! Checking...")

def nag():
    while True:
        time.sleep(60); now=time.time()
        for cid,d in list(users.items()):
            diff=now-d.get("last",now); step=d.get("step"); nags=d.get("nags",0); name=d.get("name","my friend")
            try:
                if step=="name" and diff>180 and nags==0:
                    bot.send_message(cid, f"My friend! tell me your name so we can continue-"); users[cid]["nags"]=1
                elif step=="package" and diff>300 and nags<=1:
                    bot.send_message(cid, f"{name}, you there? Choose 1-5 🔥"); users[cid]["nags"]=2
                elif step=="paid" and diff>600 and nags<=2:
                    bot.send_message(cid, f"{name}, your games ready! Lipa 0738792626 and type PAID 🎯"); users[cid]["nags"]=3
                elif diff>3600 and nags==3:
                    bot.send_message(cid, f"I'm still waiting for your reply 😊 {name}"); users[cid]["nags"]=4
            except: pass

threading.Thread(target=nag, daemon=True).start()
def run(): bot.infinity_polling()
threading.Thread(target=run).start()
if __name__=="__main__": app.run(host="0.0.0.0", port=int(os.environ.get("PORT",10000)))
