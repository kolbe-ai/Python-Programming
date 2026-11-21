"""
78. (Login Form Simulation)
Create two entry boxes (Username, Password) and a “Login” button. On click, show “Welcome <username>.”
if the details are filled in, otherwise “Please enter details.”
"""

import tkinter as tk

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry("500x500")

        #user
        self.user = tk.Label(root,text="Enter your username: ",font=("Arial",10,"bold"))
        self.user.pack()
        self.userbox = tk.Entry(font=("Arial",10))
        self.userbox.pack()

        #password
        self.password = tk.Label(root,text="Enter your password: ",font = ("Arial",10,"bold"))
        self.password.pack()
        self.passbox = tk.Entry(root,font=("Arial",10),show="*")
        self.passbox.pack()

        #button
        self.button = tk.Button(root,text="LOGIN",command= self.login)
        self.button.pack()

        #result
        self.result = tk.Label(root,text="",font=("Arial",10,"bold"))
        self.result.pack()

    def login(self):
        self.user_name= self.userbox.get()
        self.password= self.passbox.get()
        if self.user_name == "":
            self.result.config(text="Please enter details")
        else:
            self.result.config(text=f"Welcome {self.user_name}")



if __name__ == "__main__":
    window = tk.Tk()
    l = Login(window)
    window.mainloop()