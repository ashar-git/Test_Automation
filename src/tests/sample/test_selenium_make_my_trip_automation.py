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


@allure.title("Actions MMT Automation")
@allure.description("Verify MMT Automation")
def test_verify_mmt_actions():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com")
    driver.maximize_window()
    WebDriverWait(driver=driver,timeout=10).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']")))
    driver.find_element(By.XPATH,"//span[@data-cy='closeModal']").click()
    time.sleep(2)
    #move the  mouse to fromCity
    #click on it
    #Type DEL
    #press down arrow key
    #press enter
    fromcity = driver.find_element(By.ID,"fromCity")
    actions = ActionChains(driver=driver)
    (actions.move_to_element(fromcity)
     .click()
     .send_keys_to_element(fromcity,"del")
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER).perform())
    time.sleep(5)
    driver.quit()