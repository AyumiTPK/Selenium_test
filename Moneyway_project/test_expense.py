from selenium.webdriver.common.by import By
import pytest
from conftest import logged_in_driver, add_expense, navigate_to_expense_page




def check_success_message(driver, expected_message):
    success_message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    return success_message == expected_message

def test_add_expense(logged_in_driver):
    add_expense(logged_in_driver, "Supermarket", "Groceries", "Usual shopping", "50", "2024-07-07", exceptional=False)
    assert check_success_message(logged_in_driver, "Expense was created successfully.")


def test_add_exceptional_expense(logged_in_driver):
    add_expense(logged_in_driver, "Shoes", "Hobbies", "Running", "100", "2024-07-07", exceptional=True)
    assert check_success_message(logged_in_driver, "Expense was created successfully.")


def test_invalid_expense(logged_in_driver):
    add_expense(logged_in_driver, "Shoes", "Social life", "Birthday", "", "2024-07-09", exceptional=True)
    assert not check_success_message(logged_in_driver, "Expense was created successfully.")
