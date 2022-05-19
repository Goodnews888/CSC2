from tkinter import *

root = Tk()

#Create label
label = Label(root, text = "Hello Python")
label.pack()

#Create button(without command does not do anything)
button = Button(root, text = 'Click me!')
button.pack()

root.geometry("350x300")
root.mainloop()

