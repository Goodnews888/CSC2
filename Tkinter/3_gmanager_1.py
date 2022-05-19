from tkinter import *
from tkinter import ttk

root = Tk()

#create entries
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width = 30)

#Create placeholder
entry.insert(0, 'Please enter your Name')
entry2.insert(0, 'Please enter your password')

#Create button and labels
button = ttk.Button(root, text ='Enter')
lbltitle = ttk.Label(text='Our Title Here', font =(('Arial'), 22))
lblname = ttk.Label(text='Your name: ')
lblpass = ttk.Label(text = 'Your Password: ')

#Posistion of the buttons, labels and entries as outcome
lbltitle.grid(row=0, column = 0, columnspan = 2, pady =10) #move title to the 2nd column
lblname.grid(row=1, column = 0, sticky =W)             #W - left
lblpass.grid(row=2, column = 0, sticky =W)

entry.grid(row=1, column =1)
entry2.grid(row=2, column = 1)
#button.grid(row=3, column =1, sticky = E+W) #E+W spans it accross the cell in that column
#button.grid(row=3,column=1, sticky=E) #will have the button the right #NESW
#button.grid(row=3, column=1, sticky=W ) #will put button on the left
button.grid(row=3, column =1, sticky = E, pady=5) #gives you a bit of a gap between the two rows.

root.geometry('500x450')
root.mainloop()