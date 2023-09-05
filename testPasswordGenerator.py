import unittest
import passwordGenerator

class TestPasswordGenerator(unittest.TestCase):
    
    def test_generate_password_length(self):
        # Vérifiez que la longueur du mot de passe généré est correcte
        length = 12
        password = passwordGenerator.generate_password(length)
        self.assertEqual(len(password), length)

    def test_generate_password_lowercase(self):
        # Vérifiez que le mot de passe contient des lettres minuscules
        password = passwordGenerator.generate_password(8, use_lowercase=True, use_uppercase=False)
        self.assertTrue(any(c.islower() for c in password))

    def test_generate_password_uppercase(self):
        # Vérifiez que le mot de passe contient des lettres majuscules
        password = passwordGenerator.generate_password(8, use_lowercase=False, use_uppercase=True)
        self.assertTrue(any(c.isupper() for c in password))

    def test_generate_password_digits(self):
        # Vérifiez que le mot de passe contient des chiffres
        password = passwordGenerator.generate_password(8, use_digits=True, use_symbols=False)
        self.assertTrue(any(c.isdigit() for c in password))

    def test_generate_password_symbols(self):
        # Vérifiez que le mot de passe contient des symboles
        password = passwordGenerator.generate_password(8, use_symbols=True, use_lowercase=False)
        self.assertTrue(any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in password))

    def test_generate_password_no_character_selected(self):
        # Vérifiez qu'une erreur est levée si aucun caractère n'est sélectionné
        with self.assertRaises(ValueError):
            passwordGenerator.generate_password(8, use_lowercase=False, use_uppercase=False, use_digits=False, use_symbols=False)


if __name__ == '__main__':
    unittest.main()