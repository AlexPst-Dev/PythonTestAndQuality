from tkinter import *
import tkinter
import passwordGenerator


#
# Class Application : App's Interface
#
class Application:
    #
    # Defining entities on the interface
    #
    labl_title = None
    labl_nb_caracters = None
    entry_nb_caraters = Entry
    labl_hash = None
    labl_checkbox = None
    checkbox_lower = None
    checkbox_upper = None
    checkbox_digits = None
    checkbox_symbols = None
    labl_error = None
    generate_button = None
    labl_evaluation = None

    include_lowercase = None
    include_uppercase = None
    include_digits = None
    include_symbols = None
    selected_hash = None

    #
    # Init function to initialise all the elements
    #
    def __init__(self) -> None:
        self.base = tkinter.Tk()
        self.load_base()

        self.load_title()
        self.load_caracter_input()
        self.load_hash()
        self.load_caracter_options()
        self.load_error_msg()
        self.load_entry_result()
        self.load_btn_generation()
        self.load_evaluation()

    #
    # Defining the size of the app
    #
    def load_base(self):
        self.base.geometry("500x550")

    #
    # Set title
    #
    def load_title(self):
        self.base.title("Password Generator")
        self.labl_title = Label(
            self.base, text="Password Generator", width=20, font=("bold", 20)
        )
        self.labl_title.place(x=90, y=53)

    #
    # Set number of caracter input
    #
    def load_caracter_input(self):
        self.labl_nb_caracters = Label(
            self.base, text="Number of caracters :", width=20, font=("bold", 10)
        )
        self.labl_nb_caracters.place(x=10, y=100)
        self.entry_nb_caraters = Entry(self.base)
        self.entry_nb_caraters.place(x=200, y=100, width=40)

    #
    # Set radio buttons for hash
    #
    def load_hash(self):
        # var_hash is used to save a default value for the selected hash
        self.var_hash = StringVar(value="MD5")
        # List of available hash
        self.labl_hash = Label(
            self.base, text="Select a hash protocole (optional)", font=("bold", 10)
        )
        self.labl_hash.place(x=15, y=140)
        Radiobutton(
            self.base,
            text="md5",
            padx=5,
            value="MD5",
            variable=self.var_hash,
        ).place(x=10, y=165)
        Radiobutton(
            self.base,
            text="sha256",
            padx=5,
            value="SHA-256",
            variable=self.var_hash,
        ).place(x=10, y=185)

    #
    # Set checkbox for caracter options
    #
    def load_caracter_options(self):
        self.labl_checkbox = Label(self.base, text="Select options", font=("bold", 10))
        self.labl_checkbox.place(x=15, y=250)

        # Check the two first by default
        self.include_lowercase = BooleanVar(value=True)
        self.include_uppercase = BooleanVar(value=True)
        self.include_digits = BooleanVar()
        self.include_symbols = BooleanVar()

        self.checkbox_lower = Checkbutton(
            self.base, text="Lowercase", variable=self.include_lowercase
        )
        self.checkbox_lower.place(x=10, y=275)

        self.checkbox_upper = Checkbutton(
            self.base, text="Uppercase", variable=self.include_uppercase
        )
        self.checkbox_upper.place(x=10, y=300)

        self.checkbox_digits = Checkbutton(
            self.base, text="Digits", variable=self.include_digits
        )
        self.checkbox_digits.place(x=10, y=325)

        self.checkbox_symbols = Checkbutton(
            self.base, text="Symbols", variable=self.include_symbols
        )
        self.checkbox_symbols.place(x=10, y=350)

    #
    # Set error message
    #
    def load_error_msg(self):
        self.labl_error = Label(self.base, text="", font=("bold", 10), fg="red")
        self.labl_error.place(x=15, y=400)

    #
    # Set password generated result input
    #
    def load_entry_result(self):
        # Password
        self.entry_result = Entry(self.base)
        self.entry_result.place(x=10, y=420, width=480)
        # Password hashed
        self.entry_result_hashed = Entry(self.base)
        self.entry_result_hashed.place(x=10, y=450, width=480)

    #
    # Set generation button for a new password
    #
    def load_btn_generation(self):
        self.generate_button = Button(
            self.base,
            text="Generate",
            width=20,
            command=self.generate,
        ).place(x=180, y=500)

    #
    # Set string for password evaluation
    #
    def load_evaluation(self):
        self.labl_evaluation = Label(self.base, text="", font=("bold", 10))
        self.labl_evaluation.place(x=300, y=350)

    #
    # Generate function for password creation
    #
    def generate(self):
        # Get the values and options that the user set
        password_length = self.entry_nb_caraters.get()
        lowercase = self.include_lowercase.get()
        uppercase = self.include_uppercase.get()
        digits = self.include_digits.get()
        symbols = self.include_symbols.get()
        selected_hash = self.var_hash.get()  # Accédez à la variable var_hash
        self.labl_evaluation.config(text="")

        # Check if password_length is a valid insput
        if password_length.isdigit() and password_length != "":
            # Call generate_password from passwordGenerator.py
            password = passwordGenerator.generate_password(
                int(password_length),
                lowercase,
                uppercase,
                digits,
                symbols,
            )
            # If generate_password return an error value
            if password == "error":
                self.labl_error.config(
                    text="Error: Please enter a valid number and at least one option"
                )
                self.entry_result.delete(0, END)
                self.entry_result_hashed.delete(0, END)
            # If user's selected values and options are compliant, hash the password
            else:
                hashed_password = "none"
                if selected_hash == "MD5":
                    hashed_password = passwordGenerator.MD5(password)
                elif selected_hash == "SHA-256":
                    hashed_password = passwordGenerator.SHA_256(password)

                self.entry_result.delete(0, END)
                self.entry_result.insert(0, password)

                if hashed_password:
                    self.entry_result_hashed.delete(0, END)
                    self.entry_result_hashed.insert(0, hashed_password)

                # Delete error message
                self.labl_error.config(text="")
                # Evaluate the user's password
                self.labl_evaluation.config(
                    text=passwordGenerator.evaluate_password(password)
                )
        else:
            self.labl_error.config(
                text="Error: Please enter a valid number and at least one option"
            )
            self.entry_result.delete(0, END)
            self.entry_result_hashed.delete(0, END)

    #
    # Lunch the main loop of the application
    #
    def run(self) -> None:
        self.base.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
