# About
The scripts in this repository are my successful attempts at solving TryHackme's CAPTCHApocalypse CTF room!

How the scripts work:
1. Load a browser in headless mode
2. GET the webpage
3. Wait for the animation to play, then capture an image of the CAPTCHA
4. Use PILLOW for image pre-processing to scale up the image
5. Use a Tesseract Wrapper for Python, Pytesseract to convert an image to text
6. Try the given Username, Password from Wordlist and CAPTCHA
# How to use?
1. Clone the repository\
   ```git clone https://github.com/Doraemooon/THM-CAPTCHApocalypse-Script.git```
2. Create a Python virtual environment and activate it\
   ```python3 -m venv myvenv```\
   ```source myvenv/bin/activate```
3. Install requirements.txt\
   ```pip3 install -r requirements.txt```
4. Change url and wordlist variable in brute.py
5. Run the script!
