
from selenium import webdriver
from selenium.webdriver.common.by import By

import math

import time

# переход на нужную страницу
link = "http://suninjuly.github.io/math.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

# функция, которая находит значение выражения при заданном x


# находим значение x для выполнения задания
    x_in_first_test = browser.find_element(By.ID,"input_value")
    x_value = x_in_first_test.text

# высчитываем результат для первого задания
    first_test_result = calc(x_value)

# вводим ответ к первому тесту
    first_test_input = browser.find_element(By.ID,"answer")
    first_test_input.send_keys(first_test_result)

# выбираем checkbox
    robot_checkbox = browser.find_element(By.ID,"robotCheckbox")
    robot_checkbox.click()

# выбираем radiobutton
    robot_radiobutton = browser.find_element(By.ID, "robotsRule")
    robot_radiobutton.click()

# нажимаем кнопку отправить
    send_button = browser.find_element(By.CLASS_NAME, "btn-default")
    send_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()