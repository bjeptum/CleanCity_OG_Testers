from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# User registration and login authentication

def register_button():
    driver = webdriver.Chrome()  # Initialize the Chrome driver

    try:
        driver.get("http://localhost:3000/")  # Navigate to the website

        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        )
        register_button.click()  # Click the Register button
        time.sleep(5)

        # Filling in the sign-up form
        # Condition 2
        input_full_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "register-name"))
        )
        input_full_name.send_keys("User123")  # Enter fullname
        time.sleep(2)

        input_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "register-email"))
        )
        input_email.send_keys("user123@gmail.com")  # Enter email
        time.sleep(2)

        input_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "register-password"))
        )
        input_password.send_keys("1234566")  # Enter password
        time.sleep(2)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "register-btn"))
        )
        submit_button.click()  # Click the submit button
        time.sleep(2)

        # Logging in with the registered user details
        # Condition 3   
        input_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-email"))
        )
        input_email.send_keys("user123@gmail.com")  # Enter user-email
        time.sleep(2)

        input_password = WebDriverWait(driver, 10).until(   
            EC.presence_of_element_located((By.ID, "login-password"))
        )
        input_password.send_keys("1234566")  # Enter user-password
        time.sleep(2)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "login-btn"))
        )
        login_button.click()  # Click the login button
        time.sleep(5)

        # Condition 4
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "nav-logout"))
        )
        logout_button.click() # Click the logout button
        time.sleep(2)

        print("Current URL:", driver.current_url)
        assert "localhost:3000" in driver.current_url, "URL does not contain 'login'"
        print("Register button clicked successfully.")
        print("Sign-up form filled successfully.")
        print("Submit register-button clicked successfully.")
        print("Login successful")
        print("Logout successful")
        

    finally:
        driver.quit()

# Calling the test function
register_button()