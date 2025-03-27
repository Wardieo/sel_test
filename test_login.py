from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
import time

# Setup WebDriver
driver = webdriver.Chrome()

# Start timer
start_time = time.time()

# Navigate to login page
driver.get("http://localhost:3000/login")

# Find the email and password fields
email_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")

# Enter test credentials
email_input.send_keys("test@example.com")  # Use incorrect credentials
password_input.send_keys("wrongpassword")
password_input.send_keys(Keys.RETURN)

# Wait for response
time.sleep(2)

# Handle alert popup if present
alert_text = "No Alert"
try:
    alert = driver.switch_to.alert
    alert_text = alert.text  # Capture alert text
    alert.accept()  # Close the alert
except NoAlertPresentException:
    pass  # No alert was present

# Capture the body text after handling alert
page_text = driver.find_element(By.TAG_NAME, "body").text

# Stop timer
end_time = time.time()
execution_time = end_time - start_time

# Save results to a file
with open("selenium_test_results.txt", "w") as file:
    file.write(f"Test Case: Login Form Validation\n")
    file.write(f"Execution Time: {execution_time:.2f} seconds\n")
    file.write(f"Alert Message: {alert_text}\n")
    file.write(f"Page Text After Login Attempt:\n{page_text}\n")

# Print results to console
print(f"Execution Time: {execution_time:.2f} seconds")
print(f"Alert Message: {alert_text}")
print("Login Test Completed. Results saved to selenium_test_results.txt")

# Close browser
driver.quit()
