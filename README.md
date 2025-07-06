# Email_Validator
This project is a simple Python-based email validator that checks whether an email address follows basic rules such as starting with an alphabet, containing only one '@', having the proper dot (.) position, and avoiding spaces, uppercase letters, and invalid characters.

## 🔍 Features
- Checks for:
  - Minimum length
  - Starts with alphabet
  - Only one `@` symbol
  - Proper dot (`.`) position
  - No spaces or special characters
  - No capital letters

## ✅ Sample Valid Email
example123@gmail.com


## ❌ Sample Invalid Emails
1example@gmail.com → Starts with digit
example@@gmail.com → More than one '@'
example@.com → Invalid domain


## ▶️ How to Run
bash
python email_validator.py
