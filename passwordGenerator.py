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
    use_hash="none",
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
        if use_hash == "SHA-256":
            password = password.encode("utf-8")
            hasherSHA256.update(password)
            hashed_password = hasherSHA256.hexdigest()
            return hashed_password
        elif use_hash == "MD5":
            password = password.encode("utf-8")
            hasherMD5.update(password)
            hashed_password = hasherMD5.hexdigest()
            return hashed_password
        else:
            return password
    else:
        return "error"


if __name__ == "__main__":
    print(generate_password(12, True, True, True, True, "SHA-256"))
