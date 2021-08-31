from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
import os


try:
	
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/redirect_accept.html')
	button = browser.find_element(By.CLASS_NAME, 'trollface')
	button.click()

	secwindow = browser.window_handles[1]
	browser.switch_to.window(secwindow)

	m = browser.find_element(By.ID, "input_value")
	x = int(m.text)
	num = math.log(abs(12*math.sin(x)))

	answ = browser.find_element(By.ID, "answer")
	answ.send_keys(str(num))

	button = browser.find_element(By.CLASS_NAME, 'btn-primary')
	button.click()

finally:
	time.sleep(5)
	browser.quit()
