import tkinter as tk

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x500")

        self.label1 = tk.Label(root,text="Enter user",font=("Arial",10,"bold"))
        self.label1.pack()
        self.box1 = tk.Entry(root,font=("Arial",10,"bold"))
        self.box1.pack()

        self.label2 = tk.Label(root,text="Enter password",font=("Arial",10,"bold"))
        self.label2.pack()
        self.box2 = tk.Entry(root,font=("Arial",10,"bold"))
        self.box2.pack()

        self.label3= tk.Label(root,text="",font=("Arial",10,"bold"))
        self.label3.pack()
        self.button = tk.Button(root,text = "Enter",font=("Arial",10,"bold"), command=self.action_button)
        self.button.pack()
    def action_button(self):
        user = self.box1.get()
        pass1 = self.box2.get()
        self.label3.config(text=f"Welcome user {user}")




if __name__ == "__main__":
    window = tk.Tk()
    l = Login(window)
    window.mainloop()