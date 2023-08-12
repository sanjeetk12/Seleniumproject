import logging
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    return driver


def test_verify_title(driver):

    LOGGER = logging.getLogger(__name__)
    print(driver.title)
    LOGGER.info("This is information logs")
    assert "Login - VWO" == driver.title

