from selenium.webdriver.common.by import By
import time


def test_checkboxes(driver):
    driver.get("https://demoqa.com/checkbox")
    driver.find_element(By.CLASS_NAME, "rct-collapse-btn").click()
    driver.find_element(By.CLASS_NAME, "rct-checkbox").click()
    assert "You have selected" in driver.page_source
