"""
77. (Text Transformation)
Create an entry box and an “Uppercase” button. When clicked, show the uppercase version of the entered text in a label.
"""

import tkinter as tk


class Upper:
    def __init__(self,root):
        self.root = root
        self.root.title("UpperCase")
        self.root.geometry("500x500")
        self.root.config(bg="black")

        self.label = tk.Label(root,text="Enter the string: ",font=("Arial",15,"bold"),fg="cyan",bg="black")
        self.label.pack()
        self.box = tk.Entry(font=("Arial",10,"bold"))
        self.box.pack()
        self.button = tk.Button(text = "UPPER",font=("Arial",10,"bold"),bg="red",command=self.action_button)
        self.button.pack()

        self.answer = tk.Label(text="",font=("Arial",10,"bold"),fg="yellow",bg="red")
        self.answer.pack()

    def action_button(self):
        self.string= self.box.get()
        self.result = (self.string).upper()         #converting
        self.answer.config(text=f"Result is : {self.result}")


if __name__ == "__main__":
    window = tk.Tk()
    u = Upper(window)
    window.mainloop()