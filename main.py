import os
import shutil

def organize_files(folder_path):
# File extension to folder mapping
    extension_map = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.ppt', '.pptm'],
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

        target_path = os.path.join(target_folder, file)
        # Avoid overwrite by renaming
        counter = 1
        base_name, extension = os.path.splitext(file)
        while os.path.exists(target_path):
            new_name = f"{base_name}({counter}){extension}"
            target_path = os.path.join(target_folder, new_name)
            counter += 1

        try:
            # Move the file
            shutil.move(file_path, target_path)
            print(f"Moved: {file} -> {target_path}")
        except Exception as e:
            print(f"Failed to move {file}: {e}")
            
    print("✅ Done! Files have been organized by type.")

if __name__ == "__main__":
    folder = input("Enter folder path to organize: ")
    organize_files(folder)