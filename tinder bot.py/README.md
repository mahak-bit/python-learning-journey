# Day 50 — Tinder Automation Bot 🤖

A browser automation project built with **Python and Selenium WebDriver** as part of Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

## 📌 Project Overview

This project demonstrates how Selenium WebDriver can be used to automate browser interactions with a dynamic web application.

The automation bot launches Google Chrome, navigates to Tinder, allows the user to complete authentication manually, handles common pop-ups, and interacts with profile cards by automating the Like action.

The project focuses on practical browser automation concepts and demonstrates how repetitive web interactions can be automated using Python.

## 🚀 Features

- Launches and controls Google Chrome using Selenium WebDriver
- Opens the Tinder web application automatically
- Supports manual user authentication
- Handles common location and notification pop-ups
- Locates interactive elements using XPath
- Uses explicit waits to improve reliability
- Automates Like button interactions
- Limits automated interactions using a controlled loop
- Keeps the browser open after execution for debugging and inspection

## 🛠️ Technologies & Tools

- **Python 3**
- **Selenium WebDriver**
- **Google Chrome**
- **Chrome WebDriver**

## 📚 Key Concepts Learned

- Selenium WebDriver
- Browser automation
- `webdriver.Chrome()`
- `WebDriverWait`
- Explicit waits
- Expected Conditions
- XPath selectors
- `find_element()`
- `.click()`
- Exception handling with `try/except`
- `for` loops for repetitive automation
- Manual authentication within automated workflows

## 📂 Project Structure

```text
Day 50/
└── main.py
