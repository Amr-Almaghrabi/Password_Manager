from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(letters) for _ in range(randint(2, 4))]
    password_numbers = [choice(letters) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        warning = messagebox.askretrycancel(title="Warning!", message="Please do not leave any empty fields")
        return 0

    is_ok = messagebox.askokcancel(title=website, message=f"This is the information entered: \n"
                                                          f"Website: {website}\n Email: {email}\n Password: {password}\n"
                                                          f"Is it okay to save?")

    if is_ok:
        with open("data.txt", mode="a") as f:
            f.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.focus()
website_entry.config(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

Email_label = Label(text="Email/Username: ")
Email_label.grid(column=0, row=2)
email_entry = Entry()
email_entry.insert(0, "example@gmail.com")
email_entry.config(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

Password_label = Label(text="Password: ")
Password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.config(width=10)
generate_password_button.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", command=save)
add_button.config(width=33)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
