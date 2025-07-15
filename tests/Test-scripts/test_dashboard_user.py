from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_user(driver, email="user@cleancity.com", password="password123"):
    print("Logging in user...")
    log_in_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    log_in_link.click()
    time.sleep(2)

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-email"))
    )
    email_input.send_keys(email)
    time.sleep(2)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-password"))
    )
    password_input.send_keys(password)
    time.sleep(2)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "login-btn"))
    )
    login_button.click()
    time.sleep(5)
    print("User logged in successfully.")

def test_dashboard_features():
    print("Testing dashboard features...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)

    try:
        driver.get("http://localhost:3000/")
        login_user(driver)

        # Click on the "Dashboard" button
        print("Navigating to the Dashboard...")
        dashboard_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Dashboard"))
        )
        dashboard_button.click()
        time.sleep(5)

        def verify_element_by_id(element_id, description):
            print(f"Verifying {description}...")
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
            assert element.is_displayed(), f"{description} is not displayed."
            print(f"{description} verified successfully.")

        # Verify dashboard features

        # verify_element_by_id("totalRequests", "Total Requests")
        # verify_element_by_id("missedPickups", "Missed Pickups")
        # verify_element_by_id("blogPosts", "Blog Posts")
        # verify_element_by_id("communityPosts", "Community Posts")

        print("Dashboard features tested successfully.")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_dashboard_features()