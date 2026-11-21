"""
Text Transformation:
Create an entry box.
Add a button "Uppercase".
When clicked, display the uppercase version of entered text in a label.
"""
import tkinter as tk

class Text:
    def __init__(self,root):
        self.root = root
        self.root.title("Text Transformation")
        self.root.geometry("500x500")

        #showing an header
        self.label = tk.Label(root,text = "Text Transformation", font = ("Arial",10,"bold"))
        self.label.pack(pady = 20)

        #showing the textbox
        self.entry = tk.Entry(root,font= ("Arial",10,"bold"), width = 20)
        self.entry.pack()

        #showing the button to change
        self.button = tk.Button(root,text = "UPPER",font = ("Arial",10,"bold"), command = self.action_button)
        self.button.pack()

        #showing the chnaged text
        self.result_text = ""
        self.label_result = tk.Label(root,text = self.result_text,font = ("Arial",10,"bold"))
        self.label_result.pack()

    def action_button(self):
        self.user = self.entry.get()           #getting user input
        self.result_text = self.user.upper()        #changing to upper
        self.label_result.config(text = self.result_text)       #showing the text



if __name__ == "__main__":
    window = tk.Tk()
    t = Text(window)
    window.mainloop()