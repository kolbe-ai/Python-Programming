"""
76. (Simple Counter) Create a “Count” button that increases a number shown in a label each time it is clicked.
"""

import tkinter as tk

class Count:
    def __init__(self,root):
        self.root = root
        self.root.title("Counter")
        self.root.geometry("500x500")
        self.counter = 0

        self.label = tk.Label(root,text="Counter",font=("Arial",10,"bold"))
        self.label.pack()
        self.button = tk.Button(root,text="Click!",font=("Arial",10,"bold"),command = self.action_button)
        self.button.pack()

        self.result = tk.Label(root,text="0",font=("Arial",10,"bold"))
        self.result.pack()

    def action_button(self):
        self.counter+=1
        self.result.config(text=f"{self.counter}")


if __name__ == "__main__":
    window = tk.Tk()
    c = Count(window)
    window.mainloop()