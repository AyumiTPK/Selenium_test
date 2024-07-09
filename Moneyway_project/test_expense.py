from selenium.webdriver.common.by import By
import pytest
from conftest import logged_in_driver, add_expense, navigate_to_expense_page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert



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

    # Navigate to expense page
    navigate_to_expense_page(logged_in_driver)

    # Locate the expense to remove by title
    expense_link = logged_in_driver.find_element(By.LINK_TEXT, title_to_remove)
    expense_id = expense_link.get_attribute("href").split("/")[-1]

    # Construct the delete URL
    delete_url = f"/expenses/{expense_id}"

    # Click the remove button (if directly available)
    # In case the remove button is not available directly, navigate to the edit page
    # and click the delete button there
    logged_in_driver.get(delete_url)

    # Handle the confirmation pop-up
    alert = Alert(logged_in_driver)
    alert.accept()

    # Verify that the expense is no longer present
    navigate_to_expense_page(logged_in_driver)
    expense_links = logged_in_driver.find_elements(By.CSS_SELECTOR, 'a[href^="/expenses/"]')
    expense_titles = [link.text for link in expense_links]
    assert title_to_remove not in expense_titles