import pytest
from selenium.webdriver.common.by import By
from conftest import login

def test_validate_title(login_page):
    expected_title = "Moneyway"
    assert login_page.title == expected_title

def test_click_button(login_page):
    button = login_page.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

def test_click_link(login_page):
    link = login_page.find_element(By.CSS_SELECTOR, 'a[href="/users/sign_up"]')
    link.click()
    assert login_page.current_url == "https://moneyway.fly.dev/users/sign_up"

def test_click_link_pwd(login_page):
    link = login_page.find_element(By.CSS_SELECTOR, 'a[href="/users/password/new"]')
    link.click()
    assert login_page.current_url == "https://moneyway.fly.dev/users/password/new"

def test_valid_login_checkbox(login_page):
    login(login_page, "test@gmail.com", "123456")
    success_message = login_page.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert success_message == "Signed in successfully."

def test_valid_login(login_page):
    login(login_page, "test@gmail.com", "123456")
    success_message = login_page.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert success_message == "Signed in successfully."

def test_invalid_email(login_page):
    login(login_page, "testtest@gmail.com", "123456")
    error_message = login_page.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert error_message == "Invalid Email or password."

def test_invalid_pwd(login_page):
    login(login_page, "test@gmail.com", "123478")
    error_message = login_page.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert error_message == "Invalid Email or password."

def test_empty_pwd(login_page):
    login_page.find_element(By.ID, "user_email").send_keys("test@gmail.com")
    login_page.find_element(By.CLASS_NAME, "btn-primary").click()
    error_message = login_page.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert error_message == "Invalid Email or password."

def test_empty_email(login_page):
    login_page.find_element(By.ID, "user_password").send_keys("123456")
    login_page.find_element(By.CLASS_NAME, "btn-primary").click()
    error_message = login_page.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert error_message == "Invalid Email or password."
