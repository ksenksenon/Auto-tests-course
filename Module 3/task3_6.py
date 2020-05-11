# Параметризация тестов
import pytest
from selenium import webdriver
import math
import time

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.mark.parametrize('number', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element_by_tag_name("textarea").send_keys(str(answer))
    browser.find_element_by_css_selector(".submit-submission").click()
    hint = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert "Correct!" == hint, "Answer is wrong!"