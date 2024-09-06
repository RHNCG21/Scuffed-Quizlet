import os
import platform

def open_text_file(file_path):
    # Create the file if it does not exist
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            # Optionally, you can write initial content to the file here
            file.write("")

    # Open the file with the appropriate command based on the OS
    if platform.system() == "Darwin":  # macOS
        os.system(f"open {file_path}")
    elif platform.system() == "Windows":
        os.system(f"start {file_path}")
    else:  # Linux
        os.system(f"xdg-open {file_path}")


file_path = "quizlet_data.txt"
open_text_file(file_path)