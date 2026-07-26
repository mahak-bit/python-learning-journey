from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


# =========================
# 1. START CHROME
# =========================

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)


# =========================
# 2. OPEN LINKEDIN JOBS
# =========================

driver.get("https://www.linkedin.com/jobs/")

time.sleep(3)


# =========================
# 3. SEARCH FOR A JOB
# =========================

try:
    job_search = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder*='Search job']")
        )
    )

    job_search.send_keys("Python Developer")

except Exception as e:
    print("Could not find job search box:", e)


# =========================
# 4. SEARCH LOCATION
# =========================

try:
    location_search = driver.find_element(
        By.CSS_SELECTOR,
        "input[placeholder*='Search location']"
    )

    location_search.clear()
    location_search.send_keys("Remote")

except Exception as e:
    print("Could not find location box:", e)


# =========================
# 5. CLICK SEARCH
# =========================

try:
    search_button = driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    search_button.click()

except Exception as e:
    print("Could not find search button:", e)


time.sleep(5)


# =========================
# 6. FIND JOB CARDS
# =========================

try:
    job_cards = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.base-card")
        )
    )

    print("Number of jobs found:", len(job_cards))

except Exception as e:
    print("Could not find job cards:", e)
    job_cards = []


# =========================
# 7. PRINT JOB DETAILS
# =========================

for index, job in enumerate(job_cards):

    try:
        title = job.find_element(
            By.CSS_SELECTOR,
            "h3.base-search-card__title"
        ).text

        company = job.find_element(
            By.CSS_SELECTOR,
            "h4.base-search-card__subtitle"
        ).text

        location = job.find_element(
            By.CSS_SELECTOR,
            "span.job-search-card__location"
        ).text

        print("--------------------------------")
        print("Job:", index + 1)
        print("Title:", title)
        print("Company:", company)
        print("Location:", location)

    except NoSuchElementException:
        print("Could not read job details.")


# =========================
# 8. CLICK FIRST JOB
# =========================

if job_cards:

    try:
        first_job = job_cards[0]

        driver.execute_script(
            "arguments[0].scrollIntoView();",
            first_job
        )

        time.sleep(1)

        first_job.click()

        time.sleep(3)

        print("First job opened successfully.")

    except Exception as e:
        print("Could not open first job:", e)


# =========================
# 9. KEEP BROWSER OPEN
# =========================

print("Automation finished.")
print("Browser will remain open.")

input("Press Enter to close the browser...")

driver.quit()