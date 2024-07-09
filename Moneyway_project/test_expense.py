from selenium.webdriver.common.by import By
import pytest
from conftest import logged_in_driver, add_expense, navigate_to_expense_page




def check_success_message(driver, expected_message):
    success_message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    return success_message == expected_message

def test_add_expense(logged_in_driver):
    add_expense(logged_in_driver, "Supermarket", "Groceries", "Usual shopping", "50", "2024-07-07")
    assert check_success_message(logged_in_driver, "Expense was created successfully.")


def test_add_exceptional_expense(logged_in_driver):
    add_expense(logged_in_driver, "Shoes", "Hobbies", "Running", "100", "2024-07-07")
    assert check_success_message(logged_in_driver, "Expense was created successfully.")



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
