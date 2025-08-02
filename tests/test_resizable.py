# File: test_resizable.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_resizable_element(driver):
    driver.get("https://demoqa.com/resizable/")
    
    # Get the resizable box using the correct ID
    box = driver.find_element(By.ID, "resizableBoxWithRestriction")
    
    # Get the resize handle using updated class
    resize_handle = box.find_element(By.CSS_SELECTOR, "span.react-resizable-handle")

    # Resize using ActionChains
    actions = ActionChains(driver)
    actions.click_and_hold(resize_handle).move_by_offset(100, 50).release().perform()
    
    time.sleep(1)

    # Optional assertion: verify the box size increased
    new_width = box.size["width"]
    new_height = box.size["height"]

    assert new_width > 200
    assert new_height > 200
