import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

URL = 'https://moneyway.fly.dev/users/sign_up'


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
    link = browser.find_element(By.CSS_SELECTOR, 'a[href="/users/sign_in"]')
    link.click()


def test_complete_valid_form(browser):
    browser.find_element(By.ID, "user_email").send_keys("amy.jones@gmail.com")
    dropdown = Select(browser.find_element(By.ID, "user_currency"))
    dropdown.select_by_visible_text("EUR")
    browser.find_element(By.ID, "user_password").send_keys("password1234")
    browser.find_element(By.ID, "user_password_confirmation").send_keys("password1234")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    assert browser.current_url == "https://moneyway.fly.dev/users", "The login was not successful, URL does not match."


def test_short_pwd(browser):
    browser.find_element(By.ID, "user_email").send_keys("amy.jones@gmail.com")
    dropdown = Select(browser.find_element(By.ID, "user_currency"))
    dropdown.select_by_visible_text("EUR")
    browser.find_element(By.ID, "user_password").send_keys("pas")
    browser.find_element(By.ID, "user_password_confirmation").send_keys("pas")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    assert browser.current_url != "https://moneyway.fly.dev/users", "The login was not successful, URL does not match."


def test_wrong_pwd(browser):
    browser.find_element(By.ID, "user_email").send_keys("amy.jones@gmail.com")
    dropdown = Select(browser.find_element(By.ID, "user_currency"))
    dropdown.select_by_visible_text("EUR")
    browser.find_element(By.ID, "user_password").send_keys("pass123")
    browser.find_element(By.ID, "user_password_confirmation").send_keys("pas123")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    assert browser.current_url != "https://moneyway.fly.dev/users", "The login was not successful, URL does not match."


def test_empty_pwd(browser):
    browser.find_element(By.ID, "user_email").send_keys("amy.jones@gmail.com")
    dropdown = Select(browser.find_element(By.ID, "user_currency"))
    dropdown.select_by_visible_text("EUR")
    browser.find_element(By.ID, "user_password").send_keys("")
    browser.find_element(By.ID, "user_password_confirmation").send_keys("")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    assert browser.current_url != "https://moneyway.fly.dev/users", "The login was not successful, URL does not match."


def test_invalid_email(browser):
    browser.find_element(By.ID, "user_email").send_keys("amy.jones.gmail.com")
    dropdown = Select(browser.find_element(By.ID, "user_currency"))
    dropdown.select_by_visible_text("EUR")
    browser.find_element(By.ID, "user_password").send_keys("password1234")
    browser.find_element(By.ID, "user_password_confirmation").send_keys("password1234")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    assert browser.current_url != "https://moneyway.fly.dev/users", "The login was not successful, URL does not match."


def test_empty_email(browser):
    browser.find_element(By.ID, "user_email").send_keys("")
    dropdown = Select(browser.find_element(By.ID, "user_currency"))
    dropdown.select_by_visible_text("EUR")
    browser.find_element(By.ID, "user_password").send_keys("password1234")
    browser.find_element(By.ID, "user_password_confirmation").send_keys("password1234")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    assert browser.current_url != "https://moneyway.fly.dev/users", "The login was not successful, URL does not match."


def test_registered_email(browser):
    browser.find_element(By.ID, "user_email").send_keys("test@gmail.com")
    dropdown = Select(browser.find_element(By.ID, "user_currency"))
    dropdown.select_by_visible_text("EUR")
    browser.find_element(By.ID, "user_password").send_keys("password1234")
    browser.find_element(By.ID, "user_password_confirmation").send_keys("password1234")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    assert browser.current_url != "https://moneyway.fly.dev/users", "The login was not successful, URL does not match."

