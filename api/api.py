import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        data = request.get_json()  # get the data from the request body
        # do something with the data here, e.g.,
        print(data)
        return jsonify({"message": "data received successfully"})
    else:
        return jsonify({"hello": "world"})

if __name__ == '__main__':
    app.run()