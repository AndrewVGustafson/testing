from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ok")
def home():
    return "wgdfdhshd"

if __name__ == "__main__":
    app.run(debug=True)