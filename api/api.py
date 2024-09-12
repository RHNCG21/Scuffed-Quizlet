import json
from flask import Flask, jsonify, request
app = Flask(__name__)

data = {"hello": "world"}

@app.route('/data', methods=['GET'])
def get_employees():
 return jsonify(data)

if __name__ == '__main__':
   app.run(port=5000)