import random
import string

def generate_password(length, use_special_chars=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_chars = string.punctuation

    if use_special_chars:
        all_chars = lowercase_letters + uppercase_letters + numbers + special_chars
    else:
        all_chars = lowercase_letters + uppercase_letters + numbers

    password = ''.join(random.choice(all_chars) for i in range(length))
    return password

length = int(input("Enter the length of the password: "))
use_special_chars = input("Do you want to include special characters? (y/n): ").lower() == 'y'

print("Generated password: ", generate_password(length, use_special_chars))