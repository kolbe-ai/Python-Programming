"""
Login Form Simulation:
Two entry boxes: Username and Password.
A button: "Login."
On click, display "Welcome <username>." if not empty, else show "Please enter details."
"""

import tkinter as tk
class Login:
  def __init__(self,root):
    self.root = root
    self.root.title("Login")
    self.root.geometry("500x500")

    #self.user = "admin"
    #self.pass1 = "1234"

    #adding user label
    self.label = tk.Label(root,text = "Enter user name: ",font = ("Arial",10))
    self.label.pack()
    self.box = tk.Entry(root,font = ("Arial",10))
    self.box.pack()

    #adding password label
    self.label1 = tk.Label(root,text = "Enter password: ",font = ("Arial",10))
    self.label1.pack()
    self.box1 = tk.Entry(root,font=("Arial",10),show = "*")
    self.box1.pack()

    #adding button
    self.button = tk.Button(root,text = "Login",font = ("Arial",15), command = self.action_button)
    self.button.pack()

     #adding result label
    self.label3 = tk.Label(root,text = "" , font = ("Arial",10,"bold"))
    self.label3.pack()


  def action_button(self):
    self.user_name = self.box.get()
    self.password = self.box1.get()
    if (self.user_name != "" and self.password != ""):
      self.label3.config(text = "Welcome "+self.user_name)
    else:
      self.label3.config(text = "Please enter details")



if __name__ == "__main__":
  window = tk.Tk()
  Login(window)
  window.mainloop()