import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time


URL = 'https://moneyway.fly.dev/users/sign_in'


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()


def test_validate_title(browser):
    expected_title = "Moneyway"
    assert browser.title == expected_title


def test_click_button(browser):
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()


def test_click_link(browser):
    link = browser.find_element(By.CSS_SELECTOR, 'a[href="/users/sign_up"]')
    link.click()
    assert browser.current_url == "https://moneyway.fly.dev/users/sign_up", "redirected to an unexpected URL"



def test_click_link_pwd(browser):
    link = browser.find_element(By.CSS_SELECTOR, 'a[href="/users/password/new"]')
    link.click()
    assert browser.current_url == "https://moneyway.fly.dev/users/password/new", "redirected to an unexpected URL"


def test_valid_login_checkbox(browser):
    browser.find_element(By.ID, "user_email").send_keys("test@gmail.com")
    browser.find_element(By.ID, "user_password").send_keys("123456")
    browser.find_element(By.ID, "user_remember_me").click()
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    browser.implicitly_wait(10)
    success_message = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert success_message == "Signed in successfully.", "Success message text does not match"


def test_valid_login(browser):
    browser.find_element(By.ID, "user_email").send_keys("test@gmail.com")
    browser.find_element(By.ID, "user_password").send_keys("123456")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    browser.implicitly_wait(10)
    success_message = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert success_message == "Signed in successfully.", "Success message text does not match"

def test_invalid_email(browser):
    browser.find_element(By.ID, "user_email").send_keys("testtest@gmail.com")
    browser.find_element(By.ID, "user_password").send_keys("123456")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    error_message = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert error_message == "Invalid Email or password.", "Error message text does not match"


def test_invalid_pwd(browser):
    browser.find_element(By.ID, "user_email").send_keys("test@gmail.com")
    browser.find_element(By.ID, "user_password").send_keys("123478")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    error_message = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert error_message == "Invalid Email or password.", "Error message text does not match"


def test_empty_pwd(browser):
    browser.find_element(By.ID, "user_email").send_keys("test@gmail.com")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    error_message = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert error_message == "Invalid Email or password.", "Error message text does not match"


def test_empty_email(browser):
    browser.find_element(By.ID, "user_password").send_keys("123456")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    error_message = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert error_message == "Invalid Email or password.", "Error message text does not match"






