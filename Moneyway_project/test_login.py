import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from conftest import login, URL_LOGIN, URL_HOME

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

def test_valid_login(login_page):
    login(login_page, "test@gmail.com", "123456")
    verify_successful_login(login_page)

def test_invalid_email(login_page):
    login(login_page, "testtest@gmail.com", "123456")
    verify_unsuccessful_login(login_page)

def test_invalid_pwd(login_page):
    login(login_page, "test@gmail.com", "123478")
    verify_unsuccessful_login(login_page)

def test_empty_pwd(login_page):
    login_page.find_element(By.ID, "user_email").send_keys("test@gmail.com")
    login_page.find_element(By.CLASS_NAME, "btn-primary").click()
    verify_unsuccessful_login(login_page)

def test_empty_email(login_page):
    login_page.find_element(By.ID, "user_password").send_keys("123456")
    login_page.find_element(By.CLASS_NAME, "btn-primary").click()
    verify_unsuccessful_login(login_page)

def test_valid_login_checkbox(login_page):
    login(login_page, "test@gmail.com", "123456", remember_me=True)
    verify_successful_login(login_page)

    login_page.quit()

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(URL_HOME)

    assert driver.find_element(By.CSS_SELECTOR, "a[href='/users/sign_out']").is_displayed()
    driver.quit()


def test_valid_login_without_checkbox(login_page):
    login(login_page, "test@gmail.com", "123456", remember_me=False)
    verify_successful_login(login_page)

    login_page.quit()

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(URL_HOME)

    signin_message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert signin_message == "You need to sign in or sign up before continuing."

def verify_successful_login(driver):
    success_message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert success_message == "Signed in successfully."


def verify_unsuccessful_login(driver):
    error_message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert error_message == "Invalid Email or password."