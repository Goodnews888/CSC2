from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

def callback():
    #1st perimiter will be title and then the text
    mbox = messagebox.askquestion("Delete", "Are you sure?", icon = 'warning')
    # can change icon by adding, icon = 'warning'
    if mbox == 'yes':
        print("Deleted")
    else:
        print("Not Deleted")

def callback2():
    messagebox.showinfo('Success', 'Well done!')
    print("You clicked Ok!")

button1 = ttk.Button(root, text = 'Delete', command = callback).grid(
    row=0, column = 0)
button2 = ttk.Button(root, text = 'Info', command = callback2).grid(
    row= 0, column = 1)

root.geometry('350x250')
root.mainloop()

