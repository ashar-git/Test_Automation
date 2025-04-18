import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@allure.title("selenium exceptions")
@allure.description("Verify selenium exceptions")
def test_selenium_exceptions():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    try:
        driver.find_elements(By.XPATH,"No such element")
    except Exception as e:
        print(e)
    time.sleep(5)


