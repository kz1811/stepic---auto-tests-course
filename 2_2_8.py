from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
import os


try:
	#Запуск окна хрома и ссылки
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/file_input.html")
	
	#Находим поля по CSS-селектору и вводим в них значения
	form1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
	form1.send_keys("a")
	form2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
	form2.send_keys("b")
	form3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
	form3.send_keys("c")

	
	element = browser.find_element(By.ID, "file")  #Находим поле отправки файла
	current_dir = os.path.abspath(os.path.dirname(__file__))  #Находим текущую директорию
	file_path = os.path.join(current_dir, 'abcd.txt') #в file_path прикрепляем файл, лежащий в каталоге
	element.send_keys(file_path)  #Прикрепляем файл к форме

	#Находим и нажимаем кнопку отправки ответа 
	button = browser.find_element(By.CLASS_NAME, "btn-primary")
	button.click()

finally:
	time.sleep(5)
	browser.quit()
