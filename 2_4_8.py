from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
import os


try:
	
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	browser.get('http://suninjuly.github.io/explicit_wait2.html')

	button = browser.find_element(By.TAG_NAME, "button")
	signall = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
	button.click()

	m = browser.find_element(By.ID, "input_value").text
	m = str(math.log(abs(12*math.sin(int(m)))))
	form = browser.find_element(By.ID, "answer")
	form.send_keys(m)
	m = browser.find_element(By.ID, "solve")
	m.click()

	

finally:
	time.sleep(15)
	browser.quit()
