import json
from flask import Flask, jsonify, request
import os

app = Flask(__name__)
token = os.getenv('TOKEN')
# Initialize global_data outside the function
global_data = {"hello": "world"}

@app.route('/data', methods=['GET', 'POST'])
def get_data():
    auth_key = request.headers.get('Authorization')
    if auth_key == token:
        if request.method == 'POST':
            data = request.get_json()
            # Append new data to the global_data dictionary
            global global_data
            global_data.update(data)
            return jsonify({"message": "data appended successfully"})
        else:
            return jsonify(global_data)  # Return the current global_data
    else:
        return jsonify({"error": "Unauthorized"}), 401

if __name__ == '__main__':
    app.run()