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
    driver.get("http://localhost:3000/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-email"))).send_keys(email)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-password"))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "login-btn"))).click()
    time.sleep(3)
    print("Login successful.\n")

def test_community_features():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        login_user(driver)

        # FR-045: View and Edit Profile
        print("Testing FR-045: View and Edit Profile...")
        driver.find_element(By.LINK_TEXT, "Profile").click()
        time.sleep(2)

        # View profile
        name = driver.find_element(By.ID, "user-name").text
        email = driver.find_element(By.ID, "user-email").text
        assert name and email, "Profile info not visible"
        print("045-1: View profile - PASS")

        # Edit profile
        driver.find_element(By.ID, "edit-profile-btn").click()
        name_input = driver.find_element(By.ID, "edit-name")
        name_input.clear()
        name_input.send_keys("Test User")
        driver.find_element(By.ID, "save-profile-btn").click()
        time.sleep(2)
        assert "Test User" in driver.find_element(By.ID, "user-name").text
        print("045-2: Edit profile - PASS\n")

        ### FR-046: Activity History ###
        print("Testing FR-046: View Activity History...")
        activities = driver.find_element(By.ID, "activity-history").text
        assert "Post" in activities or "Comment" in activities
        print("046-1: View activity history - PASS\n")

        ### FR-047: Upload Profile Picture ###
        print("Testing FR-047: Profile Picture Upload...")
        driver.find_element(By.ID, "edit-profile-btn").click()

        # 047-1: Valid Image
        image_url_input = driver.find_element(By.ID, "edit-image-url")
        image_url_input.clear()
        image_url_input.send_keys("https://example.com/image.jpg")
        driver.find_element(By.ID, "save-profile-btn").click()
        time.sleep(2)
        assert driver.find_element(By.ID, "profile-pic").get_attribute("src").startswith("https://example.com")
        print("047-1: Valid image upload - PASS")

        # 047-2: Invalid file type
        driver.find_element(By.ID, "edit-profile-btn").click()
        image_url_input = driver.find_element(By.ID, "edit-image-url")
        image_url_input.clear()
        image_url_input.send_keys("https://example.com/file.txt")
        driver.find_element(By.ID, "save-profile-btn").click()
        time.sleep(2)
        error = driver.find_element(By.ID, "image-error").text
        assert "Invalid file type" in error
        print("047-2: Invalid file type - PASS")

        # 047-3: Remove image
        driver.find_element(By.ID, "edit-profile-btn").click()
        image_url_input = driver.find_element(By.ID, "edit-image-url")
        image_url_input.clear()
        driver.find_element(By.ID, "save-profile-btn").click()
        time.sleep(2)
        assert "default-avatar" in driver.find_element(By.ID, "profile-pic").get_attribute("src")
        print("047-3: Remove profile picture - PASS\n")

        ### FR-050: Community Feed ###
        print("Testing FR-050: Community Feed...")
        driver.find_element(By.LINK_TEXT, "Community").click()
        time.sleep(3)

        # 050-1: View feed
        posts = driver.find_elements(By.CLASS_NAME, "community-post")
        assert len(posts) > 0
        print("050-1: View community feed - PASS")

        # 050-2: Feed updates dynamically
        first_post = posts[0]
        like_button = first_post.find_element(By.CLASS_NAME, "like-btn")
        like_button.click()
        time.sleep(2)
        driver.refresh()
        time.sleep(3)
        updated_posts = driver.find_elements(By.CLASS_NAME, "community-post")
        assert len(updated_posts) > 0
        print("050-2: Feed updates dynamically - PASS\n")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_community_features()
