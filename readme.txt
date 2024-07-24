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




