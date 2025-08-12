import random 
import string 

def pass_gen(length, use_numbers=True, use_letters=True, use_Symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_Symbols:
        characters += string.punctuation
    if not characters:
        return "Error no character type selected"   

    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

print("-----WELCOME TO PASSWORD GENERATOR-----")
print("Select Your Requirements")

length = int(input("Enter the length of the password: "))
use_letters = input("Do you want to include LETTERS? (y/n): ").lower() == 'y'
use_numbers = input("Do you want to include NUMBERS? (y/n): ").lower() == 'y'
use_symbols = input("Do you want to include Symbols? (y/n): ").lower() == 'y'

result = pass_gen(length, use_letters, use_numbers, use_symbols)
print("\nGenerated password: \n",result)