from flask import Flask
from flask import jsonify
from flask.helpers import make_response

app = Flask(__name__)

garden = [
  { 'description': 'lovely, lush', 'amount': 20 }
]

@app.route('/garden', )
def gardenjson():
    print('garden service request received')
    response = make_response(jsonify(garden), 200)
    response.mimetype = 'application/json'
    return response

@app.route('/')
def home():
    print('home req received')
    response = make_response("home works\n", 200)
    response.mimetype = "text/plain"
    return response