import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver


def test_open_page(browser):
    browser.get("http://34.141.58.52:8080/#/login")

def test_login(browser):
    input1 = browser.find_element(By.ID, "login")
    input1.send_keys("e.v.koroleva@mail.ru")

    time.sleep(1)


def test_password(browser):
    input2 = browser.find_element(By.CSS_SELECTOR, "#password > input")
    input2.send_keys("1234")

    time.sleep(1)

def test_find_element(browser):
    button = browser.find_element(By.CLASS_NAME, "p-button-label")
    button.submit()

    time.sleep(1)

def test_len(browser):
    pets = browser.find_elements(By.CSS_SELECTOR, ".col-12")
    assert len(pets) == 4






