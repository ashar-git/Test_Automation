import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import ChromiumOptions


@allure.title("Actions MMT Automation")
@allure.description("Verify MMT Automation")
def test_verify_windows():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    parent_window = driver.current_window_handle
    # print(parent_window)

    link = driver.find_element(By.LINK_TEXT,"Click Here")
    link.click()

    window_handle = driver.window_handles
    # print(window_handle)
    for handle in window_handle:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("Test Passed")
            break
    time.sleep(5)
    driver.quit()