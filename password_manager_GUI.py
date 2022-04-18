import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# -------PASSWORD GENERATOR --------#


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 6)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    # print(password_list, len(password_list))

    password_list_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_list.extend(password_list_symbols)

    password_list_num = [random.choice(numbers) for num in range(nr_numbers)]
    password_list.extend(password_list_num)

    random.shuffle(password_list)

    # .join() method changes list into a string
    password_for_website = ''.join(password_list)
    # print(f"Your password is: {password_for_website}")
    web_password.insert(0, password_for_website)
    pyperclip.copy(password_for_website)


# -------FUNCTIONALITY-------- #

def save():
    website_name = web_entry.get()
    user_name = web_username.get()
    password = web_password.get()

    to_be_written_json = {
        website_name: {
            "email": user_name,
            "password": password
        }
    }
    if len(website_name) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Do not leave any field empty!")
    else:
        user_choice = messagebox.askokcancel(title=website_name, message=f"Details are email{user_name} \n password"
                                                                         f" {password}. Do you want to save it?")
        # print(website_name, user_name, password)
        if user_choice:
            # print(to_be_written_json)
            try:
                #  reads the data.json file
                with open('data.json', mode='r') as valuables:
                    # Reading  old data
                    data = json.load(valuables)
                    # print(type(data)) gives <class 'dict'>
            except FileNotFoundError:
                # if there is no data.json, then  it  creates the file data.json
                with open('data.json', mode='w') as valuables:
                    json.dump(to_be_written_json, valuables, indent=4)
            else:
                # update the dictionary to be written into  the data.json file
                with open('data.json', mode='w') as valuables:
                    data.update(to_be_written_json)
                    json.dump(data, valuables, indent=4)
            finally:
                web_entry.delete(0, 'end')
                web_password.delete(0, 'end')


def find_password():
    webpage_exists = None
    website_name = web_entry.get()
    try:
        with open('data.json', mode='r') as valuables:
            # Reading  old data
            data = json.load(valuables)
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Oops", message="No data file found")
    else:
        for web_name in data:
            if website_name == web_name:
                webpage_exists = True

        if webpage_exists:
            messagebox.showinfo(title="Your  info", message=f"email:{data[website_name]['email']} "
                                                        f"password:{data[website_name]['password']}")
        else:
            messagebox.showinfo("oops", f"No details for the website {website_name}")


# -----------------------UI SETUP---------------------------------#


window = tkinter.Tk()
window.title("Password  Manager GUI")
window.config(padx=50, pady=50)
canvas = tkinter.Canvas(window, height=200, width=200)
logo_ = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_)
canvas.grid(row=0, column=1)
web_label = tkinter.Label(text="Website:")
web_label.grid(row=1, column=0)
web_entry = tkinter.Entry(width=15)
# Sets the focus on the Website entry
web_entry.focus_set()
web_entry.grid(row=1, column=1)
search_button = tkinter.Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)
username_label = tkinter.Label(text="Email/Username:")
username_label.grid(row=2, column=0)
web_username = tkinter.Entry(width=35)
web_username.insert(0, 'pandey@pandey.com')
web_username.grid(row=2, column=1, columnspan=2)
password_label = tkinter.Label(text="Password")
password_label.grid(row=3, column=0)
web_password = tkinter.Entry(width=15)
web_password.grid(row=3, column=1)
generate_button = tkinter.Button(text="Generate Password", command=password_generator)
generate_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
