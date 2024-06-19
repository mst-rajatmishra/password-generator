import random
import string
from tkinter import *

def generate_password():
    try:
        password_length = int(e1.get())  # Get the desired length of the password from user input
        if password_length <= 5:
            password_label.config(text="Password length must be at least 5")
            return
    except ValueError:
        password_label.config(text="Please enter a valid number")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    password_label.config(text=password)

root = Tk()
root.title("Password Generator")
root.geometry("500x500")

Label(root, text="Enter length of password").pack(pady=10)

e1 = Entry(root)
e1.pack(pady=5)

b1 = Button(root, text="Generate Password", command=generate_password)
b1.pack(pady=20)

Label(root, text="New password is:").pack(pady=10)

password_label = Label(root, text="")
password_label.pack(pady=5)

root.mainloop()
