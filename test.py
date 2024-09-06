import os
import subprocess

def open_text_file(file_path):
    # Create the file if it does not exist
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            # Optionally, you can write initial content to the file here
            file.write("")
    try:
        # Open the file in nano
        subprocess.run(['nano', file_path], check=True)
    except FileNotFoundError:
        print("nano is not installed or not found in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to open the file: {e}")


file_path = "quizlet_data.txt"
open_text_file(file_path)