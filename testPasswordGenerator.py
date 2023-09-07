import unittest
import passwordGenerator

class TestPasswordGenerator(unittest.TestCase):
    
    def test_generate_password_length(self):
        # Vérifiez que la longueur du mot de passe généré est correcte
        for length in range(5, 25):
            password = passwordGenerator.generate_password(length)
            self.assertEqual(len(password), length)

    def test_generate_password_length_under_five(self):
        # Vérifiez qu'une erreur est levée si la longueur du mot de passe est inférieure à 5
        password = passwordGenerator.generate_password(4)
        self.assertEqual(password, "error")

    def test_generate_password_length_over_twenty_five(self):
        # Vérifiez qu'une erreur est levée si la longueur du mot de passe est supérieure à 25
        password = passwordGenerator.generate_password(26)
        self.assertEqual(password, "error")

    def test_generate_password_length_negative(self):
        # Vérifiez qu'une erreur est levée si la longueur du mot de passe est négative
        password = passwordGenerator.generate_password(-1)
        self.assertEqual(password, "error")

    def test_generate_password_length_null(self):
        # Vérifiez qu'une erreur est levée si la longueur du mot de passe est nulle
        password = passwordGenerator.generate_password(0)
        self.assertEqual(password, "error")

    def test_generate_password_lowercase(self):
        # Vérifiez que le mot de passe contient des lettres minuscules
        password = passwordGenerator.generate_password(25)
        self.assertTrue(any(c.islower() for c in password))

    def test_generate_password_uppercase(self):
        # Vérifiez que le mot de passe contient des lettres majuscules
        password = passwordGenerator.generate_password(25)
        self.assertTrue(any(c.isupper() for c in password))

    def test_generate_password_digits(self):
        # Vérifiez que le mot de passe contient des chiffres
        password = passwordGenerator.generate_password(25)
        self.assertTrue(any(c.isdigit() for c in password))

    def test_generate_password_symbols(self):
        # Vérifiez que le mot de passe contient des symboles
        password = passwordGenerator.generate_password(25)
        self.assertTrue(any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in password))

    def test_generate_password_no_character_selected(self):
        # Vérifiez qu'une erreur est levée si aucun caractère n'est sélectionné
        password = passwordGenerator.generate_password(25, use_lowercase=False, use_uppercase=False, use_digits=False, use_symbols=False)
        self.assertEqual(password, "error")

    def test_generate_password_hash_sha256(self):
        # Vérifiez que le mot de passe généré est correctement haché
        password = passwordGenerator.generate_password(25)
        hashed_password = passwordGenerator.SHA_256(password)
        self.assertEqual(len(hashed_password), 64)
    
    def test_generate_password_hash_md5(self):
        # Vérifiez que le mot de passe généré est correctement haché
        password = passwordGenerator.generate_password(25)
        hashed_password = passwordGenerator.MD5(password)
        self.assertEqual(len(hashed_password), 32)

if __name__ == '__main__':
    unittest.main()