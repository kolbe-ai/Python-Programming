"""
(GUI: Entry + Event Handling) [PDF Q77 style] Build a temperature converter GUI (entry in °C, button, label showing °F).
"""

import tkinter as tk


class Temp:
    def __init__(self,root):
        self.root = root
        self.root.title("Temperature converter!")
        self.root.geometry("500x500")

        self.faren = 0

        self.label = tk.Label(root, text="Temperature Converter", font=("Arial", 20, "bold"))
        self.label.pack()
        self.box = tk.Entry(root, font=("Arial", 10))
        self.box.pack()
        self.label1 = tk.Label(root, text="Answer: ", font=("Arial", 10))
        self.label1.pack()
        self.button = tk.Button(root, text="CONVERT", font=("Arial", 10), command=self.action_button)
        self.button.pack()

    def action_button(self):
        cel = float(self.box.get())
        self.faren = (cel * 9/5) + 32
        self.label1.config(text=f"Answer: {self.faren}")


if __name__ == "__main__":
    window = tk.Tk()
    t = Temp(window)
    window.mainloop()
