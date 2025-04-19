import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Actions P1")
@allure.description("Verify Action P1")
def test_verify_keyboard_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.XPATH,"//input[@name='firstname']")
    actions = ActionChains(driver=driver)
    ((actions
     .key_down(Keys.SHIFT))
     .send_keys_to_element(first_name,"The testing Academy")
     .key_up(Keys.SHIFT).perform()
     )
    time.sleep(10)
    driver.quit()


@allure.title("Actions P2")
@allure.description("Verify Action P2")
def test_verify_mouse_click_and_back_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    atag = driver.find_element(By.ID,"click")
    atag.click()
    time.sleep(2)
    actionbuilders = ActionBuilder(driver=driver)
    actionbuilders.pointer_action.pointer_up(MouseButton.BACK)
    actionbuilders.perform()



@allure.title("Actions P3")
@allure.description("Verify Action P3")
def test_verify_mouse_click_and_hold():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    element_to_hold = driver.find_element(By.ID,"draggable")
    time.sleep(2)
    actions = ActionChains(driver=driver)
    actions.click_and_hold(element_to_hold).perform()
    time.sleep(10)
    driver.quit()
