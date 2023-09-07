from tkinter import *
from tkinter import ttk
import tkinter
import passwordGenerator
from passwordGenerator import generate_password
import string


class Application:
    # Définition des entités de l'application
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

    include_lowercase = None
    include_uppercase = None
    include_digits = None
    include_symbols = None
    selected_hash = None

    def __init__(self) -> None:
        self.base = tkinter.Tk()
        # self.generate()

        self.load_base()
        self.load_title()
        self.load_caracter_input()
        self.load_hash()
        self.load_caracter_options()
        self.load_error_msg()
        self.load_entry_result()
        self.load_btn_generation()

    # Initialisation
    def load_base(self):
        self.base.geometry("500x550")

    # Title
    def load_title(self):
        self.base.title("Password Generator")
        self.labl_title = Label(
            self.base, text="Password Generator", width=20, font=("bold", 20)
        )
        self.labl_title.place(x=90, y=53)

    # Number of caracters input
    def load_caracter_input(self):
        self.labl_nb_caracters = Label(
            self.base, text="Number of caracters :", width=20, font=("bold", 10)
        )
        self.labl_nb_caracters.place(x=10, y=100)
        self.entry_nb_caraters = Entry(self.base)
        self.entry_nb_caraters.place(x=200, y=100, width=40)

    # Radios button for hash
    def load_hash(self):
        # Créez une variable StringVar pour stocker la valeur sélectionnée dans les boutons radio hash
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

    # Checkbox for caracter options
    def load_caracter_options(self):
        self.labl_checkbox = Label(self.base, text="Select options", font=("bold", 10))
        self.labl_checkbox.place(x=15, y=250)

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

    def load_error_msg(self):
        # Error message
        self.labl_error = Label(self.base, text="", font=("bold", 10), fg="red")
        self.labl_error.place(x=15, y=400)

    def load_entry_result(self):
        # Password generated result input
        self.entry_result = Entry(self.base)
        self.entry_result.place(x=10, y=420, width=480)
        # Password hashed
        self.entry_result_hashed = Entry(self.base)
        self.entry_result_hashed.place(x=10, y=450, width=480)

    # Button for a new generation
    def load_btn_generation(self):
        self.generate_button = Button(
            self.base,
            text="Generate",
            width=20,
            command=self.generate,
        ).place(x=180, y=500)

    def generate(self):
        password_length = self.entry_nb_caraters.get()
        lowercase = self.include_lowercase.get()
        uppercase = self.include_uppercase.get()
        digits = self.include_digits.get()
        symbols = self.include_symbols.get()
        selected_hash = self.var_hash.get()  # Accédez à la variable var_hash

        password = passwordGenerator.generate_password(
            int(password_length),
            lowercase,
            uppercase,
            digits,
            symbols,
        )
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

        self.labl_error.config(text="")  # Effacez le message d'erreur

        # input_value = entry_nb_caraters.get()
        # if (
        #     input_value.isdigit()
        #     and int(input_value) < 25
        #     and int(input_value) > 5
        #     and (
        #         include_digits.get()
        #         or include_lowercase.get()
        #         or include_symbols.get()
        #         or include_uppercase.get()
        #     )
        # ):
        #     # Si input_value est un nombre, convertissez-le en entier
        #     nb_caracters = int(input_value)
        #     selected_hash = var_hash.get()
        #     password = passwordGenerator.generate_password(
        #         nb_caracters,
        #         include_lowercase.get(),
        #         include_uppercase.get(),
        #         include_digits.get(),
        #         include_symbols.get(),
        #         selected_hash,
        #     )
        #     entry_result.delete(0, END)  # Effacez le texte précédent dans entry_result
        #     entry_result.insert(
        #         0, password
        #     )  # Insérez le mot de passe généré dans entry_result
        #     # Effacez le message d'erreur s'il existe
        #     labl_error.config(text="")
        # else:
        #     # Affichez le message d'erreur dans le label
        #     labl_error.config(
        #         text="Error: Please enter a valid number and at least one option"
        #     )

    # Lancer la boucle principale de l'application
    def run(self) -> None:
        self.base.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
