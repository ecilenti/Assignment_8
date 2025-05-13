from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

# Define the structure of the input data
class SignupData(BaseModel):
    email: str
    password: str

# POST endpoint to validate signup data
@app.post("/api/validate-signup")
def validate_signup(data: SignupData):
    email = data.email.strip().lower()
    password = data.password

    email_valid, email_message = validate_email(email)
    password_valid, password_message = validate_password(email, password)

    overall_message = "Validation passed" if email_valid and password_valid else "Validation failed"

    return {
        "email_valid": email_valid,
        "email_message": email_message,
        "password_valid": password_valid,
        "password_message": password_message,
        "message": overall_message
    }

# --- Helper function to validate email format ---
def validate_email(email: str) -> tuple[bool, str]:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, email):
        return False, "Email format is invalid. Must include '@' and a domain."
    return True, "Email is valid."

# --- Helper function to validate password strength ---
def validate_password(email: str, password: str) -> tuple[bool, str]:
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must include at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must include at least one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Password must include at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must include at least one special character."

    if '@' not in email:
        return False, "Email missing '@'. Cannot validate username against password."

    local_part = email.split('@')[0]
    if local_part.lower() in password.lower():
        return False, "Password should not contain your email username."

    common_passwords = ['password', '12345678']
    if password.lower() in common_passwords:
        return False, "Password is too common. Choose something more secure."

    return True, "Password is valid."

# --- Entry point to run with Uvicorn from PyCharm ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("credential_validators:app", host="127.0.0.1", port=8000, reload=True)
