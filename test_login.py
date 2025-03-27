from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

# Setup WebDriver
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://localhost:3000/login")

# Find the email and password fields
email_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")

# Enter test credentials
email_input.send_keys("test@example.com")
password_input.send_keys("wrongpassword")
password_input.send_keys(Keys.RETURN)

# Wait and capture result
time.sleep(2)
error_message = driver.find_element(By.TAG_NAME, "body").text
print("Login Test Result:", error_message)

# Close browser
driver.quit()
