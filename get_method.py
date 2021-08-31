import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    #поиск х и ввод ответа в поле ввода
    x  = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = int(x.text)
    m = math.log(abs(12*math.sin(x)))

    element = browser.find_element(By.ID, "answer")
    element.send_keys(str(m))

    button = browser.find_element(By.ID, "robotCheckbox")
    button.click()

    button = browser.find_element(By.ID, "robotsRule")
    button.click()

    button = browser.find_element(By.XPATH, '//button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла