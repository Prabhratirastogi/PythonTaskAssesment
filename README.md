# Python Task Assessment

## Overview
This repository contains a series of Python tasks, including web scraping, data processing, Django model implementations, rate limiting, and algorithmic challenges. Each task is organized in its own folder with corresponding test files that validate the functionality.

## Table of Contents
- [Tasks](#tasks)
- [Setup Instructions](#setup-instructions)
- [Testing](#testing)
- [Requirements](#requirements)
- [GitHub Repository](#github-repository)
- [License](#license)

## Tasks

### Task 1: Web Scraping
**Description:** A script that scrapes the titles and URLs of the latest articles from CNN using BeautifulSoup and requests.  
**Files:** `scrape_cnn.py`, `test_scrape_cnn.py`  
**Functionality:**
- Fetches and prints the latest article titles and URLs.

### Task 2: Data Cleaning
**Description:** Reads a CSV file with user data, removes duplicates, and filters out invalid email formats.  
**Files:** `clean_user_data.py`, `test_clean_user_data.py`  
**Functionality:**
- Cleans user data and saves it to `new_data.csv`.


### Task 3: Django Model Method

**Description:** Implements a method in a Django model to get the top 5 customers based on spending in the last 6 months.

**Files:** `models.py`, `views.py`, `urls.py`

#### Setup for Django Project

1. **Install Django:**
   ```bash
   pip install django

2. **Navigate to the project directory:**
   ```bash
   cd myproject

3. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

4. **Run the server:**
   ```bash
    python manage.py runserver

5. **Access the view: Navigate to http://127.0.0.1:8000/orders/top-customers/ to see the top 5 customers.:**

6. **To run the tests for the Django application:**
   ```bash
    python manage.py test orders


### Task 4: Rate Limiter
**Description:** A rate limiter that restricts the number of requests a user can make in a given time window.  
**Files:** `rate_limiter.py`, `test_rate_limiter.py`  
**Functionality:**
- Allows or denies requests based on user ID.

### Task 5: Data Aggregation
**Description:** Aggregates values from a list of dictionaries based on a specified key.  
**Files:** `aggregate_data.py`, `test_aggregate_data.py`  
**Functionality:**
- Groups data and applies an aggregation function.

### Task 6: Find Duplicate in Array
**Description:** Finds a duplicate number in an array using Floyd’s Tortoise and Hare algorithm.  
**Files:** `find_duplicate.py`, `test_find_duplicate.py`  
**Functionality:**
- Returns the duplicate number.

## Setup Instructions

### Clone the Repository:
```bash
git clone https://github.com/yourusername/repository.git
cd repository


Create a Virtual Environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate


Install Dependencies:
```bash
pip install -r requirements.txt


Testing
To run the tests for each task, navigate to the respective folder and execute:
```bash
python -m unittest test_filename.py
To run the tests for Task Django Model Order:
```bash
python manage.py test app_name(order)



Requirements
Create a requirements.txt file using:
```bash
pip freeze > requirements.txt


GitHub Repository
You can find the repository at:[GitHub Link]



