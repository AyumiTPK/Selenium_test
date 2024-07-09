import pytest
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from conftest import register

def test_validate_title(signup_page):
    expected_title = "Moneyway"
    assert signup_page.title == expected_title

def test_click_button(signup_page):
    button = signup_page.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

def test_click_link(signup_page):
    link = signup_page.find_element(By.CSS_SELECTOR, 'a[href="/users/sign_in"]')
    link.click()

def test_complete_valid_form(signup_page):
    unique_email = f"amy+{int(time.time())}@gmail.com"
    register(signup_page, unique_email, "password1234", "password1234")
    success_message = signup_page.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert success_message == "Welcome! You have signed up successfully.", "Success message text does not match"


def test_short_pwd(signup_page):
    register(signup_page, "amy.jones@gmail.com", "pas", "pas")
    error_message = signup_page.find_element(By.ID, "error_explanation")
    assert error_message.is_displayed()

def test_wrong_pwd(signup_page):
    register(signup_page, "amy.jones@gmail.com", "pass123", "pas123")
    error_message = signup_page.find_element(By.ID, "error_explanation")
    assert error_message.is_displayed()

def test_empty_pwd(signup_page):
    register(signup_page, "amy.jones@gmail.com", "", "")
    error_message = signup_page.find_element(By.ID, "error_explanation")
    assert error_message.is_displayed()

def test_invalid_email(signup_page):
    register(signup_page, "amy.jones.gmail.com", "password1234", "password1234")
    assert signup_page.current_url != "https://moneyway.fly.dev/users", "The signup was not successful, URL does not match."

def test_empty_email(signup_page):
    register(signup_page, "", "password1234", "password1234")
    error_message = signup_page.find_element(By.ID, "error_explanation")
    assert error_message.is_displayed()

def test_registered_email(signup_page):
    register(signup_page, "test@gmail.com", "password1234", "password1234")
    error_message = signup_page.find_element(By.ID, "error_explanation")
    assert error_message.is_displayed()
