Description:



Running from pycharm:
1. Import your project into pycharm
2. In cmd you will need to create a python3 virtual environment using following command:
virtualenv venv
where venv is the title of your environment. If performed correctly a - a new "venv" folder will be created in "Shell_Assignment repo"

3. After environment is created, you need to activate it with following command:
source venv2/bin/activate

4. After activation, make sure to install all dependencies required with following command:
pip install -r requirements.txt

Running the application:

All tests are marked with tags to enable selective test execution. Available tags are:
@UI
@API

To run all tests use:
behave -f html -o /reports/behave-report.html

To run tests marked by specific tag use:
behave --tags=@YOUR_TAG -f html -o /reports/behave-report.html




