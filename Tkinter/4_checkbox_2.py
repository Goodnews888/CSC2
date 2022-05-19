from tkinter import *
from tkinter import ttk

root = Tk()

def callback():
    print("Your name:"+entry.get())
    print("Your Password:"+entry2.get())
    if chvar.get()==1:           #means the checkbox is checked
        print("Remember me selected")
    else:
        print("Not selected")

#Create entry boxes.
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width = 30)
entry.insert(0, 'Please enter your Name')
entry2.insert(0, 'Please enter your password')

#Create button and labels
button = ttk.Button(root, text ='Enter')
button.config(command=callback)
lbltitle = ttk.Label(text='Our Title Here', font =(('Arial'), 22))
lblname = ttk.Label(text='Your name: ')
lblpass = ttk.Label(text = 'Your Password: ')

#Posistion of the buttons, labels and entries as outcome
lbltitle.grid(row=0, column = 0, columnspan = 2, pady =10) #move title to the 2nd column
lblname.grid(row=1, column = 0, sticky =W)             #W - left
lblpass.grid(row=2, column = 0, sticky =W)
entry.grid(row=1, column =1)
entry2.grid(row=2, column = 1)
button.grid(row=3, column =1, sticky = E, pady=5) 

#checkbox
chvar=IntVar() #Checkbox variable
chvar.set(0) #set to 0 - means not checked

#checkbox variable
cbox = Checkbutton(root, text='Remember Me', variable=chvar, font ='Arial 16').grid(row=4, column =0, sticky = E, columnspan =2)

#Sticky =E, columnspan =2 #in order to get it align right


root.geometry('500x450')
root.mainloop()