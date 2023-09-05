from tkinter import *
from tkinter import ttk
import passwordGenerator
import string


def generate():
    input_value = entry_nb_caraters.get()
    if (
        input_value.isdigit()
        and int(input_value) < 25
        and (
            include_digits.get()
            or include_lowercase.get()
            or include_symbols.get()
            or include_uppercase.get()
        )
    ):
        # Si input_value est un nombre, convertissez-le en entier
        nb_caracters = int(input_value)
        selected_hash = var_hash.get()
        password = passwordGenerator.generate_password(
            nb_caracters,
            include_lowercase.get(),
            include_uppercase.get(),
            include_digits.get(),
            include_symbols.get(),
            selected_hash,
        )
        entry_result.delete(0, END)  # Effacez le texte précédent dans entry_result
        entry_result.insert(
            0, password
        )  # Insérez le mot de passe généré dans entry_result
        # Effacez le message d'erreur s'il existe
        labl_error.config(text="")
    else:
        # Affichez le message d'erreur dans le label
        labl_error.config(
            text="Error: Please enter a valid number and at least one option"
        )


# Initialisation
base = Tk()
base.geometry("500x550")

# Title
base.title("Registration Form")
labl_title = Label(base, text="Password Generator", width=20, font=("bold", 20))
labl_title.place(x=90, y=53)

# Number of caracters input
labl_nb_caracters = Label(
    base, text="Number of caracters :", width=20, font=("bold", 10)
)
labl_nb_caracters.place(x=10, y=100)
entry_nb_caraters = Entry(base)
entry_nb_caraters.place(x=200, y=100, width=40)

# Créez une variable StringVar pour stocker la valeur sélectionnée dans les boutons radio hash
var_hash = StringVar(value="none")
# List of available hash
labl_hash = Label(base, text="Select a hash protocole (optional)", font=("bold", 10))
labl_hash.place(x=15, y=140)
Radiobutton(base, text="md5", padx=5, value="MD5", variable=var_hash).place(x=10, y=165)
Radiobutton(base, text="sha256", padx=5, value="SHA-256", variable=var_hash).place(
    x=10, y=185
)
Radiobutton(base, text="None", padx=5, value="none", variable=var_hash).place(
    x=10, y=205
)


# Checkbox for character types
labl_checkbox = Label(base, text="Select options", font=("bold", 10))
labl_checkbox.place(x=15, y=250)

include_lowercase = BooleanVar(value=True)
include_uppercase = BooleanVar(value=True)
include_digits = BooleanVar()
include_symbols = BooleanVar()

checkbox_lower = Checkbutton(base, text="Lowercase", variable=include_lowercase)
checkbox_lower.place(x=10, y=275)

checkbox_upper = Checkbutton(base, text="Uppercase", variable=include_uppercase)
checkbox_upper.place(x=10, y=300)

checkbox_digits = Checkbutton(base, text="Digits", variable=include_digits)
checkbox_digits.place(x=10, y=325)

checkbox_symbols = Checkbutton(base, text="Symbols", variable=include_symbols)
checkbox_symbols.place(x=10, y=350)

# Error message
labl_error = Label(base, text="", font=("bold", 10), fg="red")
labl_error.place(x=15, y=400)

# Password generated result input
entry_result = Entry(base)
entry_result.place(x=10, y=450, width=480)

# Button for a new generation
Button(
    base,
    text="Generate",
    width=20,
    command=generate,
).place(x=180, y=500)
base.mainloop()
