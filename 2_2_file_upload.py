# Загрузка текстового файла в форме регистрации
from selenium import webdriver
import math
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("asd")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("dfg")
    email = browser.find_element_by_name("email")
    email.send_keys("fhfjk")

    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt') 

    send_button = browser.find_element_by_id("file")
    send_button.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


