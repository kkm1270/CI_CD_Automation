import pytest
import time
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()