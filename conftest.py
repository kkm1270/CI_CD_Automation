import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='session')
def driver():
    options = Options()
    # Optional: run in headless if in CI
    #options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    
    # Initialize driver with webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()




























# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import tempfile

# @pytest.fixture(scope='session')
# def driver():
#     options = Options()
#     # Create a temporary directory for Edge user data
#     user_data_dir = tempfile.mkdtemp()
#     options.add_argument(f'--user-data-dir={user_data_dir}')
#     # Optional: run in headless if in CI
#     #options.add_argument('--headless')
#     options.add_argument('--disable-gpu')
#     options.add_argument('--no-sandbox')
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()
































# import pytest
# import time
# from selenium import webdriver


# @pytest.fixture(scope='session')
# def driver():
#     driver=webdriver.Edge()
#     driver.maximize_window()
#     yield driver
#     driver.quit()