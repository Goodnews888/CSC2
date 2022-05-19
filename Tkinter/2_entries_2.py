from tkinter import *
from tkinter import ttk

root = Tk()




    

entry = ttk.Entry(root, width=30) #size of the field
entry2= ttk.Entry(root, width=30)
entry.insert(0, "Please enter your name") # 0 is the index - first character
 # This will hide the password or the text entered

def showpass():
    if entry2.cget('show')=='':
        entry2.config(show='*')
        button1.config(text='Show Password')
    else:
        entry2.config(show='')
        button1.config(text ='Hide Password')

#Create entry boxes
def callback():
    val1=entry.get()
    val2=entry2.get()
    print("Your name is :" + val1)
    print("Your password is :" + val2)

button = ttk.Button(root, text = 'Sign up', command = callback)
button1= ttk.Button(root, text = 'Hide Password', command = showpass)

entry.pack()
entry2.pack()
button.pack()
button1.pack()

root.geometry("600x500")
root.mainloop()

