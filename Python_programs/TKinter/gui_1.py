"""
(GUI: Entry + Event Handling) [PDF Q77] Build an entry box and a “Reverse” button that shows the reversed text in a label.
"""

import tkinter as tk


class Reverse:
    def __init__(self, root):
        self.root = root
        self.root.title("Reverse")
        self.root.geometry("500x500")

        self.word = ""

        self.label = tk.Label(root, text="Enter the text: ", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.label1 = tk.Label(root, text="Result: ", font=("Arial", 15, "bold"))
        self.label1.pack()
        self.box = tk.Entry(root, font=("Arial", 10))
        self.box.pack()
        self.button = tk.Button(root, text="REVERSE", font=("Arial", 10), command=self.action_button)
        self.button.pack()

    def action_button(self):
        word = self.box.get()
        rev_word = word[::-1]
        self.label1.config(text=f"Result: {rev_word}")


if __name__ == "__main__":
    window = tk.Tk()
    r = Reverse(window)
    window.mainloop()
