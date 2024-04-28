
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# переход на нужную страницу
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим все нужные элементы на странице
    name_field = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    lastname_field = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    email_field = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    file_button = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    send_button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")

    # заполняем форму
    name_field.send_keys("H")
    lastname_field.send_keys("F")
    email_field.send_keys("y")

    # находим путь до текущей папки
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # достраиваем его до пути до нужного файла
    file_path = os.path.join(current_dir, "test_file.txt")

    # посылаем этот файл
    file_button.send_keys(file_path)
    send_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()