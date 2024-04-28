from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = "http://SunInJuly.github.io/execute_script.html"

# функция, которая находит значение выражения при заданном x
def calc(x):
	return str ( math.log( abs( 12 * math.sin( int( x ) ) ) ) )

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим значение x для выполнения задания
    x_in_text = browser.find_element(By.ID, "input_value")
    x_value = x_in_text.text

    # считаем значение x
    first_answer = calc(x_value)

    # скроллим страницу до появления на ней поля ввода в зоне видимости
    first_input = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", first_input)

    # вводим ответ в поле ввода
    first_input.send_keys(first_answer)

    # выбираем checkbox
    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    # выбираем radiobutton
    robotRadiobutton = browser.find_element(By.ID, "robotsRule")
    robotRadiobutton.click()

    # нажимаем кнопку отправить
    send_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    send_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()