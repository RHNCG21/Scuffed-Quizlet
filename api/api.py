import json
from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
token = os.getenv('TOKEN')
print(token)

DATA_FILE = 'data.json'
if os.path.exists(DATA_FILE):
    print("Data file found")
else:
    with open(DATA_FILE, 'w') as file:
        json.dump({}, file)

def load_data():
    """Load data from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {"Error": "No file found"}

def save_data(data):
    """Save data to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

@app.route('/data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        auth_key = request.headers.get('Authorization')
        if auth_key == "Bearer " + token:
            data = request.get_json()
            # Load current data from file
            current_data = load_data()
            # Update data with new values
            current_data.update(data)
            # Save updated data back to file
            save_data(current_data)
            return jsonify({"message": "data appended successfully"})
        else:
            return jsonify({"error": "Unauthorized"}), 401
    else:  # For GET requests
        # Return the current data from file
        current_data = load_data()
        return jsonify(current_data)

if __name__ == '__main__':
    app.run()