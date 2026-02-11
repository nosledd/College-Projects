import os
import shutil

def sort_file(file_path, subject):
    
    # Create subject folder if not exists
    destination_folder = f"sorted_notes/{subject}"
    os.makedirs(destination_folder, exist_ok=True)
    
    # Get file name
    file_name = os.path.basename(file_path)
    
    # Destination path
    destination_path = os.path.join(destination_folder, file_name)
    
    # Move file
    shutil.move(file_path, destination_path)
    
    print(f"File moved to {destination_folder}")
    
    return destination_path
