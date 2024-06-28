from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start a new browser session
driver = webdriver.Chrome()

# Step 1: Navigate to saucedemo.com
driver.get("https://www.saucedemo.com/")

# Step 2: Capture and display cookies before login
cookies_before_login = driver.get_cookies()
print("Cookies before login:")
for cookie in cookies_before_login:
    print(cookie)

# Step 3: Perform login
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()

# Wait for dashboard to load
WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))

# Step 4: Capture and display cookies after login
cookies_after_login = driver.get_cookies()
print("\nCookies after login:")
for cookie in cookies_after_login:
    print(cookie)

# Step 5: Verify that cookies were generated during login process
if len(cookies_after_login) > len(cookies_before_login):
    print("\nCookies were generated during login process.")
else:
    print("\nNo new cookies were generated during login process.")

# Step 6: Perform logout
logout_button = driver.find_element(By.ID, "react-burger-menu-btn")
logout_button.click()

logout_link = driver.find_element(By.ID, "logout_sidebar_link")
logout_link.click()

# Close the browser session
driver.quit()
