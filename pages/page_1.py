from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class saucelabs:
    def __init__(self,driver):
        self.driver= driver
    def login(self):
        url="https://www.saucedemo.com/"
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        username=self.driver.find_element(By.ID,"user-name")
        password=self.driver.find_element(By.ID,"password")
        login_button=self.driver.find_element(By.ID,"login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        self.driver.implicitly_wait(10)
    def logout(self):
        login_button=self.driver.find_element(By.ID,"login-button")
        self.driver.implicitly_wait(10)
        menu_button=self.driver.find_element(By.ID,"react-burger-menu-btn")
        logout_button=self.driver.find_element(By.ID,"logout_sidebar_link")
        menu_button.click()
        time.sleep(1)
        logout_button.click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located,login_button)
    