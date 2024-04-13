from django.http import JsonResponse
from robot.run import run
import json
import os
from django.views.decorators.csrf import csrf_exempt
from uuid import uuid4

@csrf_exempt
def execute_tests(request):
 
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

    try:
        payload = json.loads(request.body)
        tests = payload.get('tests', [])

        results = []

        for test in tests:
            title = test.get('title', 'Untitled Test')
            steps = test.get('steps', [])

            if not title or not steps:
                results.append({'title': title, 'passed': False, 'error': 'Invalid test case data'})
                continue

            temp_file_name = f'temp_test_{uuid4()}.robot'
            
            with open(temp_file_name, 'w') as file:
                file.write(f"*** Settings ***\nLibrary    SeleniumLibrary\n\n*** Test Cases ***\n{title}\n")
                file.write('\n'.join(f"    {step}" for step in steps))

            run_status = run(temp_file_name, outputdir='output')
            passed = (run_status == 0)

            results.append({'title': title, 'passed': passed})

            os.remove(temp_file_name)

        return JsonResponse({'results': results})

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON payload'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



# BELOW CODE FROM SELENIUM  THIS IS ALSO WORKING WITH SAME OUTPUT


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from robot.api import ExecutionResult
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import json
# import logging
# import time

# @csrf_exempt
# def execute_tests(request):
#     if request.method != 'POST':
#         return JsonResponse({'error': 'Only POST requests are supported'}, status=405)

#     try:
#         # Configure logging
#         logger = logging.getLogger(__name__)
#         logger.setLevel(logging.DEBUG)
        
#         fh = logging.FileHandler('test_execution.log')
#         fh.setLevel(logging.DEBUG)
        
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         fh.setFormatter(formatter)
#         logger.addHandler(fh)

#         data = json.loads(request.body)
#         tests = data.get('tests', [])
        
#         if not isinstance(tests, list):
#             return JsonResponse({'error': 'Invalid payload: "tests" must be a list'}, status=400)
        
#         options = webdriver.ChromeOptions()
#         # Adjust options as needed (e.g., headless mode)
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#         results = []
#         for test in tests:
#             title = test.get('title', 'Untitled Test')
#             steps = test.get('steps', [])
            
#             for step in steps:
#                 if 'Open Browser browser=' in step:
#                     pass
#                 elif 'Go To url=' in step:
#                     # Extract the URL from the step
#                     url = step.split('=')[1].strip("'")
#                     try:
#                         driver.get(url)
#                         time.sleep(2)
#                     except Exception as e:
#                         # Log navigation errors
#                         logger.error(f"Failed to navigate to URL: {url}. Error: {str(e)}")
#                         results.append({
#                             'title': title,
#                             'error': f"Failed to navigate to URL: {url}. Error: {str(e)}"
#                         })
#                         continue  # Skip to next test case
                
#                 # Handle other test steps if necessary
#                 # You may add more code here to handle additional test steps

#             results.append({
#                 'title': title,
#             })

#         driver.quit()

#         return JsonResponse({'results': results})

#     except json.JSONDecodeError:
#         logger.error('Invalid JSON payload received.')
#         return JsonResponse({'error': 'Invalid JSON payload'}, status=400)

#     except Exception as e:
#         logger.exception(f'An unexpected error occurred: {str(e)}')
#         return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=500)
