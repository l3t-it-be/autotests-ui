# 🚀 UI Course Automation Tests

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-green)](https://docs.pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Web%20Testing-red?logo=playwright)](https://playwright.dev/)
[![Allure](https://img.shields.io/badge/Allure-Reporting-yellow)](https://docs.qameta.io/allure/)

Automated tests for
the [UI Course Test Application](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login),
built with **Python**, **Pytest**, **Allure**, and **Playwright**.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Getting Started](#-getting-started)
    - [Clone the Repository](#-clone-the-repository)
    - [Create a Virtual Environment](#-create-a-virtual-environment)
    - [Install Dependencies](#-install-dependencies)
    - [Additional Playwright Setup](#-additional-playwright-setup)
- [Running the Tests](#-running-the-tests)
    - [With Allure Report Generation](#-with-allure-report-generation)
    - [Viewing the Allure Report](#-view-the-allure-report)

---

## 🌐 Project Overview

The goal of this project is to automate the testing of the UI Course application.
The automated tests verify various functionalities of the application to ensure
its stability and correctness. The project structure follows best practices
for organizing test code with clear, maintainable scripts.

**Tech Stack**:

- **Language**: Python 3.11+
- **Frameworks**: Pytest, Playwright
- **Reporting**: Allure
- **Test Coverage**: [UI Coverage Tool](https://github.com/Nikita-Filonov/ui-coverage-tool)
- **CI/CD**: GitHub Actions

---

## 🛠️ Getting Started

### 📥 Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 🐍 Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. 
Follow the instructions for your operating system:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 📦 Install Dependencies

Once the virtual environment is activated, install the project dependencies
listed in requirements.txt:

```bash
pip install -r requirements.txt
```

### ⚙️ Additional Playwright Setup

If you're running Playwright for the first time,
you might need to install the required browsers (Chromium, Firefox, WebKit):

```bash
playwright install
```

---

## 🖥️ Running the Tests

### ▶️ With Allure Report Generation

To run the tests and generate an Allure report, use the following command:

```bash
pytest -m 'regression' --alluredir=./allure-results
```

This will execute all tests in the project marked "regression" and display the results in the terminal.

### 📊 View the Allure Report

To run the tests and generate an Allure report, use the following command:

```bash
pytest -m 'regression' --alluredir=./allure-results
```

