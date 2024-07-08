import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def browser():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def browser():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_duckduckgo_search(browser):
    # Navigate to DuckDuckGo
    browser.get("https://www.duckduckgo.com")

    # Test search functionality
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.submit()

    # Wait for search results to load
    time.sleep(2)

    # Verify search results page
    assert "Selenium Python" in browser.title


def test_duckduckgo_image_search(browser):
    # Navigate to DuckDuckGo
    browser.get("https://www.duckduckgo.com")

    # Test image search functionality
    image_button = browser.find_element(By.XPATH, "//a[@data-zci-link='images']")
    image_button.click()

    # Wait for image search results to load
    time.sleep(2)

    # Verify image search page
    assert "Images" in browser.title


def test_duckduckgo_video_search(browser):
    # Navigate to DuckDuckGo
    browser.get("https://www.duckduckgo.com")

    # Test video search functionality
    video_button = browser.find_element(By.XPATH, "//a[@data-zci-link='videos']")
    video_button.click()

    # Wait for video search results to load
    time.sleep(2)

    # Verify video search page
    assert "Videos" in browser.title

