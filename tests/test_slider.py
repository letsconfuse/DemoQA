# File: test_slider.py
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

def test_slider_movement(driver):
    driver.get("https://demoqa.com/slider")
    slider = driver.find_element(By.CLASS_NAME, "range-slider")
    ActionChains(driver).click_and_hold(slider).move_by_offset(50, 0).release().perform()
    time.sleep(1)
    slider_value = driver.find_element(By.ID, "sliderValue")
    assert int(slider_value.get_attribute("value")) > 25
