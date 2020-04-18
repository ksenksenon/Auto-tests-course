# Ждем нужный текст на странице
from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
        
    button = browser.find_element_by_id("book")
    button.click()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    submit = browser.find_element_by_id("solve")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


