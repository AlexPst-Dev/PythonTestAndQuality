import string
import random
import hashlib

#
# Set characters panel
#
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

#
# Set hashers panel
#
hasherSHA256 = hashlib.sha256()  # SHA-256
hasherMD5 = hashlib.md5()  # MD5


#
# function to generate password with the given length and the given characters options
#
def generate_password(
    length,
    use_lowercase=True,
    use_uppercase=True,
    use_digits=True,
    use_symbols=True,
):
    if (
        length < 26
        and length > 4
        and (use_lowercase or use_uppercase or use_symbols or use_digits)
    ):
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
    else:
        return "error"


#
# function to hash the given password with the SHA_256 algorithm
#
def SHA_256(password):
    password = password.encode("utf-8")
    hasherSHA256.update(password)
    hashed_password = hasherSHA256.hexdigest()
    return hashed_password


#
# function to hash the given password with the MD5 algorithm
#
def MD5(password):
    password = password.encode("utf-8")
    hasherMD5.update(password)
    hashed_password = hasherMD5.hexdigest()
    return hashed_password


#
# function to evaluate the given password
#
def evaluate_password(password):
    score = 0

    length = len(password)

    if length <= 8:
        score += 3
    elif 8 < length <= 10:
        score += 5
    elif 10 < length <= 12:
        score += 10
    elif 12 < length <= 16:
        score += 20
    elif length > 16:
        score += 40

    types_of_characters = 0
    # Check if the password contains lowercase letters
    if any(char.islower() for char in password):
        types_of_characters += 1
    # Check if the password contains uppercase letters
    if any(char.isupper() for char in password):
        types_of_characters += 1
    # Check if the password contains digits
    if any(char.isdigit() for char in password):
        types_of_characters += 1
    # Check if the password contains symbols
    if any(not char.isalnum() for char in password):
        types_of_characters += 1

    # If the password contains only one type of character, the score is very weak
    if types_of_characters == 1:
        return "Très faible"
    elif types_of_characters == 2:
        score *= 2
    elif types_of_characters == 3:
        score *= 4
    elif types_of_characters == 4:
        score *= 8

    if score < 20:
        return "Très faible"
    elif 20 <= score < 60:
        return "Faible"
    elif 60 <= score < 100:
        return "Moyen"
    elif 100 <= score < 200:
        return "Fort"
    else:
        return "Très fort"


if __name__ == "__main__":
    print(
        generate_password(
            16,
            use_lowercase=True,
            use_uppercase=True,
            use_digits=True,
            use_symbols=True,
        )
    )
