from selenium.webdriver.common.by import By
from utils.logger import get_logger
import time
import os

logger = get_logger()
BASE_URL = "https://the-internet.herokuapp.com"


def test_login_valid(driver):
    logger.info("TC-LOGIN-001: Open login page")
    driver.get(f"{BASE_URL}/login")

    logger.info("TC-LOGIN-001: Enter username")
    driver.find_element(By.ID, "username").send_keys("tomsmith")

    logger.info("TC-LOGIN-001: Enter password")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    logger.info("TC-LOGIN-001: Click Login")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    logger.info("TC-LOGIN-001: Validate success message")
    message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in message


def test_file_download_initiated(driver):
    logger.info("TC-DOWNLOAD-001: Open download page")
    driver.get(f"{BASE_URL}/download")

    target_name = "SomeFile.txt"
    logger.info(f"TC-DOWNLOAD-001: Find file link: {target_name}")

    file_link = driver.find_element(By.LINK_TEXT, target_name)
    assert file_link.is_displayed(), "Expected download link to be visible"

    href = file_link.get_attribute("href")
    assert href.endswith(f"/download/{target_name}"), f"Expected href to end with /download/{target_name}, but got: {href}"

    logger.info(f"TC-DOWNLOAD-001: Click file link: {target_name}")
    file_link.click()

    time.sleep(2)
    
    downloads_dir = os.path.abspath("downloads")
    assert os.path.exists(downloads_dir), f"Downloads directory not found: {downloads_dir}"
    
    files = os.listdir(downloads_dir)
    assert len(files) > 0, f"No files found in downloads directory"
    
    downloaded_file = files[0]
    logger.info(f"TC-DOWNLOAD-001: File downloaded: {downloaded_file}")
    logger.info("TC-DOWNLOAD-001: Download initiated successfully")


def test_add_remove_elements(driver):
    logger.info("TC-ADDREMOVE-001: Open add/remove elements page")
    driver.get(f"{BASE_URL}/add_remove_elements/")

    logger.info("TC-ADDREMOVE-001: Click Add Element")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()

    logger.info("TC-ADDREMOVE-001: Verify Delete button appears")
    delete_btns = driver.find_elements(By.CSS_SELECTOR, "#elements button")
    assert len(delete_btns) == 1

    logger.info("TC-ADDREMOVE-001: Click Delete")
    delete_btns[0].click()

    logger.info("TC-ADDREMOVE-001: Verify element removed")
    delete_btns_after = driver.find_elements(By.CSS_SELECTOR, "#elements button")
    assert len(delete_btns_after) == 0

def test_forgot_password_confirmation_message(driver):
    logger.info("TC-FORGOTPASS-001: Open forgot password page")
    driver.get("https://the-internet.herokuapp.com/forgot_password")

    logger.info("TC-FORGOTPASS-001: Enter email")
    driver.find_element(By.ID, "email").send_keys("test@gmail.com")

    logger.info("TC-FORGOTPASS-001: Click Retrieve password")
    driver.find_element(By.ID, "form_submit").click()

    logger.info("TC-FORGOTPASS-001: Validate confirmation message")
    body_text = driver.find_element(By.TAG_NAME, "body").text

    assert "Your e-mail's been sent!" in body_text, f"Expected confirmation message, but got: {body_text}"
