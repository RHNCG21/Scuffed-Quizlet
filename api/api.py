import json
from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()
app = Flask(__name__)
token = os.getenv('TOKEN')
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

# Initialize Supabase client
supabase: Client = create_client(supabase_url, supabase_key)

BUCKET_NAME = 'set-data'
FILE_NAME = 'data.json'

def load_data():
    """Load data from the JSON file in Supabase Storage."""
    try:
        response = supabase.storage.from_(BUCKET_NAME).download(FILE_NAME)
        json_data = response.decode('utf-8')
        return json.loads(json_data)
    except Exception as e:
        # If the file does not exist, return an empty dictionary
        if '404' in str(e):
            return {}
        print(f"Error loading data: {e}")
        return {"Error": "Failed to load data"}

def save_data(new_data):
    """Append data to the JSON file in Supabase Storage."""
    try:
        # Load existing data from Supabase Storage
        current_data = load_data()
        
        # Merge new data with existing data
        current_data.update(new_data)
        
        # Convert the updated data to JSON
        json_data = json.dumps(current_data, indent=4)
        
        # Remove the existing file if it exists
        try:
            supabase.storage.from_(BUCKET_NAME).remove([FILE_NAME])
        except Exception as e:
            print(f"Error removing file: {e}")

        # Upload the updated data
        response = supabase.storage.from_(BUCKET_NAME).upload(FILE_NAME, json_data.encode('utf-8'))
        
        # Check if the response has a success status code
        if response.status_code != 200:
            raise Exception(f"Failed to upload data to Supabase Storage: {response.text}")
        
        return {"message": "Data appended successfully"}
        
    except Exception as e:
        print(f"Error saving data: {e}")
        return {"error": "Failed to save data"}

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        auth_key = request.headers.get('Authorization')
        if auth_key == "Bearer " + token:
            data = request.get_json()
            # Save the updated data back to Supabase Storage
            result = save_data(data)
            return jsonify(result)
        else:
            return jsonify({"error": "Unauthorized"}), 401
    else:  # For GET requests
        # Return the current data from Supabase Storage
        current_data = load_data()
        return jsonify(current_data)
    
@app.route('/')
def home():
    return "you have reached the scuffed quizlet api. try /data for list of sets" 

if __name__ == '__main__':
    app.run()