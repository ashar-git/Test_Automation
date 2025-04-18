import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

@allure.title("selenium stale element exceptions")
@allure.description("Verify selenium stale element exceptions")
def test_selenium_stale_element_exceptions():
    driver=webdriver.Chrome()
    driver.get("https://google.com")
    textarea = driver.find_elements(By.ID,"input")
    driver.refresh()
    time.sleep(5)


