import os
from flask import Flask, request

app = Flask(__name__)

USERNAME = os.getenv("USERNAME", "jani")
PASSWORD = os.getenv("PASSWORD", "jani2025")

@app.route("/", methods=["GET"])
def home():
    return open("index.html", encoding="utf-8").read()

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == USERNAME and password == PASSWORD:
        return f"<h2>Szia, {USERNAME.capitalize()}! Sikeres bejelentkezés.</h2>"
    else:
        return "<h2>Hibás felhasználónév vagy jelszó!</h2>", 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
