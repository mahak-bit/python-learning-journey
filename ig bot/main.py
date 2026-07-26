from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ==============================
# CONFIGURATION
# ==============================

TARGET_PROFILE = "instagram"  # Change this to the profile you want to visit
FOLLOW_LIMIT = 20             # Maximum number of accounts to follow


# ==============================
# SETUP CHROME
# ==============================

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)


# ==============================
# OPEN INSTAGRAM
# ==============================

driver.get("https://www.instagram.com/")
driver.maximize_window()

print("Instagram opened.")
print("Please log in manually in the browser.")

input("After logging in successfully, press ENTER here...")


# ==============================
# OPEN TARGET PROFILE
# ==============================

driver.get(f"https://www.instagram.com/{TARGET_PROFILE}/")
time.sleep(5)

print(f"Opened profile: @{TARGET_PROFILE}")


# ==============================
# OPEN FOLLOWERS LIST
# ==============================

try:
    followers_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, '/followers/')]")
        )
    )

    followers_button.click()

    print("Followers list opened.")

except Exception as e:
    print("Could not open followers list.")
    print("Instagram's UI or selector may have changed.")
    print(e)
    driver.quit()
    exit()


# ==============================
# WAIT FOR FOLLOWERS DIALOG
# ==============================

time.sleep(3)


# ==============================
# SCROLL FOLLOWERS LIST
# ==============================

try:

    dialog = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@role='dialog']")
        )
    )

    print("Followers dialog detected.")

    for _ in range(5):

        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight",
            dialog
        )

        time.sleep(2)

    print("Followers list scrolled.")

except Exception as e:

    print("Could not scroll followers list.")
    print(e)


# ==============================
# FOLLOW ACCOUNTS
# ==============================

followed_count = 0

try:

    while followed_count < FOLLOW_LIMIT:

        buttons = driver.find_elements(
            By.XPATH,
            "//div[@role='dialog']//button"
        )

        found_new_follow = False

        for button in buttons:

            if followed_count >= FOLLOW_LIMIT:
                break

            try:

                button_text = button.text.strip().lower()

                if button_text == "follow":

                    driver.execute_script(
                        "arguments[0].click();",
                        button
                    )

                    followed_count += 1
                    found_new_follow = True

                    print(
                        f"Followed account "
                        f"{followed_count}/{FOLLOW_LIMIT}"
                    )

                    time.sleep(2)

            except Exception:
                continue

        if not found_new_follow:

            driver.execute_script(
                "arguments[0].scrollTop += 500",
                dialog
            )

            time.sleep(2)

        if followed_count >= FOLLOW_LIMIT:
            break

except Exception as e:

    print("An error occurred while following accounts.")
    print(e)


# ==============================
# FINISHED
# ==============================

print("\n================================")
print("Instagram Follower Bot Finished!")
print(f"Total accounts followed: {followed_count}")
print("================================")

input("Press ENTER to close the browser...")

driver.quit()