import unittest
from main import Application


#
# Class TestApplication : Automatic tests for the interface
#
class TestApplication(unittest.TestCase):
    #
    # Destroy the application after all the test
    #
    def tearDown(self):
        self.tk.base.destroy()

    #
    # Launch the app
    #
    def setUp(self):
        self.tk = Application()

    #
    # Test if the title of the app is the string expected
    #
    def test_title(self):
        expected = "Password Generator"
        self.assertEqual(
            self.tk.base.winfo_toplevel().title(),
            expected,
            "Title expected : {expected}",
        )

    #
    # Test for the instanciation of the elements, check if there are not set to None type
    #
    def test_instanciate_element(self):
        self.assertIsNotNone(self.tk.base)
        self.assertIsNotNone(self.tk.labl_title)
        self.assertIsNotNone(self.tk.labl_nb_caracters)
        self.assertIsNotNone(self.tk.entry_nb_caraters)
        self.assertIsNotNone(self.tk.labl_hash)
        self.assertIsNotNone(self.tk.labl_checkbox)
        self.assertIsNotNone(self.tk.checkbox_lower)
        self.assertIsNotNone(self.tk.checkbox_upper)
        self.assertIsNotNone(self.tk.checkbox_digits)
        self.assertIsNotNone(self.tk.checkbox_symbols)
        self.assertIsNotNone(self.tk.labl_error)

    #
    # Check if the default options are checked
    #
    def test_checkboxes(self):
        self.assertTrue(
            self.tk.include_lowercase.get(),
            "The lowercase checkbox has to be checked by default",
        )
        self.assertTrue(
            self.tk.include_uppercase.get(),
            "The uppercase checkbox has to be checked by default",
        )
        self.assertFalse(
            self.tk.include_digits.get(),
            "The digits checkbox has to not be checked by default",
        )
        self.assertFalse(
            self.tk.include_symbols.get(),
            "The symbols checkbox has to not be checked by default",
        )

    #
    # Check if the default radio button for hash is on
    #
    def test_radio_button_hash(self):
        self.assertEqual(
            self.tk.var_hash.get(),
            "MD5",
            "The md5 radio button have to be selected by default",
        )
        self.assertNotEqual(
            self.tk.var_hash.get(),
            "SHA-256",
            "The sha-256 radio button have to not be selected by default",
        )
