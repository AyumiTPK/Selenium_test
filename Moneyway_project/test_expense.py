from selenium.webdriver.common.by import By
import pytest
from conftest import logged_in_driver, add_expense, navigate_to_expense_page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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


def test_remove_expense(logged_in_driver):
    # Add an expense to be removed later
    title_to_remove = "Test Remove"
    add_expense(logged_in_driver, title_to_remove, "Groceries", "Test description", "30", "2024-07-07")
    assert check_success_message(logged_in_driver, "Expense was created successfully.")

    # Wait for the expense row containing the title_to_remove
    expense_row_xpath = f'//tr[.//a[text()="{title_to_remove}"]]'
    expense_row = WebDriverWait(logged_in_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, expense_row_xpath))
    )

    # Optionally, perform actions on the found expense_row
    # For example, clicking the delete button within the row
    delete_button = expense_row.find_element(By.CSS_SELECTOR, 'a[href*="/expenses/"]')
    delete_button.click()

    # Handle the confirmation pop-up
    alert = Alert(logged_in_driver)

    # Optionally, assert the text of the alert message
    assert "Are you sure?" in alert.text  # Adjust the text according to your application

    # Accept the alert (confirm the action)
    alert.accept()

    assert not logged_in_driver.find_elements(By.LINK_TEXT, title_to_remove)