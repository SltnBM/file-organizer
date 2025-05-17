# 🗂️ File Organizer - Python Project

A simple Python script to automatically organize files in a folder based on their file extensions. Perfect for keeping your folder clean and tidy!

---

## 📦 Features

- Automatically sorts files by type (Images, Documents, Music, Videos, Archives)
- Creates target folders if they don't exist
- Easy to customize and extend
- Works on Windows, macOS, and Linux

---

## 🚀 How To Use
1. Make sure you have Python installed (Python 3 recommended).
2. Clone the Repository

```bash
git clone https://github.com/SltnBM/file-organizer.git
```
3. Navigate to the project directory
```bash
cd file-organizer
```
4. Run the script using terminal or command prompt
```bash
python main.py
```

## ⚙️ Setup
In main.py, set the path of the folder you want to organize:
```bash
folder_path = r'C:\Users\YourName\Downloads'
```

## Example 🔍
Before:
```bash
 📂 Downloads/
├── 🖼️ photo.jpg
├── 🖼️ vacation.png
├── 📄 report.pdf
├── 📄 notes.txt
├── 🎵 song.mp3
├── 🎥 video.mp4
├── 🗃️ archive.zip
├── ❓ randomfile.xyz
```

After:
```bash
📂 Downloads/
├── 📁 Images/
│   ├── 🖼️ photo.jpg
│   └── 🖼️ vacation.png
├── 📁 Documents/
│   ├── 📄 report.pdf
│   └── 📄 notes.txt
├── 📁 Music/
│   └── 🎵 song.mp3
├── 📁 Videos/
│   └── 🎥 video.mp4
├── 📁 Archives/
│   └── 🗃️ archive.zip
├── 📁 Others/
│   └── ❓ randomfile.xyz

```

## 📄 License
This project is open-source and free to use under the MIT License.