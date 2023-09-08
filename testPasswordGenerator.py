import unittest
import passwordGenerator

class TestPasswordGenerator(unittest.TestCase):

    # 
    # Check that the password length is correct
    #
    def test_generate_password_length(self):
        for length in range(5, 25):
            password = passwordGenerator.generate_password(length)
            self.assertEqual(len(password), length)

    # 
    # Check that an error is raised if the password length is less than 5
    #
    def test_generate_password_length_under_five(self):
        password = passwordGenerator.generate_password(4)
        self.assertEqual(password, "error")

    # 
    # Check that an error is raised if the password length is greater than 25
    #
    def test_generate_password_length_over_twenty_five(self):
        password = passwordGenerator.generate_password(26)
        self.assertEqual(password, "error")

    # 
    # Check that an error is raised if the password length is negative
    #
    def test_generate_password_length_negative(self):
        password = passwordGenerator.generate_password(-1)
        self.assertEqual(password, "error")

    # 
    # Check that an error is raised if the password length is null
    #
    def test_generate_password_length_null(self):
        password = passwordGenerator.generate_password(0)
        self.assertEqual(password, "error")

    # 
    # Check that the password contains lowercase letters
    #
    def test_generate_password_lowercase(self):
        password = passwordGenerator.generate_password(25)
        self.assertTrue(any(c.islower() for c in password))

    #
    # Check that the password contains uppercase letters
    #
    def test_generate_password_uppercase(self):
        password = passwordGenerator.generate_password(25)
        self.assertTrue(any(c.isupper() for c in password))

    #
    # Check that the password contains digits
    #
    def test_generate_password_digits(self):
        password = passwordGenerator.generate_password(25)
        self.assertTrue(any(c.isdigit() for c in password))

    #
    # Check that the password contains symbols
    #
    def test_generate_password_symbols(self):
        password = passwordGenerator.generate_password(25)
        self.assertTrue(any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in password))

    #
    # Check that an error is raised if no character is selected
    #
    def test_generate_password_no_character_selected(self):
        password = passwordGenerator.generate_password(25, use_lowercase=False, use_uppercase=False, use_digits=False, use_symbols=False)
        self.assertEqual(password, "error")

    #
    # Check that the password is correctly hashed with SHA-256 algorithm
    #
    def test_generate_password_hash_sha256(self):
        password = passwordGenerator.generate_password(25)
        hashed_password = passwordGenerator.SHA_256(password)
        self.assertEqual(len(hashed_password), 64)
    
    #
    # Check that the password is correctly hashed with MD5 algorithm
    #
    def test_generate_password_hash_md5(self):
        password = passwordGenerator.generate_password(25)
        hashed_password = passwordGenerator.MD5(password)
        self.assertEqual(len(hashed_password), 32)

if __name__ == '__main__':
    unittest.main()