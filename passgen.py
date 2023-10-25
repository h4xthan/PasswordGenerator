import string
import random

def generate_password(length, use_letters = True, use_numbers = True, use_special_chars = True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
        
    while True:
        password = ''.join(random.choice(characters) for i in range(length))
        if (use_letters and any(c.islower() for c in password) and any(c.isupper() for c in password)) or \
            (use_numbers and any(c.isdigit() for c in password)) or \
                (use_special_chars and any(c in string.punctuation for c in password)):
                    return password

num_passwords = int(input('Enter the number of passwords to be generated => '))
length = int(input('Enter how many characters long your password will be (recommended to be longer than 8 characters) => '))

use_letters = input('Do you want to include letters? (y/n) ').lower() == 'y'
use_numbers = input('Do you want to include numbers? (y/n) ').lower() == 'y'
use_special_chars = input('Do you want to include special characters? (y/n) ').lower() == 'y'

passwords = []
for i in range(num_passwords):
    password = generate_password(length, use_letters, use_numbers, use_special_chars)
    passwords.append(password)
    
print('Your generated passwords are => ', passwords)
