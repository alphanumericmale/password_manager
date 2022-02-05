import json
import random
from tkinter import *
from tkinter import messagebox
import pyperclip
from random import randint, choice


# ---------------------------- PASSWORD searcher ------------------------------- #
def search():
    search_term = w_entry.get()
    try:
        with open("password_list.json", mode="r") as file:

            dict_ = json.load(file)
            email = dict_[search_term]['email']
            password = dict_[search_term]['password']
            messagebox.showinfo(title=search_term, message=f"Email: {email}\nPassword: {password}")

    except KeyError as err:
        messagebox.showerror(title="oops", message=f"No such entry as {err}")
    except FileNotFoundError as err:
        messagebox.showerror(title="oops", message=f"No such entry as {search_term}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pword():
    p_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pw_numbers + pw_symbols + pw_letters
    random.shuffle(password_list)

    password_ = "".join(password_list)

    p_entry.insert(0, password_)
    pyperclip.copy(password_)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    website = w_entry.get()
    email = e_u_entry.get()
    password = p_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="oops", message="You haven't completed the form")

    else:
        try:
            with open(file="password_list.json", mode="r") as file:
                # read old data
                data = json.load(file)
                # updating data
                data.update(new_data)
            with open(file="password_list.json", mode="w") as file_:
                # saving new data
                json.dump(data, file_, indent=4)
        except json.decoder.JSONDecodeError:
            with open(file="password_list.json", mode="w") as file_:
                # saving new data
                json.dump(new_data, file_, indent=4)
        except FileNotFoundError:
            with open(file="password_list.json", mode="w") as file_:
                # saving new data
                json.dump(new_data, file_, indent=4)

                w_entry.delete(0, END)
                p_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# image
canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("Arial", 15, "bold"))
website_label.grid(column=0, row=1)
email_un_label = Label(text="Email/Username:", font=("Arial", 15, "bold"))
email_un_label.grid(column=0, row=2)
pword_label = Label(text="Password:", font=("Arial", 15, "bold"))
pword_label.grid(column=0, row=3)

# entry boxes
w_entry = Entry(width=33)
w_entry.focus()
w_entry.grid(column=1, row=1, columnspan=1)
e_u_entry = Entry(width=52)
e_u_entry.grid(column=1, row=2, columnspan=2)
e_u_entry.insert(0, "paercky@gmail.com")
p_entry = Entry(width=33)
p_entry.grid(column=1, row=3, columnspan=1)

# buttons
gen_pword_button = Button(text="Generate Password", command=gen_pword)
gen_pword_button.grid(column=2, row=3)
add_button = Button(width=44, text="Add", command=add_entry)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(width=15, text="Search", command=search)
search_button.grid(column=2, row=1)

window.mainloop()

# TODO 1: encryption with pword protection as key
# TODO 2: polymorphic password - like date - 1 or something
# TODO 3: out of band otp / two factor auth
# TODO 4: check for multiple entries
# TODO 5: catch exceptions

# try except else finally
