import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException




URL = 'https://qa-practice.netlify.app/bugs-form.html'


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()


def test_validate_title(browser):
    expected_title = "QA Practice | Learn with RV"
    assert browser.title == expected_title


def test_click_button(browser):
    button = browser.find_element(By.ID, "registerBtn")
    button.click()


def test_click_link(browser):
    try:
        link = browser.find_element(By.LINK_TEXT, "More information")
        # If the element is found, click it and fail the test intentionally
        link.click()
        pytest.fail("Intentional failure for testing purposes")
    except NoSuchElementException:
        # If NoSuchElementException is raised, pass the test
        pass


def test_complete_valid_form(browser):
    browser.find_element(By.ID, "firstName").send_keys("Amy")
    browser.find_element(By.ID, "lastName").send_keys("Jones")
    browser.find_element(By.ID, "phone").send_keys("12345678910")
    dropdown = Select(browser.find_element(By.ID, "countries_dropdown_menu"))
    dropdown.select_by_visible_text("Australia")
    browser.find_element(By.ID, "emailAddress").send_keys("amy.jones@gmail.com")
    browser.find_element(By.ID, "password").send_keys("password1234")
    browser.find_element(By.ID, "exampleCheck1").click()
    browser.find_element(By.ID, "registerBtn").click()
    success_message = browser.find_element(By.ID, "message")
    assert success_message.text == "Successfully registered the following information", "Success message text does not match"

def test_phone_number_min_length(browser):
    browser.find_element(By.ID, "firstName").send_keys("Amy")
    browser.find_element(By.ID, "lastName").send_keys("Jones")
    browser.find_element(By.ID, "phone").send_keys("12")
    dropdown = Select(browser.find_element(By.ID, "countries_dropdown_menu"))
    dropdown.select_by_visible_text("Australia")
    browser.find_element(By.ID, "emailAddress").send_keys("amy.jones@gmail.com")
    browser.find_element(By.ID, "password").send_keys("password1234")
    browser.find_element(By.ID, "exampleCheck1").click()
    browser.find_element(By.ID, "registerBtn").click()
    success_message = browser.find_element(By.ID, "message")
    assert success_message.text == "The phone number should contain at least 10 characters!", "Success message text does not match"

def test_select_country(browser):
    browser.find_element(By.ID, "firstName").send_keys("Amy")
    browser.find_element(By.ID, "lastName").send_keys("Jones")
    browser.find_element(By.ID, "phone").send_keys("12345678910")
    dropdown = Select(browser.find_element(By.ID, "countries_dropdown_menu"))
    dropdown.select_by_visible_text("Australia")
    browser.find_element(By.ID, "emailAddress").send_keys("amy.jones@gmail.com")
    browser.find_element(By.ID, "password").send_keys("password1234")
    browser.find_element(By.ID, "exampleCheck1").click()
    browser.find_element(By.ID, "registerBtn").click()
    success_message = browser.find_element(By.ID, "message")
    assert success_message.text == "Successfully registered the following information", "Success message text does not match"

def test_email_format(browser):
    browser.find_element(By.ID, "firstName").send_keys("Amy")
    browser.find_element(By.ID, "lastName").send_keys("Jones")
    browser.find_element(By.ID, "phone").send_keys("12345678910")
    dropdown = Select(browser.find_element(By.ID, "countries_dropdown_menu"))
    dropdown.select_by_visible_text("Australia")
    browser.find_element(By.ID, "emailAddress").send_keys("amy.jones@gmail.com")
    browser.find_element(By.ID, "password").send_keys("password1234")
    browser.find_element(By.ID, "exampleCheck1").click()
    browser.find_element(By.ID, "registerBtn").click()
    success_message = browser.find_element(By.ID, "message")
    assert success_message.text == "Successfully registered the following information", "Success message text does not match"

def test_password_strength(browser):
    browser.find_element(By.ID, "firstName").send_keys("Amy")
    browser.find_element(By.ID, "lastName").send_keys("Jones")
    browser.find_element(By.ID, "phone").send_keys("12345678910")
    dropdown = Select(browser.find_element(By.ID, "countries_dropdown_menu"))
    dropdown.select_by_visible_text("Australia")
    browser.find_element(By.ID, "emailAddress").send_keys("amy.jones@gmail.com")
    browser.find_element(By.ID, "password").send_keys("password1234")
    browser.find_element(By.ID, "exampleCheck1").click()
    browser.find_element(By.ID, "registerBtn").click()
    success_message = browser.find_element(By.ID, "message")
    assert success_message.text == "Successfully registered the following information", "Success message text does not match"


