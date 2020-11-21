import requests
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config["SECRET KEY"] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

#Al ejecutar la funcion 'submit vote' extrae el resultado y ejecuta la funcion 'announce vote'
@socketio.on('submit vote')
def vote(data):
    selection = data["selection"]
    emit("announce vote", {'selection':selection}, broadcast=True)
