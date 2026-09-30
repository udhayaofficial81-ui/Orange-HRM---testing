import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = os.getenv("ORANGEHRM_URL", "https://opensource-demo.orangehrmlive.com/")
USERNAME = os.getenv("ORANGEHRM_USERNAME", "Admin")
PASSWORD = os.getenv("ORANGEHRM_PASSWORD", "admin123")


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(45)
    yield browser
    browser.quit()


def test_orangehrm_end_to_end(driver):
    wait = WebDriverWait(driver, 20)

    driver.get(BASE_URL)
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h6.oxd-topbar-header-breadcrumb-module")
        )
    )
    assert "dashboard" in driver.current_url.lower()

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='PIM']"))
    ).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[normalize-space()='PIM']")))
    wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//label[normalize-space()='Employee Name']/../following-sibling::div//input",
            )
        )
    )
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']"))
    ).click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-table")))
    wait.until(
        lambda page: page.find_elements(
            By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row"
        )
        or "No Records Found" in page.page_source
    )
    assert (
        driver.find_elements(By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row")
        or "No Records Found" in driver.page_source
    )

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-userdropdown-tab"))
    ).click()
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']"))
    ).click()
    wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    assert "auth/login" in driver.current_url.lower()
