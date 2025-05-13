# Assignment_8
CS_361Assignment_8

Mitigation Plan
1.	Teammate: Martin Puchta
2.	Status: "credential_validators” microservice is completed and tested 
3.	Incomplete Parts: n/a
4.	Access Instructions:
o	Get code from GitHub: 
o	Run locally or in a virtual machine
o	I will summit a copy of the code via Discord in case you have issues accessing GitHub. 
5.	If Issues Arise:
o	Contact me ASAP via Discord
o	Available Sun–Tues 9AM- 2PM PST or 4PM to 7PM PST or WED-Friday 9AM to 11AM PST
o	Deadline to report issues: Saturday (5/17) EOD
6.	If for any reason the microservice cannot be run locally:
•	I can provide a sample response JSON file or a mocked API interface you can use in testing.
•	We can also walk through the request/response flow manually if needed for integration.

![image](https://github.com/user-attachments/assets/735f020f-5eb1-4e74-a39d-a163a0c20f31)


========================================
  FastAPI Signup Validator Microservice
========================================

This microservice validates email and password inputs based on formatting and complexity rules.
----------------------------------------
Endpoint Information
----------------------------------------

Method: POST
URL: http://127.0.0.1:8000/api/validate-signup
Content-Type: application/json

----------------------------------------
 Required Request Format
----------------------------------------

Send a JSON object with the following structure:

{
  "email": "example@domain.com",
  "password": "StrongPassword123!"
}

----------------------------------------
 Example Request in Python
----------------------------------------

import requests

url = "http://127.0.0.1:8000/api/validate-signup"

payload = {
    "email": "user@example.com",
    "password": "StrongP@ssw0rd"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.json())


----------------------------------------
Sample JSON Response
----------------------------------------

{
  "email_valid": true,
  "email_message": "Email is valid.",
  "password_valid": true,
  "password_message": "Password is valid.",
  "message": "Validation passed"
}

----------------------------------------
How to Programmatically RECEIVE Data
----------------------------------------

When a POST request is sent to the microservice, the response is returned as a JSON object.

Example in Python:

import requests

url = "http://127.0.0.1:8000/api/validate-signup"
payload = {
    "email": "user@example.com",
    "password": "Weakpass"
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print("Email Valid:", data["email_valid"])
    print("Email Message:", data["email_message"])
    print("Password Valid:", data["password_valid"])
    print("Password Message:", data["password_message"])
    print("Overall Message:", data["message"])
else:
    print("Request failed with status code:", response.status_code)
