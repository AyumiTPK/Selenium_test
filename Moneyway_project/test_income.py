
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def navigate_to_expense_page(driver):
    driver.get("https://moneyway.fly.dev/daybooks")
    driver.find_element(By.CSS_SELECTOR, 'a[href="/expenses"]').click()
    driver.find_element(By.CSS_SELECTOR, 'a[href="/expenses/new"]').click()

def test_add_expense(logged_in_driver):
    driver = logged_in_driver
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

def test_add_exceptional_expense(logged_in_driver):
    driver = logged_in_driver
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

def test_invalid_expense(logged_in_driver):
    driver = logged_in_driver
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





