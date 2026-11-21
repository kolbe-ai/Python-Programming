import tkinter as tk
import random


class GuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess Game")
        self.root.geometry("500x500")

        # random number each time
        self.num = random.randint(0, 10)

        # adding label
        self.label = tk.Label(root, text="Guess Game (1-10)", font=("Arial", 25, "bold"))
        self.label.pack(pady=20)

        # adding text book
        self.text = tk.Entry(root, font=("Arial", 10))
        self.text.pack()

        # adding button
        self.button = tk.Button(root, text="submit", font=("Arial", 10), command=self.check)
        self.button.pack()

        # showing result
        self.label1 = tk.Label(root, text="", font=("Arial", 15))
        self.label1.pack()

    def check(self):
        check_num = int(self.text.get())
        difference = abs(check_num - self.num)      #abs gives the absolute value instead of negative
        if (difference == 0):
            self.label1.config(text="Correct guess!")
        elif (difference >= 7):
            self.label1.config(text="Too Cold *_*")
        elif (difference >= 5):
            self.label1.config(text="Warm -_-")
        elif (difference >= 2):
            self.label1.config(text="To hot +_+!")
        else:
            self.label1.config(text = "Almost there ^_^!")

if __name__ == "__main__":
    window = tk.Tk()
    GuessGame(window)
    window.mainloop()