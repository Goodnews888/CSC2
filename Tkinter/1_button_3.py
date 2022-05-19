from tkinter import *
from tkinter import ttk

root = Tk()

#some widgets available only in ttk and some in Tkinter
# we will see the dfference here with the buttons

button1 = Button(root, text="Click Me!") #button created using tkinter
button2 = ttk.Button(root, text = "Click Me!") #button created using ttk
# if you run it now you will see an empty GUI as the buttons don't show up 
# have to use geoemtry manager to be able
#to see the buttons
# here we will use .pack() to show our buttons

button1.pack()
button2.pack()

#Here we create our geometry manager to display GUI
root.geometry("600x500")
root.mainloop()








