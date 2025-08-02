# File: test_title_links.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_homepage_title(driver):
    driver.get("https://demoqa.com/")
    assert "DEMOQA" in driver.title

def test_internal_link_interactions(driver):
    driver.get("https://demoqa.com/")
    driver.find_element(By.XPATH, '//h5[text()="Interactions"]').click()
    WebDriverWait(driver, 10).until(EC.url_contains("interaction"))
    assert "interaction" in driver.current_url

def test_sidebar_link_resizable(driver):
    driver.get("https://demoqa.com/")
    driver.find_element(By.XPATH, '//h5[text()="Interactions"]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Resizable"]'))).click()
    assert "resizable" in driver.current_url

def test_sidebar_link_tooltip(driver):
    driver.get("https://demoqa.com/")
    driver.find_element(By.XPATH, '//h5[text()="Widgets"]').click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[text()="Tool Tips"]'))
    )

    tooltip_link = driver.find_element(By.XPATH, '//span[text()="Tool Tips"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", tooltip_link)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Tool Tips"]')))
    tooltip_link.click()

    assert "tool-tips" in driver.current_url

def test_external_header_link(driver):
    # Optional: test removed, or you can test some footer link instead
    pass
