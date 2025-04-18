import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@allure.title("Dropdowns")
@allure.description("Verify Dropdowns")
def test_selenium_dropdown():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    driver.maximize_window()
    select_html_tags = driver.find_element(By.ID,"dropdown")
    select = Select(select_html_tags)
    select.select_by_visible_text("Option 1")
    time.sleep(5)