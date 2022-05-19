# In this program we will create buttons for our list box


from tkinter import *
from tkinter import ttk

root = Tk()

# below we will add single/double or multiple/extended browse mode
# which lets you choose one or multiple items from the list

# single selection from list
listBox = Listbox(root, width=40, height=15, selectmode=MULTIPLE)
# once you have run the program with single, change the mode to MULTIPLE
# and run it again and select the items of the lsit
listBox.insert(0, "Python")
listBox.insert(1, "C++")
listBox.insert(2, "C#")
listBox.insert(3, "PHP")
listBox.pack(pady=25)

#Functions
def print_me():
    pass
def delete_me():
    select = listBox.curselection()
    for index in select[::-1]:
        listBox.delete(index)


# create buttons
button = Button(root, text='Print', command=print_me).place(x=300, y=300)
button2 = Button(root, text='Delete', command=delete_me).place(x=350,y=300)


root.geometry("650x650+650+200")
root.mainloop()