import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():


    currency = request.form.get('currency')
    res = requests.get('https://api.currencyfreaks.com/latest?apikey=999e8884fae64452b2c7952c67cb5603')


    if res.status_code != 200:
        return jsonify({"success": False})


    data = res.json()
    if currency not in data["rates"]:
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][currency]})
