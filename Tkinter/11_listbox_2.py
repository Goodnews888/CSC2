# In this program we will use browse mode for selection of items in a list

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

root.geometry("650x650+650+200")
root.mainloop()