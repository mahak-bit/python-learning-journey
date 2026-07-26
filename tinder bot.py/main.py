from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ==========================================
# 1. START CHROME
# ==========================================

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 15)


# ==========================================
# 2. OPEN TINDER
# ==========================================

driver.get("https://tinder.com/")

time.sleep(5)


# ==========================================
# 3. LOGIN MANUALLY
# ==========================================

print("Please log in to Tinder manually.")
input("After logging in, press Enter here...")


# ==========================================
# 4. HANDLE LOCATION POP-UP
# ==========================================

try:
    not_interested_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Not interested')]")
        )
    )

    not_interested_button.click()

except Exception:
    print("Location pop-up not found.")


# ==========================================
# 5. HANDLE NOTIFICATION POP-UP
# ==========================================

try:
    not_interested_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Not interested')]")
        )
    )

    not_interested_button.click()

except Exception:
    print("Notification pop-up not found.")


# ==========================================
# 6. START SWIPING
# ==========================================

for i in range(10):

    try:

        # Find the Like button
        like_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@aria-label='Like']")
            )
        )

        # Click Like
        like_button.click()

        print(f"Profile {i + 1} liked ❤️")

        # Wait before next profile
        time.sleep(2)

    except Exception as e:

        print("Could not click Like button.")
        print(e)

        break


# ==========================================
# 7. FINISH
# ==========================================

print("Swiping automation finished!")

input("Press Enter to close the browser...")

driver.quit()