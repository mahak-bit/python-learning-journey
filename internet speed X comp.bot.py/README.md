# Day 51 — Internet Speed Twitter Complaint Bot 📡🐦

A Python automation project built with **Selenium WebDriver** and **Speedtest** as part of Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

## 📌 Project Overview

This project combines internet speed testing with browser automation.

The program measures the current internet download and upload speeds using Speedtest and then uses Selenium WebDriver to open X (formerly Twitter). After the user completes authentication manually, the automation creates a complaint message containing the measured internet speeds and posts it to the platform.

The project demonstrates how Python can be used to combine external libraries, real-world data, and browser automation into a practical workflow.

## 🚀 Features

- Measures real-time internet download speed
- Measures real-time internet upload speed
- Automatically selects the best available Speedtest server
- Launches Google Chrome using Selenium WebDriver
- Supports manual authentication for secure login
- Dynamically generates a complaint message using speed test results
- Automates interaction with the X post composer
- Uses explicit waits for more reliable browser automation
- Handles potential Selenium errors using exception handling

## 🛠️ Technologies & Tools

- **Python 3**
- **Selenium WebDriver**
- **Speedtest**
- **Google Chrome**
- **Chrome WebDriver**

## 📚 Key Concepts Learned

- Working with external Python libraries
- Measuring internet speed programmatically
- Selenium WebDriver
- Browser automation
- Explicit waits with `WebDriverWait`
- Expected Conditions
- CSS Selectors
- XPath
- Finding and interacting with web elements
- `.click()`
- `.send_keys()`
- Exception handling with `try/except`
- Dynamic message generation
- Combining multiple Python libraries in one project

## 📂 Project Structure

```text
Day 51/
└── main.py










⚙️ Installation

Install the required Python libraries:

python -m pip install selenium
python -m pip install speedtest-cli

Make sure Google Chrome is installed on your computer.

▶️ How to Run

Run the Python script:

python main.py

The program will:

Run an internet speed test.
Display the download speed.
Display the upload speed.
Open X in Google Chrome.
Allow the user to log in manually.
Generate a complaint message using the measured speeds.
Enter the message into the post composer.
Attempt to publish the post.
🔐 Authentication

For security reasons, login credentials are not stored in the source code.

The user completes authentication manually before the automation continues.

⚠️ Disclaimer

This project was created for educational purposes to demonstrate Python, Selenium WebDriver, and browser automation concepts.

Automated interactions with third-party platforms may be subject to their Terms of Service and usage policies. Always use automation responsibly and respect platform rules, rate limits, and user privacy.

Website interfaces and element selectors may change over time, so Selenium selectors may require updates if the target platform changes its HTML structure.

🎯 Learning Outcome

Through this project, I strengthened my understanding of Python libraries, internet speed testing, Selenium WebDriver, browser automation, explicit waits, dynamic content generation, exception handling, and integrating multiple tools into a single automated workflow.
