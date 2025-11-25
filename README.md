# Password ZIP Cracker (Python)

This is a simple Python program with a graphical user interface (GUI) that attempts to crack the password of a ZIP file using a dictionary attack method. It goes through a list of possible passwords provided in a text file.

## What's Included

- `Password_cracker.py` – the main Python script with the GUI and cracking logic
- `passwords.txt` – a list of possible passwords (dictionary file)
- `zip_folder.zip` – a sample password-protected ZIP file for testing

## Features

- User-friendly graphical interface (built with `tkinter`)
- No terminal usage required once it's running
- Real-time status updates as it tests passwords

## Requirements

- Python 3.x
- No additional installations required (uses built-in libraries like `zipfile` and `tkinter`)

## How to Run

1. Make sure you have Python 3 installed.
2. Open your terminal or command prompt.
3. Navigate to the folder with the script and run:

```bash
python3 Password_cracker.py
