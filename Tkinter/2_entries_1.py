from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)
entry.insert(0, "Please enter your name") # 0 is the index - first character
entry2.config(show='*') # This will hide the password or the text entered

entry.pack()
entry2.pack()

root.geometry("600x500")
root.mainloop()