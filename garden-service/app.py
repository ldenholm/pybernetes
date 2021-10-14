from flask import Flask
from flask import jsonify

app = Flask(__name__)

garden = [
  { 'description': 'lovely, lush', 'amount': 20 }
]

@app.route("/garden", )
def gardenjson():
    print('garden service request received')
    return jsonify(garden)

app.run()
# @app.route("/")
# def garden():
#     print('garden service request received')
#     return "garden service"