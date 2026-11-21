"""
(GUI: Login Form) [PDF Q78] Build a login form that shows “Welcome <user>“ if the password is admin123, else “Wrong password”
"""

import tkinter as tk


class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x500")

        self.user = "admin123"

        self.label = tk.Label(root,text = "Enter login: ",font = ("Arial",10,"bold"))
        self.label.pack()
        self.box1 = tk.Entry(root, font=("Arial", 10))
        self.box1.pack()

        self.label1 = tk.Label(root,text = "Enter password: ",font = ("Arial",10,"bold"))
        self.label1.pack()
        self.box2 = tk.Entry(root,font=("Arial",10),show = "*")
        self.box2.pack()

        self.label2 = tk.Label(root,text="", font = ("Arial",10,"bold"))
        self.label2.pack()

        self.button = tk.Button(root,text="Login", font = ("Arial",15,"bold"),command = self.action_button)
        self.button.pack()
    def action_button(self):
        user = self.box1.get()
        pass1 = self.box2.get()

        if (pass1 == "admin123"):
            self.label2.config(text = f"Welcome {user}!")
        else:
            self.label2.config(text = "INVALID PASSWORD")



if __name__ == "__main__":
    window = tk.Tk()
    l = Login(window)
    window.mainloop()