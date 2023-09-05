import string
import random

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = ""
    if use_lowercase:
        characters += lowercase_letters
    if use_uppercase:
        characters += uppercase_letters
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols

    if not characters:
        raise ValueError("No characters to choose from!")
    
    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print(generate_password(12))
