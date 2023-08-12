import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_verify():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options)
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    driver.maximize_window()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                   ((By.XPATH, "//a[contains(text(),'OrangeHRM, Inc')]"))
                                   )

    username = driver.find_element(By.XPATH, "//input[@name='username']")
    username.send_keys("admin")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Hacker@4321")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                   ((By.XPATH, "//h5[@class='oxd-text oxd-text--h5 oxd-table-filter-title']"))
                                   )

    driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                   ((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']"))
                                   )
    driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("sanjeet")
    driver.find_element(By.XPATH, "//input[@name='middleName']").send_keys("k")
    driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("kosi")
    driver.find_element(By.XPATH, "// button[@type = 'submit']").click()
