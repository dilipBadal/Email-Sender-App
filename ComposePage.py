import tkinter as tk
from PIL import ImageTk, Image
import smtplib


class Compose(tk.Tk):
    def __init__(self, email, password):
        super().__init__()
        self.canvas = tk.Canvas(width=500, height=500, bg="#121212", highlightthickness=0)
        self.bg_image = Image.open("Logos/mail_logo.jpg")
        self.canvas.image = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(450, 200, image=self.canvas.image)
        self.canvas.place(x=0, y=0)

        self.title("Compose")
        self.config(width=500, height=500, pady=20, bg="#EF2121", padx=20)
        self.minsize(width=500, height=500)
        self.title("Mail Sender")
        self.user_email = email
        self.user_pass = password

        # Entries
        self.user_mail_entry = tk.Entry(width=30)
        self.receiver_mail_entry = tk.Entry(width=30)
        self.subject_entry = tk.Entry()
        self.msg_box = tk.Text()

        self.place_entries(self.user_email)

        def clear():
            self.subject_entry.delete(0, tk.END)
            self.msg_box.delete("1.0", tk.END)

        def send():
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as con:
                con.starttls()
                con.login(user=self.user_email, password=self.user_pass)
                con.sendmail(from_addr=self.user_email, to_addrs=self.receiver_mail_entry.get(),
                             msg=f"Subject:{self.subject_entry.get()}\n\n{self.msg_box.get('1.0','end-1c')}")

        # Buttons
        self.clear_button = tk.Button(text="Clear", command=clear)
        self.send_button = tk.Button(text="Send", command=send)
        self.place_buttons()
        self.mainloop()

    def place_entries(self, email):
        self.user_mail_entry.insert(0, email)
        self.user_mail_entry.grid(column=0, row=0, columnspan=2, pady=5, padx=0)
        self.receiver_mail_entry.grid(column=0, row=1, columnspan=2, pady=5, padx=0)
        self.receiver_mail_entry.focus_set()
        self.receiver_mail_entry.insert(0, "Receiver's Email")
        self.subject_entry.place(height=35, width=400, x=0, y=90)
        self.subject_entry.insert(0, "Subject")
        self.msg_box.place(height=300, width=400, x=0, y=150)

    def place_buttons(self):
        self.clear_button.place(y=3, x=340, width=60)
        self.send_button.place(y=35, x=340, width=60)




