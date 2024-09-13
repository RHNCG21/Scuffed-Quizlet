import json
from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Get the token from environment variables
token = os.getenv('TOKEN')

# Initialize global_data outside the function
global_data = {"hello": "world"}

@app.route('/data', methods=['GET', 'POST'])
def get_data():
    # Extract the Authorization header
    auth_key = request.headers.get('Authorization')

    # Check if the token matches
    if auth_key == f"Bearer {token}":  # Using Bearer token for standardization
        if request.method == 'POST':
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"}), 400

            # Append new data to the global_data dictionary
            global global_data
            global_data.update(data)
            return jsonify({"message": "data appended successfully"})
        else:
            return jsonify(global_data)  # Return the current global_data
    else:
        return jsonify({"error": "Unauthorized"}), 401

if __name__ == '__main__':
    if token is None:
        raise ValueError("No TOKEN environment variable set. Please set it before running the app.")
    app.run()