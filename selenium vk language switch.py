from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

options = Options()
options.binary_location = r'firefox.exe' # path to firefox.exe file

s = Service('geckodriver.exe') # path to geckodriver.exe file
driver = webdriver.Firefox(service=s, options=options)
driver.get('https://vk.com/')
vk_login = driver.find_element(By.ID, 'top_switch_lang')
driver.implicitly_wait(100)
vk_login.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'VkIdForm__header') , # element filtration
        'Sign in to VK'# the expected text
    )
)