def test_empty_fields(browser):
    browser.find_element(By.ID, "registerBtn").click()
    error_message_last_name = browser.find_element(By.ID, "message")
    error_message_phone = browser.find_element(By.ID, "message")
    error_message_email = browser.find_element(By.ID, "message")
    error_message_password = browser.find_element(By.ID, "message")
    error_message_checkbox = browser.find_element(By.ID, "message")
    assert error_message_last_name.text != "Successfully registered the following information", \
        "Unexpected success message displayed for invalid last name format"
    assert error_message_phone.text != "Successfully registered the following information", \
        "Unexpected success message displayed for invalid phone number format"
    assert error_message_email.text != "Successfully registered the following information", \
        "Unexpected success message displayed for invalid email format"
    assert error_message_password.text != "Successfully registered the following information", \
        "Unexpected success message displayed for invalid password format"
    assert error_message_checkbox.text != "Successfully registered the following information", \
        "Unexpected success message displayed for checkbox"


def test_invalid_email_format(browser):
    browser.find_element(By.ID, "firstName").send_keys("Amy")
    browser.find_element(By.ID, "lastName").send_keys("Jones")
    browser.find_element(By.ID, "phone").send_keys("12345678910")
    dropdown = Select(browser.find_element(By.ID, "countries_dropdown_menu"))
    dropdown.select_by_visible_text("Australia")
    browser.find_element(By.ID, "emailAddress").send_keys("amy.jones.gmail.com")
    browser.find_element(By.ID, "password").send_keys("password1234")
    browser.find_element(By.ID, "exampleCheck1").click()
    browser.find_element(By.ID, "registerBtn").click()
    error_message = browser.find_element(By.ID, "message")
    assert error_message.text != "Successfully registered the following information", \
        "Unexpected success message displayed for invalid email format"

def test_short_password(browser):
    browser.find_element(By.ID, "firstName").send_keys("Amy")
    browser.find_element(By.ID, "lastName").send_keys("Jones")
    browser.find_element(By.ID, "phone").send_keys("12345678910")
    dropdown = Select(browser.find_element(By.ID, "countries_dropdown_menu"))
    dropdown.select_by_visible_text("Australia")
    browser.find_element(By.ID, "emailAddress").send_keys("amy.jones@gmail.com")
    browser.find_element(By.ID, "password").send_keys("pass")
    browser.find_element(By.ID, "exampleCheck1").click()
    browser.find_element(By.ID, "registerBtn").click()
    error_message = browser.find_element(By.ID, "message")
    assert error_message.text == "The password should contain between [6,20] characters!", "Error message text does not match"

def test_unchecked_checkbox(browser):
    browser.find_element(By.ID, "firstName").send_keys("Amy")
    browser.find_element(By.ID, "lastName").send_keys("Jones")
    browser.find_element(By.ID, "phone").send_keys("12345678910")
    dropdown = Select(browser.find_element(By.ID, "countries_dropdown_menu"))
    dropdown.select_by_visible_text("Australia")
    browser.find_element(By.ID, "emailAddress").send_keys("amy.jones@gmail.com")
    browser.find_element(By.ID, "password").send_keys("password1234")
    browser.find_element(By.ID, "registerBtn").click()
    error_message = browser.find_element(By.ID, "message")
    assert error_message.text != "Successfully registered the following information", \
        "Unexpected success message displayed for checkbox"

def test_invalid_phone_format(browser):
    browser.find_element(By.ID, "firstName").send_keys("Amy")
    browser.find_element(By.ID, "lastName").send_keys("Jones")
    browser.find_element(By.ID, "phone").send_keys("ncmsjfhxidf")
    dropdown = Select(browser.find_element(By.ID, "countries_dropdown_menu"))
    dropdown.select_by_visible_text("Australia")
    browser.find_element(By.ID, "emailAddress").send_keys("amy.jones@gmail.com")
    browser.find_element(By.ID, "password").send_keys("password1234")
    browser.find_element(By.ID, "exampleCheck1").click()
    browser.find_element(By.ID, "registerBtn").click()
    error_message = browser.find_element(By.ID, "message")
    assert error_message.text != "Successfully registered the following information", \
        "Unexpected success message displayed for checkbox"

def test_send_special_keys(browser):
    text_field = browser.find_element(By.ID, "firstName")
    text_field.send_keys(Keys.ENTER)

