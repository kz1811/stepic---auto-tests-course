from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
	#Запуск окна хрома и ссылки
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/selects1.html")

	#Поиск чисел по ид, сумму которых нужно найти
	num1 = browser.find_element(By.ID, "num1").text
	num2 = browser.find_element(By.ID, "num2").text
	#Сумма
	result = int(num1)+int(num2)

	#Поиск с помощью атрибута selenium.webdriver.support.ui.Select выпадающего списка по тегу
	
	select = Select(browser.find_element(By.TAG_NAME, "select"))
	select.select_by_value(str(result))
	

	#browser.find_element(By.ID, "dropdown").send_keys(str(result))

	browser.find_element(By.CLASS_NAME, "btn-default").click()


finally:
	time.sleep(10)
	browser.quit()
