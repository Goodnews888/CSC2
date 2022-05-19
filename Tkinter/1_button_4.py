from tkinter import *

root = Tk()


#Create label
label = Label(root, text = "Hello Python")
label.pack()

def callback():
    label.config(text='You clicked me!', fg = 'red', bg = 'yellow')


#Create button(now with the command function)
button = Button(root,text = 'Click me!', command = callback)
button['state']='disabled' #can disable the button
button['state']='normal' #back to normal
button.pack()


root.geometry("500x300")
root.mainloop()
