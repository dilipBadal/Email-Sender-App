from tkinter import *
from ComposePage import Compose


# Functions
def login():
    email = mail_entry.get()
    password = pass_entry.get()
    window.destroy()
    compose = Compose(email, password)


# User Interface for Login Page
window = Tk()
window.config(width=500, height=500, bg="#EF2121", pady=20, padx=20)
window.title("Mail Sender")


mail_label = Label(text="E-Mail", fg="white", bg="#EF2121", font=("Ariel", 10, "normal"))
pass_label = Label(text="Password", fg="white", bg="#EF2121", font=("Ariel", 10, "normal"))
mail_label.grid(column=0, row=2)
pass_label.grid(column=0, row=3)


mail_entry = Entry(width=35)
mail_entry.focus_set()
pass_entry = Entry(width=35)
mail_entry.grid(column=1, row=2, pady=5)
pass_entry.grid(column=1, row=3, pady=5)

login_button = Button(text="Login", bg="#EA4335", width=30, command=login)
login_button.grid(column=1, row=4)

logo = PhotoImage(file="Logos/square_logo.png")
canvas = Canvas(width=250, height=250, bg="#EF2121", highlightthickness=0)
canvas.create_text(85, 15, text="Mail", fill="white", font=("Ariel", 20, "bold"))
canvas.create_text(160, 15, text="Sender", fill="white", font=("Ariel", 20, "bold"))
canvas.create_image(125, 125, image=logo)
canvas.grid(column=0, row=1, columnspan=2)






window.mainloop()
