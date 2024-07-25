# Test Automation Framework

## Overview

This project is a sample test automation framework designed to validate the functionalities of both web and API endpoints. It uses Behavior-Driven Development (BDD) to write tests in a human-readable format, ensuring that both technical and non-technical stakeholders can understand the testing processes.
Due to technical limitation - API and UI products used for this project are not related

- **UI product**: https://magento.softwaretestingboard.com/
- **API product**: https://restful-booker.herokuapp.com/

## Features

- **UI Testing**: Automates end-to-end testing of web applications using Selenium WebDriver.
- **API Testing**: Validates API endpoints using HTTP methods like GET, POST, PUT, and DELETE.
- **Pydantic Models**: Ensures data validation and type enforcement for API responses.
- **Authentication**: Includes functionality to generate and manage API tokens for authenticated endpoints.
- **Reports**: Generates detailed test execution reports for analysis and review.

## Technologies Used

- **Python**: The core programming language.
- **Selenium WebDriver**: For automating web browser interactions.
- **Behave**: A BDD framework for writing tests in Gherkin language.
- **Pydantic**: For data validation and settings management.
- **Requests**: For making HTTP requests to the API.

## Prerequisites

- **Python 3.x**: Ensure you have Python installed on your machine.
- **WebDriver**: For Selenium, ensure the correct WebDriver (e.g., ChromeDriver) is installed.
- **Virtual Environment**: Recommended for managing dependencies.



This document provides instructions for setting up and running tests for the project both locally using PyCharm and Docker.

## Running from PyCharm Locally

1. **Import Project**: Open your project in PyCharm.
2. **Create a Python Virtual Environment**:
   - Run the command: `virtualenv venv`
   - This creates a `venv` folder in the project directory.
3. **Activate the Environment**:
   - Run: `source venv/bin/activate`
4. **Install Dependencies**:
   - Run: `pip install -r requirements.txt`

## Running the Application

Tests are tagged for selective execution. Available tags are:
- `@UI`
- `@API`

To run all tests:
```bash
behave -f html -o /reports/behave-report.html


To run tests marked by specific tag use:
behave --tags=@YOUR_TAG -f html -o /reports/behave-report.html


Running from Docker locally:

1. Using terminal go into projects root directory
2. Using dockerfile - run following command depending on which machine you're running on:

For linux x64/86 please use following command:
docker build -t behave-tests .

While on Mac linux/amd64 use following command:
docker build --platform linux/amd64 -t behave-tests .

Once the image is built, you can run tests using following command:

For linux x64/86 please use following command:
docker run --rm behave-tests

While on Mac linux/amd64 use following command:
docker run --rm --platform linux/amd64 behave-tests




