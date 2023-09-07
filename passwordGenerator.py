import string
import random
import hashlib

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

hasherSHA256 = hashlib.sha256()  # SHA-256
hasherMD5 = hashlib.md5()  # MD5


def generate_password(
    length,
    use_lowercase=True,
    use_uppercase=True,
    use_digits=True,
    use_symbols=True,
):
    if (
        length < 25
        and length > 5
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

def SHA_256(password):
    password = password.encode("utf-8")
    hasherSHA256.update(password)
    hashed_password = hasherSHA256.hexdigest()
    return hashed_password

def MD5(password):
    password = password.encode("utf-8")
    hasherMD5.update(password)
    hashed_password = hasherMD5.hexdigest()
    return hashed_password

def evaluate_password(password):
    score = 0

    length = len(password)

    if length <= 8:
        return score  # Mot de passe très faible
    elif 8 < length <= 10:
        score += 5  # Mot de passe faible
    elif 10 < length <= 12:
        score += 10  # Mot de passe moyen
    elif 12 < length <= 16:
        score += 20  # Mot de passe fort
    elif length > 16:
        score += 40  # Mot de passe très fort

    types_of_characters = 0
    if any(char.islower() for char in password):
        types_of_characters += 1
    if any(char.isupper() for char in password):
        types_of_characters += 1
    if any(char.isdigit() for char in password):
        types_of_characters += 1
    if any(not char.isalnum() for char in password):
        types_of_characters += 1

    if (types_of_characters == 1):
        return 'Mot de passe très faible'
    elif (types_of_characters == 2):
        score *=2
    elif (types_of_characters == 3):
        score *=4
    elif (types_of_characters == 4):
        score *=8

    if score < 20:
        return 'Mot de passe très faible'
    elif 20 <= score < 60:
        return 'Mot de passe faible'
    elif 60 <= score < 100:
        return 'Mot de passe moyen'
    elif 100 <= score < 160:
        return 'Mot de passe fort'
    elif 160 <= score < 260:
        return 'Mot de passe très fort'
    else:
        return 'Mot de passe abusé wesh'


if __name__ == "__main__":
    print(generate_password(16, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True))
