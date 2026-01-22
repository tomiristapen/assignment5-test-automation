import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.logger import get_logger


logger = get_logger()


@pytest.fixture
def driver():
    logger.info("TEST START: launching browser")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    os.makedirs("downloads", exist_ok=True)
    prefs = {
        "download.default_directory": os.path.abspath("downloads"),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_settings.popups": 0,
        "profile.managed_default_content_settings.downloads": 1
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(5)

    yield driver

    logger.info("TEST END: closing browser")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Take screenshot automatically if test failed (on call phase)
    """
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = os.path.join("screenshots", f"{item.name}_{timestamp}.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"TEST FAILED: screenshot saved -> {screenshot_path}")
