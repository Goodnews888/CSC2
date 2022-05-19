from tkinter import *
from tkinter import ttk


def print_myfunc():
    print("Your First Name: "+entry.get())
    print("Your Last Name: "+entry2.get())
root = Tk()




entry = Entry(root, width=15)
entry2 = Entry(root, width = 15)
entry.insert(0, '')
entry2.insert(0, '')

#Create button and labels
button1 = Button(root, text ='Print', command=print_myfunc)
button2 = Button(root, text ='Quit', command=exit)
lblname = ttk.Label(text='First Name ')
lblpass = ttk.Label(text = 'Last Name ')

#Posistion of the buttons, labels and entries as outcome

lblname.grid(row=1, column = 0, padx =5)             #W - left
lblpass.grid(row=2, column = 0, padx=5)
entry.grid(row=1, column =1, padx =5,pady=5)
entry2.grid(row=2, column = 1, padx=5)
button1.grid(row=3, column =1, pady=2) 
button2.grid(row=3, column =0, pady=2)

root.mainloop()