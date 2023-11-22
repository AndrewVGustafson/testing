from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/ok")
def home():
    return "wgdfdhshd"

@app.route("/<name>")
def name(name):
    
    return f"fjisjfioaj ifo {name} fsfsd {name*5}"


if __name__ == "__main__":
    app.run(debug=True)