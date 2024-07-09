import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_LOGIN = 'https://moneyway.fly.dev/users/sign_in'
URL_HOME = 'https://moneyway.fly.dev/daybooks'


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def login(driver, email, password):
    driver.get(URL_LOGIN)
    driver.find_element(By.ID, "user_email").send_keys(email)
    driver.find_element(By.ID, "user_password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "btn-primary").click()

def navigate_to_expense_page(driver):
    driver.get(URL_HOME)
    driver.find_element(By.CSS_SELECTOR, 'a[href="/expenses"]').click()
    driver.find_element(By.CSS_SELECTOR, 'a[href="/expenses/new"]').click()

def test_add_expense(driver):
    login(driver, "test@gmail.com", "123456")
    navigate_to_expense_page(driver)

    driver.find_element(By.ID, "expense_title").send_keys("Supermarket")
    dropdown = Select(driver.find_element(By.ID, "expense_expense_type_id"))
    dropdown.select_by_visible_text("Groceries")
    driver.find_element(By.ID, "expense_description").send_keys("Usual shopping")
    driver.find_element(By.ID, "expense_amount").send_keys("50")
    driver.find_element(By.ID, "expense_date").send_keys("2024-07-07")
    driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
    success_message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert success_message == "Expense was created successfully."

def test_add_exceptional_expense(driver):
    login(driver, "test@gmail.com", "123456")
    navigate_to_expense_page(driver)

    driver.find_element(By.ID, "expense_title").send_keys("Shoes")
    dropdown = Select(driver.find_element(By.ID, "expense_expense_type_id"))
    dropdown.select_by_visible_text("Hobbies")
    driver.find_element(By.ID, "expense_description").send_keys("Running")
    driver.find_element(By.ID, "expense_amount").send_keys("100")
    driver.find_element(By.ID, "expense_date").send_keys("2024-07-07")
    driver.find_element(By.ID, "expense_exceptional_expense").click()
    driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
    success_message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert success_message == "Expense was created successfully."



def test_invalid_expense(driver):
    login(driver, "test@gmail.com", "123456")
    navigate_to_expense_page(driver)

    driver.find_element(By.ID, "expense_title").send_keys("Shoes")
    dropdown = Select(driver.find_element(By.ID, "expense_expense_type_id"))
    dropdown.select_by_visible_text("Social life")
    driver.find_element(By.ID, "expense_description").send_keys("Birthday")
    driver.find_element(By.ID, "expense_amount").send_keys("")
    driver.find_element(By.ID, "expense_date").send_keys("2024-07-09")
    driver.find_element(By.ID, "expense_exceptional_expense").click()
    driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
    success_message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert success_message != "Expense was created successfully."