# File Organizer
A simple Python script that automatically organizes files in a folder based on their file extensions. Perfect for keeping your folders clean and well-organized

---

## Features
- Automatically sorts files by type (Images, Documents, Music, Videos, Archives)
- Creates target folders if they don't exist
- Easy to customize and extend

---

## Requirements
1. Python 3.x
2. No external libraries needed

---

## How To Use
1. Make sure you have Python installed (Python 3 recommended). Download it from [python.org](https://www.python.org/downloads/).  
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

When you run the script, it will ask you to enter the folder path to organize.

Example input:
```bash
Enter folder path to organize: C:\Users\YourName\Downloads
```

---

## Example
Before:
```bash
Downloads/
├── photo.jpg
├── vacation.png
├── report.pdf
├── notes.txt
├── song.mp3
├── video.mp4
├── archive.zip
├── randomfile.xyz
```

After:
```bash
Downloads/
├── Images/
│   ├── photo.jpg
│   └── vacation.png
├── Documents/
│   ├── report.pdf
│   └── notes.txt
├── Music/
│   └── song.mp3
├── Videos/
│   └── video.mp4
├── Archives/
│   └── archive.zip
├── Others/
│   └── randomfile.xyz

```

---

## Customization
You can customize file categories and extensions by editing the extension_map dictionary inside main.py.

---

## Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

---

## Connect With Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sultan%20Badra-blue?logo=linkedin\&logoColor=white\&style=flat-square)](https://www.linkedin.com/in/sultan-badra)

---

## License
This project is open-source and free to use under the MIT [LICENSE](./LICENSE).
