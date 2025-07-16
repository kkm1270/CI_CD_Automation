import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.page_1 import saucelabs


def test_case_1(driver):
    case_1=saucelabs(driver)
    case_1.login()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Selenium not landed on Home Screen of Web App."
def test_case_2(driver):
    case_2=saucelabs(driver)
    case_2.logout()
    assert driver.current_url == "https://www.saucedemo.com/", "Selenium did not navigated back to Login Screen of Web App."
