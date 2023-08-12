import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vmlogin():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome(options)
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()

    email_ele = driver.find_element(By.ID, "login-username")
    email_ele.send_keys("93npu2yyb0@esiix.com")

    pass_ele = driver.find_element(By.NAME, "password")
    pass_ele.send_keys("Wingify@123")

    rem_ele = driver.find_element(By.CLASS_NAME, "checkbox-radio-icon")
    rem_ele.click()

    sign_in_button_ele = driver.find_element(By.ID, "js-login-btn")
    sign_in_button_ele.click()

    time.sleep(5)

    LOGGER.info("title is" + driver.title)
    assert "Dashboard" in driver.title
