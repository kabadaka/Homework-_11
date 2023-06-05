import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:

    browser = webdriver.Chrome()
    browser.get('http://34.141.58.52:8080/#/')

    browser.find_element(By.ID, 'typesSelector').click()

    browser.find_element(By.ID, 'pv_id_2_2').click()

    browser.save_screenshot('result.png')


finally:
    browser.quit()
