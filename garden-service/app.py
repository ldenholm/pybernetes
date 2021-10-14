from flask import Flask
from flask import jsonify

app = Flask(__name__)

garden = {"lush", "green", "fountains"}

@app.route("/garden")
def get_garden():
    return jsonify(garden)

@app.route("/")
def garden():
    print('garden service request received')
    return "garden service"