# Q2. Write a Python program that generates a password with the following conditions:
# At least one uppercase letter.
# At least one lowercase letter.
# At least two numbers.
# At least one special character (e.g., !@#$%&*).
# The password should be exactly 16 characters long.
# The password should contain no repeating characters.
# The password should have a random order each time.





import random
import string

def generate_password():
    while True:
        pwd = []
        pwd.append(random.choice(string.ascii_uppercase))
        pwd.append(random.choice(string.ascii_lowercase))
        pwd.extend(random.choices(string.digits, k=2))
        pwd.append(random.choice('!@#$%&*'))
        
        new_length = 16 - len(pwd)
        all_characters = string.ascii_letters + string.digits + '!@#$%&*'
        pwd.extend(random.sample(all_characters, new_length))
        
        random.shuffle(pwd)
        
        if len(set(pwd)) == 16:
            return ''.join(pwd)

print(generate_password())