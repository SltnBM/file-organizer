import os
import shutil

# Set the folder you want to organize
folder_path = r'C:\Users\YourName\Downloads'  # Replace with your actual path

# File extension to folder mapping
extension_map = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Music': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.mkv'],
    'Archives': ['.zip', '.rar'],
    'Others': []
}

# Loop through files in the folder
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, ext = os.path.splitext(file)

    # Determine destination folder
    found = False
    for folder, ext_list in extension_map.items():
        if ext.lower() in ext_list:
            target_folder = os.path.join(folder_path, folder)
            found = True
            break

    if not found:
        target_folder = os.path.join(folder_path, 'Others')

    # Create target folder if it doesn't exist
    os.makedirs(target_folder, exist_ok=True)

    # Move the file
    shutil.move(file_path, os.path.join(target_folder, file))

print("✅ Done! Files have been organized by type.")
