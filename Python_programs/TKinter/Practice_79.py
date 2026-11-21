"""
79. (Project) Develop a GUI-based game in Python that demonstrates event-driven programming, widgets, event handling and user interaction.
"""

import tkinter as tk
import random

class Guess:
    def __init__(self,root):
        self.root = root
        self.root.title("GUESS GAME!")
        self.root.geometry("500x500")
        self.num = random.randint(0,10)
        self.root.config(bg="black")

        #Enter the number
        self.label = tk.Label(root,text="Guess The Number: ",font=("Arial",10,"bold"),bg="red")
        self.label.pack()

        #Entry field
        self.box = tk.Entry(root,font=("Arial",10))
        self.box.pack()

        #result
        self.result = tk.Label(root,text="",font=("Arial",10,"bold"))
        self.result.pack()

        #button
        self.button = tk.Button(root,text="GUESS!",command=self.game)
        self.button.pack()
    def game(self):
        n = self.box.get()
        if (n == ""):
            self.result.config(text="Please enter number!")
        else:
            n = int(n)
            if (n == self.num):
                self.result.config(text="CORRECT GUESS",bg="Red",fg="Yellow")
            else:
                self.result.config(text="INCORRECT GUESS",bg="Red",fg="Yellow")




if __name__ == "__main__":
    window = tk.Tk()
    g = Guess(window)
    window.mainloop()