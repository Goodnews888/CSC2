from tkinter import * #imports erverything from tkinter - tkinter is a module
from tkinter import ttk # ttk is a sub module

root = Tk() # top level window

#Create a label Widget

label = Label(root, text ="Hello Python")  # what you see on the screen

#font colour, config is for properties
label.config(text="Hello Python", fg="red") #Text, Font Color
label.config(bg="yellow") # background color
label.config(font='Times 20') #Size of Font

label.config(text = 'Python is a great program, and we can do lots with it')
label.config(wraplength = '150') # wrap text if long label
label.config(justify="right")
label.pack()
#Showing it on the screen

root.geometry("1000x600")

root.mainloop() # GUI is always looping - #when you run your maouse over and you can click on any buttons/labels


