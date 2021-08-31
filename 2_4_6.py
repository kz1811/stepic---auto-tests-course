from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
import os


try:
	
	browser = webdriver.Chrome()
	browser.get(' http://suninjuly.github.io/cats.html')
	button = browser.find_element(By.ID, 'button')
	button.click()

	

finally:
	time.sleep(5)
	browser.quit()
