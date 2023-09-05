from tkinter import *
from tkinter import ttk

# Initialisation
base = Tk()
base.geometry("500x350")

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

# List of available hash
labl_hash = Label(base, text="Select a hash protocole (optional)", font=("bold", 10))
labl_hash.place(x=15, y=140)
Radiobutton(base, text="md5", padx=5, value="md5").place(x=10, y=165)
Radiobutton(base, text="sha256", padx=5, value="sha256").place(x=10, y=185)

# Password generated result input
entry_result = Entry(base)
entry_result.place(x=10, y=220, width=250)

# Button for a new generation
Button(base, text="Generate", width=20).place(x=180, y=275)
base.mainloop()
