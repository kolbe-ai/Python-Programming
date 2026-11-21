"""
(GUI: Button + Label) [PDF Q76] Build a window with a label and an “Add 5” button that increases the number by 5 on every click
"""

import tkinter as tk


class gui:
    def __init__(self, root):
        self.root = root
        self.title = root.title("Add by 5")
        self.geometry = root.geometry("500x500")

        self.counter = 0

        self.label = tk.Label(root, text=f"Add by 5: {self.counter}", font=("Arial", 15, "bold"))
        self.label.pack(pady = 20)
        self.button = tk.Button(root, text="click", font=("Arial", 10), command=self.action_button)
        self.button.pack(pady= 30)

    def action_button(self):
        self.counter += 5
        self.label.config(text=f"Add by 5: {self.counter}")


if __name__ == "__main__":
    window = tk.Tk()
    gui(window)
    window.mainloop()