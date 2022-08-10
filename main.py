from tkinter import *
from tkinter import messagebox
import random

THEME_COLOR = "#202A44"

window = Tk()
window.title("Graphical Register System.")
window.config(pady=20, padx=20)
window["bg"] = THEME_COLOR

canvas = Canvas(width=220, height=225, bg=THEME_COLOR, highlightthickness=0)
image = PhotoImage(file="joinnow.png")
canvas.create_image(119, 117, image=image)
canvas.grid(row=0, column=2)


def gen_password():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "A", "B", "C", "X", "Y", "Z", "W", "R", "L"]
    characters = ["!", "@", "#", "$", "%", "^", "&", "*", "+", "<"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    output = []
    for i in range(3):
        output.append(random.choice(alphabet))
        output.append(random.choice(characters))
        output.append(random.choice(numbers))
    random.shuffle(output)
    result = ""
    for char in output:
        result += char
    password.insert(0, result)
    confirm_password.insert(0, result)


def save():
    name_entry = name.get()
    email_entry = email.get()
    password_entry = password.get()
    con_password = confirm_password.get()
    with open("data.txt", "a") as file:
        file.write(f"{name_entry}|{email_entry}|{password_entry}\n")
        name.delete(0, END)
        email.delete(0, END)
        password.delete(0, END)
        confirm_password.delete(0, END)
        messagebox.showinfo(title="Success", message="Registration Complete.")


# ---------------------------------------GUI--------------------------------------------------------#


header1 = Label(text="Join Cohort 5.0 now!", bg=THEME_COLOR, font=("Arial", 18, "bold"), fg="white", padx=20, pady=20)
header1.grid(row=0, column=0)

name_def = Label(text="Name:", bg=THEME_COLOR, font=("Times New Roman", 18, "normal"), fg="white")
name_def.grid(row=2, column=0)

name = Entry(width=30)
name.focus()
name.grid(row=2, column=1)

email_def = Label(text="Email:", bg=THEME_COLOR, font=("Times New Roman", 18, "normal"), fg="white")
email_def.grid(row=3, column=0)

email = Entry(width=30)
email.grid(row=3, column=1)

password_def = Label(text="Password:", bg=THEME_COLOR, font=("Times New Roman", 18, "normal"), fg="white")
password_def.grid(row=4, column=0)

password = Entry(width=30)
password.grid(row=4, column=1)

confirm_password_def = Label(text="Confirm Password:", bg=THEME_COLOR, font=("Times New Roman", 18, "normal"),
                             fg="white")
confirm_password_def.grid(row=5, column=0)

confirm_password = Entry(width=30)
confirm_password.grid(row=5, column=1)

bottom_text = Label(text="By creating an account,\n you agree to our terms and condition.",
                    bg=THEME_COLOR, font=("Arial", 10, "italic", "underline"), fg="white", padx=20, pady=20,
                    cursor="hand2")
bottom_text.grid(row=6, column=2, columnspan=2)

sign_up = Button(width=10, text="Sign Up", bg="#2E2252", fg="white", command=save)
sign_up.grid(row=7, column=2, columnspan=2)

generate_password = Label(text="Let's help you generate a password.",
                          bg=THEME_COLOR, font=("Arial", 10, "italic", "underline"), fg="white", padx=20, pady=20)
generate_password.grid(row=6, column=0)

password_button = Button(width=25, text="Generate Password for me", bg="#2E2252", fg="white", command=gen_password)
password_button.grid(row=7, column=0)

window.mainloop()
