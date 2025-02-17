import re

# Q1. Write a Python program to perform the following: 
# Validate a given public IP address to check if it follows the correct format (IPv4).
# Validate a given email address to check if it’s a valid Gmail address, considering:
# It should contain "@gmail.com".
# The username before "@gmail.com" should contain only lowercase letters , numbers and permitted symbols.
# Provide informative error messages for invalid IP or email.

def validate_ip(ip):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if pattern.match(ip):
        parts = ip.split('.')
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return "Invalid IP address: Each part must be between 0 and 255."
        return "Valid IP address."
    else:
        return "Invalid IP address format."

def validate_email(email):
    pattern = re.compile(r'^[a-z0-9._%+-]+@gmail\.com$')
    if pattern.match(email):
        return "Valid Gmail address."
    else:
        return "Invalid Gmail address: Must contain '@gmail.com' and only lowercase letters, numbers, and permitted symbols before '@gmail.com'."

ip = input("Enter IP address: ")
email = input("Enter email address: ")

print(validate_ip(ip))
print(validate_email(email))
