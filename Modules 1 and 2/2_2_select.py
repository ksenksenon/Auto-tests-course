# Работа с выпадающим списком
from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select

try:
    link="http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x=int(browser.find_element_by_id("num1").text)
    y=int(browser.find_element_by_id("num2").text)
    sum=x+y
    print(sum)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum)) # ищем элемент с текстом "Python"

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
