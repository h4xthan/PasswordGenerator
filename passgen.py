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

num_passwords = int(input('Ingresa el numero de contraseñas a generar => '))
length = int(input('Ingresa de cuantos caracteres sera tu contraseña => '))

use_letters = input('Quieres incluir letras? (y/n) ').lower() == 'y'
use_numbers = input('Quieres incluir numeros? (y/n) ').lower() == 'y'
use_special_chars = input('Quieres incluir caracteres especiales? (y/n) ').lower() == 'y'

passwords = []
for i in range(num_passwords):
    password = generate_password(length, use_letters, use_numbers, use_special_chars)
    passwords.append(password)
    
print('Tus contraseñas generadas son => ', passwords)