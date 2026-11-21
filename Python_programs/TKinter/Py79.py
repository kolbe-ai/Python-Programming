"""
Project:
Develop a GUI-based game using Python that demonstrates the concepts of event-driven programming,
widgets, event handling, and user interaction.
"""
import tkinter as tk
import random


class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Me")
        self.root.geometry("500x500")

        #adding title
        self.label = tk.Label(root, text="Click me game", font=("Arial", 10, "bold"))
        self.label.pack(pady=20)

        #adding score
        self.count = 0
        self.label1 = tk.Label(root, text = str(self.count), font = ("Arial",10,"bold"))
        self.label1.pack()

        #adding button
        self.button = tk.Button(root, text="CLICK ME !!", font=("Arial", 20, "bold"), command=self.change)
        self.button.pack()
        self.button.place(x=200, y=100)

    def change(self):
        self.count += 1
        self.label1.config(text = str(self.count))
        random_x = random.randint(20, 400)
        random_y = random.randint(20, 400)

        self.button.place(x=random_x, y = random_y)


if __name__ == "__main__":
    window = tk.Tk()
    Game(window)
    window.mainloop()
