

## Setup Instructions
1. Clone the repository from GitHub Repo URL : `https://github.com/sandeeptale/Django-robot-selenium_navigate.git'

2. Navigate to the project directory: `new-test\test_ai\test_executor`  - cd test_ai
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:

 On Windows: `venv\Scripts\activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Apply migrations:`python manage.py migrate`
7. Run the Django development server: `python manage.py runserver`
8. The Django server should now be running locally.
##  other Instructions


pip install chromedriver-autoinstaller
pip install selenium
pip install robotframework-seleniumlibrary
pip install robotframework-pythonlibcore
pip install robotframework



- you have to also setup chromedriver which the chrome version and set the path also in python  file where python install
https://sites.google.com/chromium.org/driver/
for fire box you can install geckodriver and  set the path also
####
I HAVE WRITTEN BOTH CODE YOU CAN RUN BY ROBOT OR OTHER  METHOD (SELENIUM) JUST UNCOMMNET THE  LINE OF CODE OTHER # Testing with Selenium WebDriver ALSO YOU WIll GET SAME ANS # To execute tests :
## Execution Instructions
1. Use a tool like Postman to send a POST request to the API endpoint.
2. Configure the request with the following details:

- Endpoint: `http://127.0.0.1:8000/tests/v1/execute`
- Method: POST
- Headers: Content-Type: application/json
- Body:
```
{
    "tests": [
        {
            "title": "Open google.com",
            "steps": [
                "Open Browser https://google.com chrome"
            ]
        }
    ]
}
```

3. Send the request and observe the response for the test output.


## API Call Examples
### Request
```
POST /testai/tests/v1/execute HTTP/1.1
Host: http://127.0.0.1:8000
Content-Type: application/json

{
    "tests": [
        {
            "title": "Open google.com",
            "steps": [
                "Open Browser https://google.com chrome"
            ]
        }
    ]
}
```
YOU CAN OPEN FIREBOX ALSO BY SELENUIM



## OUT PUT ON postman - 
```
{
    "results": [
        {
            "title": "Open google.com",
            "passed": true
        }
    ]
}





- SANDEEP TALE


