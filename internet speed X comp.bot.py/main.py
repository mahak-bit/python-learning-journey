import speedtest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ==========================================
# 1. INTERNET SPEED TEST
# ==========================================

print("Starting internet speed test...")

st = speedtest.Speedtest()

st.get_best_server()

download_speed = st.download() / 1_000_000
upload_speed = st.upload() / 1_000_000

download_speed = round(download_speed, 2)
upload_speed = round(upload_speed, 2)

print("--------------------------------")
print("Internet Speed Test Results")
print("--------------------------------")
print(f"Download Speed: {download_speed} Mbps")
print(f"Upload Speed: {upload_speed} Mbps")
print("--------------------------------")


# ==========================================
# 2. START CHROME
# ==========================================

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 15)


# ==========================================
# 3. OPEN X / TWITTER
# ==========================================

driver.get("https://x.com/")

time.sleep(5)


# ==========================================
# 4. MANUAL LOGIN
# ==========================================

print("Please log in to X manually.")

input("After you have logged in, press Enter here...")


# ==========================================
# 5. OPEN COMPOSE BOX
# ==========================================

try:

    post_box = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div[role='textbox']")
        )
    )

    post_box.click()


    # ======================================
    # 6. CREATE COMPLAINT MESSAGE
    # ======================================

    message = (
        f"Hey Internet Provider, "
        f"I am paying for a high-speed internet connection, "
        f"but my current internet speed is only "
        f"{download_speed} Mbps download and "
        f"{upload_speed} Mbps upload. "
        f"Could you please look into this issue?"
    )


    # ======================================
    # 7. TYPE THE POST
    # ======================================

    post_box.send_keys(message)

    time.sleep(2)


    # ======================================
    # 8. POST THE COMPLAINT
    # ======================================

    post_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@data-testid='tweetButtonInline']"
            )
        )
    )

    post_button.click()

    print("Complaint posted successfully! 🚀")


except Exception as e:

    print("Something went wrong.")
    print("Error:", e)


# ==========================================
# 9. KEEP BROWSER OPEN
# ==========================================

input("Press Enter to close the browser...")

driver.quit()