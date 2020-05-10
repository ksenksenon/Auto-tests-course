import unittest
from selenium import webdriver
import time
class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block .form-control.first")
        first_name.send_keys("text")

        last_name = browser.find_element_by_css_selector(".first_block .form-control.second")
        last_name.send_keys("text")

        email = browser.find_element_by_css_selector(".first_block .form-control.third")
        email.send_keys("text")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration 1 error")
        
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block .form-control.first")
        first_name.send_keys("text")

        last_name = browser.find_element_by_css_selector(".first_block .form-control.second")
        last_name.send_keys("text")

        email = browser.find_element_by_css_selector(".first_block .form-control.third")
        email.send_keys("text")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration 2 error")
        
if __name__ == "__main__":
    unittest.main()