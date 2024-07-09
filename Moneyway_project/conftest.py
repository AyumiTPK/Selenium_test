import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL_SIGNUP = 'https://moneyway.fly.dev/users/sign_up'
URL_LOGIN = 'https://moneyway.fly.dev/users/sign_in'
URL_HOME = 'https://moneyway.fly.dev/daybooks'


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def signup_page(driver):
    driver.get(URL_SIGNUP)
    return driver


@pytest.fixture
def login_page(driver):
    driver.get(URL_LOGIN)
    return driver


@pytest.fixture
def logged_in_driver(driver):
    login(driver, "test@gmail.com", "123456")
    return driver


def login(driver, email, password):
    driver.get(URL_LOGIN)
    driver.find_element(By.ID, "user_email").send_keys(email)
    driver.find_element(By.ID, "user_password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "btn-primary").click()


def register(driver, email, password, password_confirmation, currency="EUR"):
    driver.find_element(By.ID, "user_email").send_keys(email)
    dropdown = Select(driver.find_element(By.ID, "user_currency"))
    dropdown.select_by_visible_text(currency)
    driver.find_element(By.ID, "user_password").send_keys(password)
    driver.find_element(By.ID, "user_password_confirmation").send_keys(password_confirmation)
    driver.find_element(By.CLASS_NAME, "btn-primary").click()


def navigate_to_expense_page(driver):
    driver.get(URL_HOME)
    driver.find_element(By.CSS_SELECTOR, 'a[href="/expenses"]').click()
    driver.find_element(By.CSS_SELECTOR, 'a[href="/expenses/new"]').click()


def add_expense(driver, title, types, description, amount, date, exceptional=False):
    navigate_to_expense_page(driver)

    driver.find_element(By.ID, "expense_title").send_keys(title)
    dropdown = Select(driver.find_element(By.ID, "expense_expense_type_id"))
    dropdown.select_by_visible_text(types)
    driver.find_element(By.ID, "expense_description").send_keys(description)
    driver.find_element(By.ID, "expense_amount").send_keys(amount)
    driver.find_element(By.ID, "expense_date").send_keys(date)

    if exceptional:
        driver.find_element(By.ID, "expense_exceptional_expense").click()

    driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()

