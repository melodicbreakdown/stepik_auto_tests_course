
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import pyperclip
import time

# функция, которая находит значение выражения при заданном x
def calc(x):
	return str( math.log (abs ( 12 * math.sin( x ) ) ) )

# переход на нужную страницу
link = "http://suninjuly.github.io/alert_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	# кликаем по волшебной кнопке
	magic_button = browser.find_element(By.CLASS_NAME, "btn-primary")
	magic_button.click()

	# пока не "умеем" пользоваться нормальными ожиданиями
	time.sleep(1)

	# принимаем assert
	alert = browser.switch_to.alert
	alert.accept()

	# находим значение x для выполнения задания
	x_string = browser.find_element(By.ID, "input_value")
	x_number = int( x_string.text )

	# высчитываем результат для задания
	answer = calc(x_number)

	# находим поле ввода, вводим туда ответ
	input_answer = browser.find_element(By.ID, "answer")
	input_answer.send_keys(answer)

	# находим и нажимаем на кнопку
	send_button = browser.find_element(By.CLASS_NAME, "btn-primary")
	send_button.click()

	# все еще не "умеем" пользоваться нормальными ожиданиями
	time.sleep(1)

	# ждём алерта, достаем из него текст
	alert = browser.switch_to.alert
	alert_text = alert.text

	# вытаскиваем из текста алерта число, копируем в буфер обмена
	addToClipBoard = alert_text.split(': ')[-1]
	pyperclip.copy(addToClipBoard)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()