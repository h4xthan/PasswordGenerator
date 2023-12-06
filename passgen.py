import string
import random

def generate_password(length, use_letters=True, use_numbers=True, use_special_chars=True):
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

# Prompt the user for the number of passwords to generate
num_passwords = int(input('Enter the number of passwords to be generated => '))

# Prompt the user for the desired password length
length = int(input('Enter how many characters long your password will be (recommended to be longer than 8 characters) => '))

# Prompt the user for password complexity options
use_letters = input('Do you want to include letters? (y/n) ').lower() == 'y'
use_numbers = input('Do you want to include numbers? (y/n) ').lower() == 'y'
use_special_chars = input('Do you want to include special characters? (y/n) ').lower() == 'y'

# Generate the specified number of passwords
passwords = []
for i in range(num_passwords):
    password = generate_password(length, use_letters, use_numbers, use_special_chars)
    passwords.append(password)

# Open a file to write the generated passwords
with open('passwords.txt', 'a') as file:
    for password in passwords:
        file.write(password + '\n')

# Print the generated passwords and inform the user that they have been saved to a file
print('Your generated passwords are => ', passwords)
print('Passwords have been saved to passwords.txt')
