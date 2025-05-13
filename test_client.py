import requests

# Define the API endpoint
url = "http://127.0.0.1:8000/api/validate-signup"

# List of test cases: (email, password, description)
test_cases = [
    ("User@Example.com", "StrongP@ssw0rd", "Valid email & password"),
    ("InvalidEmail", "StrongP@ssw0rd", "Invalid email format"),
    ("user@example.com", "weak", "Password too short & no complexity"),
    ("user@example.com", "password", "Common password (too weak)"),
    ("user@example.com", "User@1234", "Password contains email username"),
    ("user@example.com", "NoSpecialChar1", "Missing special character"),
    ("user@example.com", "nospecialchar1!", "Missing uppercase letter"),
    ("user@example.com", "NOSPECIALCHAR1!", "Missing lowercase letter"),
    ("user@example.com", "StrongP@ssw0rd", "Another valid password"),
]

# Loop through test cases
for email, password, description in test_cases:
    payload = {
        "email": email,
        "password": password
    }

    print("====== Test Case ======")
    print(f"Description    : {description}")
    print(f"Input Email    : {email}")
    print(f"Input Password : {password}")

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            print("Response       :", data)
        else:
            print(f"Error          : Received status code {response.status_code}")
    except requests.exceptions.ConnectionError:
        print(" ERROR: Cannot connect to the server at", url)

    print()
