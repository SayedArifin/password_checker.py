from array_all import specialCharacters
from array_all import lowercaseAlphabets
from array_all import uppercaseAlphabets
from array_all import numbers

specialCharacters_value = False
lowercaseAlphabets_value = False
uppercaseAlphabets_value = False
numbers_value = False
length = False

print("Welcome to the Simple Password Strength Viewer with Python")
password = input("Please enter your password to check:\n➜ ")

if len(password) >= 8:
    length = True
else:
    print('⦿ Your password should have 8 or more characters.')

for letter in password:
    if letter in specialCharacters:
        specialCharacters_value = True
    if letter in lowercaseAlphabets:
        lowercaseAlphabets_value = True
    if letter in uppercaseAlphabets:
        uppercaseAlphabets_value = True
    if letter in numbers:
        numbers_value = True

if not specialCharacters_value:
    print('⦿ Your password must have a special character.')
if not lowercaseAlphabets_value:
    print('⦿ Your password must have a lowercase character.')
if not uppercaseAlphabets_value:
    print('⦿ Your password must have an uppercase character.')
if not numbers_value:
    print('⦿ Your password must have a number.')

if uppercaseAlphabets_value and lowercaseAlphabets_value and specialCharacters_value and numbers_value and length:
    print(f'⦿ "{password}" is a strong password.')
