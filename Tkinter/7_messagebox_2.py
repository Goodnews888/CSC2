"""In this program we are going to create a text editor in tkinter"""

from tkinter import *

root = Tk()
textEditor = Text(root, wrap=WORD, font= 'Times 20', width = 30, height = 10, fg='blue', bg='yellow') #1st parameter is root
textEditor.insert(INSERT, "Hello, I am learning about tkinter widgets by using INSERT")
textEditor.grid(row=0, column=0, pady=20, padx=40)

button = Button(root, text = "Save")

button.grid(row=3, column=0)

root.geometry("550x550")
root.mainloop()
