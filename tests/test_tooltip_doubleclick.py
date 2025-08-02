# File: test_tooltip_doubleclick.py
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

def test_tooltip_double_click(driver):
    driver.get("https://demoqa.com/buttons")
    button = driver.find_element(By.ID, "doubleClickBtn")
    ActionChains(driver).double_click(button).perform()
    message = driver.find_element(By.ID, "doubleClickMessage")
    assert "You have done a double click" in message.text
