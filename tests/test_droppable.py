# File: test_droppable.py
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

def test_droppable_element(driver):
    driver.get("https://demoqa.com/droppable/")
    drag = driver.find_element(By.ID, "draggable")
    drop = driver.find_element(By.ID, "droppable")
    ActionChains(driver).drag_and_drop(drag, drop).perform()
    time.sleep(1)
    assert "Dropped!" in drop.text
    