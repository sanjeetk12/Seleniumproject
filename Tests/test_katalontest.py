# Test case to automation - Manual Testing

# Enter the Date and Text and Click Book Appointment
# Verify that the Appointment Confirmation message is visible on the page.

import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_katalon_verify():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options)
    # Open - https://katalon-demo-cura.herokuapp.com/
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    # Click on the Make Appointment
    driver.find_element(By.ID, "btn-make-appointment").click()

    # Put Username, Password and click Login
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    # driver.find_element(By.CLASS_NAME, "form-control").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()

    # Select the 2 option, Radio, 2 Checkbox

    dropdown_element = driver.find_element(By.ID, "combo_facility")
    dropdown = Select(dropdown_element)
    dropdown.select_by_value("Hongkong CURA Healthcare Center")

    driver.find_element(By.ID, "chk_hospotal_readmission").click()
    driver.find_element(By.ID, "radio_program_medicaid").click()

    driver.find_element(By.ID, "txt_visit_date").send_keys("09/08/2023")
    driver.find_element(By.ID, "btn-book-appointment").click()
    assert "CURA Healthcare Service" == driver.title
    heading = driver.find_element(By.TAG_NAME, "h2")
    assert "Appointment Confirmation" == heading.text

    driver.quit()


