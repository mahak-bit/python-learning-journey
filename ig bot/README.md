# 📸 Day 52 — Instagram Follower Bot

A Python automation project built using **Selenium WebDriver** that demonstrates browser automation by opening Instagram, navigating to a target profile's followers list, scrolling through followers, and attempting to follow available accounts.

This project is part of my **100 Days of Code: The Complete Python Pro Bootcamp** journey by Angela Yu.

---

## 🚀 Project Overview

The Instagram Follower Bot automates repetitive browser interactions using **Selenium**.

The program:

* Opens Instagram in Google Chrome
* Allows the user to log in manually
* Navigates to a specified Instagram profile
* Opens the profile's followers list
* Scrolls through the followers list
* Attempts to click available **Follow** buttons
* Limits the number of follow actions using a configurable value

The project focuses on learning **web automation, browser control, element selection, explicit waits, and interaction with dynamic web pages**.

---

## 🛠️ Technologies Used

* **Python**
* **Selenium WebDriver**
* **Google Chrome**
* **ChromeDriver**

---

## 📂 Project Structure

```text
Day 52
├── main.py
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project folder

```bash
cd Day-52
```

### 3. Install Selenium

```bash
pip install selenium
```

### 4. Run the program

```bash
python main.py
```

---

## 🔧 Configuration

You can change the target Instagram profile in `main.py`:

```python
TARGET_PROFILE = "instagram"
```

For example:

```python
TARGET_PROFILE = "example_user"
```

You can also control the maximum number of follow actions:

```python
FOLLOW_LIMIT = 20
```

For testing, it is recommended to start with a small number:

```python
FOLLOW_LIMIT = 3
```

---

## 🔐 Login

For security reasons, the project does **not** store Instagram login credentials directly in the source code.

Instead, the browser opens Instagram and the user can log in manually.

This avoids exposing sensitive credentials in the GitHub repository.

---

## 🧠 What I Learned

Through this project, I practiced:

* Automating browsers with Selenium
* Launching and controlling Chrome using Python
* Using `WebDriverWait` and explicit waits
* Finding elements with XPath
* Clicking dynamic web elements
* Working with dialogs and scrollable containers
* Using JavaScript to interact with web elements
* Handling exceptions in automation scripts
* Building configurable automation programs
* Understanding the challenges of automating dynamic websites

---

## ⚠️ Important Note

Instagram's website structure and selectors can change frequently. As a result, Selenium selectors used in this project may require updates if Instagram changes its interface.

Automated actions on social media platforms may also trigger anti-bot systems or be restricted by platform rules. This project is intended for **educational purposes and learning browser automation**.

Use automation responsibly and avoid excessive or abusive activity.

---

## 🎯 Future Improvements

Possible improvements include:

* Adding more robust element selectors
* Improving scrolling logic
* Adding better error handling
* Detecting already-followed accounts
* Adding configurable delays
* Using environment variables for configuration
* Creating a reusable Selenium automation framework
---
