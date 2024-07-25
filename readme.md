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
- **Test formatting**: Tests are written in human readable and non technical language.
- **CI/CD**: On every commit - a CI/CD pipeline is executed to ensure stability of codebase

## Technologies Used

- **Python**: The core programming language.
- **Selenium WebDriver**: For automating web browser interactions.
- **Behave**: A BDD framework for writing tests in Gherkin language.
- **Pydantic**: For data validation and settings management.
- **Requests**: For making HTTP requests to the API.
- **CircleCI**: For running all tests in CI/CD
- **Docker**: For local deployment

## Prerequisites

- **Python 3.x**: Ensure you have Python installed on your machine.
- **ChromeDriver**: For Selenium, ensure the correct ChromeDriver is installed.
- **Chrome Browser**: For UI test chrome driver usage
- **Virtual Environment**: Recommended for managing dependencies.
- **Docker**: to run tests from a container instead of locally
- **Virtualenv**: to run tests on virtual environment


This Section provides instructions for setting up and running tests for the project both locally using:
- **command line**
- **docker **

## Running from PyCharm Locally

Note: Make sure all prerequisites are met before proceeding with setup

1. **Import Project**: Open your project in PyCharm.
2. **Create a Python Virtual Environment**:
   - Run the command: `virtualenv venv`
   - This creates a `venv` folder in the project directory.
3. **Activate the Environment**:
   - Run: `source venv/bin/activate`
4. **Install Dependencies**:
   - Run: `pip install -r requirements.txt`
5. **Optional**: in case Brew did was not installed properly you can try:
   - Run: "pip install behave"

## Running the Application:

Tests are tagged for selective execution. Available tags are:
- `@UI`
- `@API`

To run all tests:
```behave -f html -o behave-report.html```


To run tests marked by specific tag use:
'behave --tags=@YOUR_TAG -f html -o behave-report.html'

## Reporting:
Navigating to behave-report.html will provide you with .html report with test redults

## Running from Docker locally:

1. **Using terminal go into projects root directory**
2. **Using dockerfile - run following command depending on which machine you're running on**:

- For linux x64/86 please use following command:
```docker build -t behave-tests .```

- While on Mac linux/amd64 use following command:
```docker build --platform linux/amd64 -t behave-tests .```

3. **Once the image is built, you can run tests using following command:**

- For linux x64/86 please use following command:
```docker run --rm behave-tests```

- While on Mac linux/amd64 use following command:
```docker run --rm --platform linux/amd64 behave-tests```