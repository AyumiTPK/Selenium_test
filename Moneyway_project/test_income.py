# Locate the expense to remove by title
expense_link = logged_in_driver.find_element(By.LINK_TEXT, title_to_remove)
expense_id = expense_link.get_attribute("href").split("/")[-1]
delete_url = f"/expenses/{expense_id}"
# Construct the CSS selector dynamically
delete_selector = f'a[href="{delete_url}"]'
# Click the delete link
delete_link = logged_in_driver.find_element(By.CSS_SELECTOR, delete_selector)
delete_link.click()



