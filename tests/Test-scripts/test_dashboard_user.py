from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_dashboard_user():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        print("Navigating to the application...")
        driver.get("http://localhost:3000/")
        print("Page title after navigation:", driver.title)

        # Test Case: Display personalized dashboard
        print("Attempting to find login email field...")
        input_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-email"))
        )
        print("Login email field found.")
        input_email.send_keys("mpumelaqq@gmail.com")
        time.sleep(2)

        print("Attempting to find login password field...")
        input_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-password"))
        )
        print("Login password field found.")
        input_password.send_keys("1234566")
        time.sleep(2)

        print("Attempting to find login button...")
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "login-btn"))
        )
        print("Login button found.")
        login_button.click()
        time.sleep(5)

        # Test Case: View recent pickup requests
        print("Attempting to find recent pickups...")
        recent_pickups = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "recentPickups"))
        )
        print("Recent pickups found.")
        recent_pickups.click()
        time.sleep(2)

        # Test Case: View upcoming scheduled pickups
        print("Attempting to find scheduled pickups...")
        scheduled_pickups = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "scheduledPickups"))
        )
        print("Scheduled pickups found.")
        scheduled_pickups.click()
        time.sleep(2)

        # Test Case: View environmental impact stats
        print("Attempting to find impact stats...")
        impact_stats = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "impactStats"))
        )
        print("Impact stats found.")
        impact_stats.click()
        time.sleep(2)

        # Test Case: View achievement badges
        print("Attempting to find achievement badges...")
        achievement_badges = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "achievementBadges"))
        )
        print("Achievement badges found.")
        achievement_badges.click()
        time.sleep(2)

        # Test Case: Use quick action buttons
        print("Attempting to find quick action...")
        quick_action = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "quickAction"))
        )
        print("Quick action found.")
        quick_action.click()
        time.sleep(2)

        # Test Case: Calculate & display total waste diverted
        print("Attempting to find total waste...")
        total_waste = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "totalWaste"))
        )
        print("Total waste found.")
        total_waste.click()
        time.sleep(2)

        # Test Case: Calculate & display CO2 saved
        print("Attempting to find co2 saved...")
        co2_saved = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "co2Saved"))
        )
        print("CO2 saved found.")
        co2_saved.click()
        time.sleep(2)

        # Test Case: Calculate & display trees equivalent
        print("Attempting to find trees equivalent...")
        trees_equivalent = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "treesEquivalent"))
        )
        print("Trees equivalent found.")
        trees_equivalent.click()
        time.sleep(2)

        print("Dashboard tests completed successfully.")

    finally:
        driver.quit()

# Calling the test function
test_dashboard_user()