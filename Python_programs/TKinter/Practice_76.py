"""
76. (Simple Counter) Create a “Count” button that increases a number shown in a label each time it is clicked.
"""

import tkinter as tk

class Count:
    def __init__(self,root):
        self.count = 0

        self.root = root
        self.root.title("Counter")
        self.root.geometry("500x500")
        self.root.config(bg="cyan")

        self.label = tk.Label(root,text = "Counter: 0",font = ("Arial",20,"bold"),bg="brown",fg="grey")
        self.label.pack()

        self.button= tk.Button(root,text= "Click Here!",font=("Arial",20,"bold"),command= self.counter)
        self.button.pack()

    def counter(self):
        self.count += 1
        self.label.config(text = f"Counter: {self.count}")


if __name__ == "__main__":
    window = tk.Tk()
    c = Count(window)
    window.mainloop()