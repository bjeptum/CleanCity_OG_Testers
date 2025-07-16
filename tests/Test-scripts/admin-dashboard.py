from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# Admnin dashboard

def dashboard_button():
    driver = webdriver.Chrome()  # Initialize the Chrome driver

    try:
        driver.get("http://127.0.0.1:5500/index.html")  # Navigate to the website

        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/nav/div/ul/li[2]/a[1]"))
        )
        login_button.click()  # Click the Register button
        time.sleep(2)

        # Admin login
        # Condition 2
        input_email_address = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-email"))
        )
        input_email_address.send_keys("admin@cleancity.com")  # Enter admin email
        time.sleep(2)

        input_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-password"))
        )
        input_password.send_keys("admin123")  # Enter admin password
        time.sleep(5)

        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div[4]/form/button"))
        )
        submit_button.click()  # Click the login button
        time.sleep(5)

        # Condition 3 : Admin updating requests

        admin_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/nav/div/ul/li[3]/a[3]"))
        )
        admin_page.click()  # Click the admin page link
        time.sleep(5)

        select_request = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[7]/div[2]/div/div[1]/select"))
        )
        select_request.send_keys("REQ006 - user (Nairobi)")
        time.sleep(5)

        select_status = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[7]/div[2]/div/div[2]/select"))
        )
        select_status.send_keys("Completed")
        time.sleep(5)

        # submit button

        update_status_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "updateStatusBtn"))
        )
        update_status_button.click()
        time.sleep(2)

        # Handle the alert
        try:
            alert = driver.switch_to.alert
            print("Alert text:", alert.text)
            alert.accept()
            time.sleep(1)
        except:
            print("No alert present.")

        print("Current URL:", driver.current_url)
        assert "127.0.0.1:5500/index.html" in driver.current_url, "URL does not contain 'login'"
        print("Login button clicked successfully.")
        print("Admin login successful")
        print("Update successful")

    finally:
        driver.quit()

# Calling the function
dashboard_button()

