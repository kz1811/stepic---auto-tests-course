import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/get_attribute.html")

	#достаем с помощью get_attribute значение аттрибута и считаем пример
	x = browser.find_element(By.TAG_NAME, "img")
	x = x.get_attribute("valuex")
	x = math.log(abs(12*math.sin(int(x))))

	#вставляем ответ в поле ввода
	answ = browser.find_element(By.ID, "answer")
	answ.send_keys(str(x))

	#ищем чек-бокс с надписью I'm the robot
	chk_box = browser.find_element(By.ID, "robotCheckbox")
	chk_box.click()

	#ищем чек-бокс с надписью Robot's rule
	rad_button = browser.find_element(By.ID, "robotsRule")
	rad_button.click()

	#ищем кнопку отправки ответа
	submit_button = browser.find_element(By.TAG_NAME, "button")
	submit_button.click()


finally:
	#Задержка времени 30 секунд
	time.sleep(5)
	#Закрытие окна браузера
	browser.quit()
