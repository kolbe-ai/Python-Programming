"""
Simple Counter:
Have a button "Count".
Each time it’s clicked, increase a number shown in a label
"""
import tkinter as tk


class SimpleCounter:
    def __init__(self,root):
        self.root = root
        self.root.title("Simple Counter")
        self.root.geometry("300x400")

        self.counter = 0

        self.label = tk.Label(root,text = str(self.counter), font = ("Arial",25,"bold"))
        self.label.pack(pady=20)

        self.button = tk.Button(root,text = str("Count"), font = ("Arial",15,"bold"), command = self.action_button)
        self.button.pack()

    def action_button(self):
        self.counter += 1
        self.label.config(text = str(self.counter))

if __name__ == "__main__":
    window = tk.Tk()              #getting the window
    c = SimpleCounter(window)
    window.mainloop()