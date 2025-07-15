from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date, timedelta
import time

def login_user(driver, email="user1@test.com", password="TestPass123"):
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

def fill_schedule_form(driver, with_desc=False):
    print("Filling schedule form...")
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "home-name"))
    )
    name_input.send_keys("John Doe")
    time.sleep(2)

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "home-email"))
    )
    email_input.send_keys("user1@test.com")
    time.sleep(2)

    location_select = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "home-location"))
    ))
    location_select.select_by_value("Mombasa")
    time.sleep(2)

    waste_select = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "home-waste"))
    ))
    waste_select.select_by_value("General Waste")
    time.sleep(2)

    pickup_date = (date.today() + timedelta(days=2)).strftime("%Y-%m-%d")
    date_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "home-date"))
    )
    date_input.send_keys(pickup_date)
    time.sleep(2)

    if with_desc:
        desc_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "home-desc"))
        )
        desc_input.send_keys("Leave near the gate.")
        time.sleep(2)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "home-btn"))
    )
    submit_button.click()
    time.sleep(5)
    print("Schedule form submitted successfully.")

def test_schedule_pickup_without_description():
    print("Testing schedule pickup without description...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://localhost:3000")
        login_user(driver)
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Schedule Pickup"))
        )
        link.click()
        time.sleep(2)
        fill_schedule_form(driver, with_desc=False)
        print("Test for pickup without description completed successfully.")
    finally:
        driver.quit()

def test_schedule_pickup_with_description():
    print("Testing schedule pickup with description...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://localhost:3000/")
        login_user(driver)
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Schedule Pickup"))
        )
        link.click()
        time.sleep(2)
        fill_schedule_form(driver, with_desc=True)
        print("Test for pickup with description completed successfully.")
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Starting tests...")
    test_schedule_pickup_without_description()
    test_schedule_pickup_with_description()
    print("All tests completed successfully.")