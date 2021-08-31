from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

try:
	#Запуск окна хрома и ссылки
	browser = webdriver.Chrome()
	browser.get("http://SunInJuly.github.io/execute_script.html")

	#Поиск чисел по ид, сумму которых нужно найти
	x = int(browser.find_element(By.ID, "input_value").text)
	x = math.log(abs(12*math.sin(x)))
	#Поиск меню ввода
	inp_str = browser.find_element(By.ID, "answer")
	inp_str.send_keys(str(x))

	#поиск чекбокса - checkbox
	chk_button = browser.find_element(By.ID, "robotCheckbox")
	#открытие доступа для клика
	browser.execute_script("return arguments[0].scrollIntoView(true);", chk_button)
	#клик
	chk_button.click()

	#поиск кнопки выбора - radiobutton 
	rad_button = browser.find_element(By.ID, "robotsRule")
	#открытие доступа для клика
	browser.execute_script("return arguments[0].scrollIntoView(true);", rad_button)
	#клик
	rad_button.click()

	#пролистать до кнопки
	button = browser.find_element(By.CLASS_NAME, "btn-primary")
	#открытие доступа для клика
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	#клик
	button.click()


finally:
	time.sleep(5)
	browser.quit()
