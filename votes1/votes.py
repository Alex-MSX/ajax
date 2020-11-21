import requests
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config["SECRET KEY"] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
socketio = SocketIO(app)

votes = {"yes":0, "no":0, "maybe":0}

@app.route("/")
def index():
    return render_template("index.html", votes=votes)

#Al ejecutar la funcion 'submit vote' extrae el resultado y ejecuta la funcion 'vote totals' en js
@socketio.on('submit vote')
def vote(data):
    selection = data["selection"]
    votes[selection] += 1
    emit("vote totals", votes, broadcast=True)
