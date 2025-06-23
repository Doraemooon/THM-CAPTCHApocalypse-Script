from PIL import Image
import os
import pytesseract
import io

def read_captcha(img_bytes):
	image = Image.open(io.BytesIO(img_bytes))
	image = image.resize((image.width*5, image.height*5), Image.LANCZOS) #Scale image 5x
	return pytesseract.image_to_string(image, config="--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ23456789")
