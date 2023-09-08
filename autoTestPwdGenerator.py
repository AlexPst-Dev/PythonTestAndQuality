import unittest
import passwordGenerator
import tkinter as tk
import main  # Importez votre application principale
from main import Application


class TestApplication(unittest.TestCase):
    def tearDown(self):
        self.tk.base.destroy()

    def setUp(self):
        self.tk = Application()

    def test_title(self):
        expected = "Password Generator"
        self.assertEqual(
            self.tk.base.winfo_toplevel().title(),
            expected,
            "Title expected : {expected}",
        )

    # Check for elements instanciation
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

    # Check the default options are checked
    def test_checkboxes_with_digits(self):
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

    # Check the default radio bbutton for hash is on
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
