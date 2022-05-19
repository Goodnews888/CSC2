"""In this program we will learn how to use Place Geometry Manager.
Place Geometry Manager allows us exact control over the widget's
location and size.
We can use absolute posistion and size for our widgets
We will create a login form for our application"""

from tkinter import *
root = Tk()

#Function
def Save():
    button.config(state="disabled")
    global name_
    global pass_
    name_=name_input.get()
    pass_=pass_input.get()
    print(name_)
    print(pass_)

def login():
    if name_input.get() == name_ and pass_input.get() == pass_:
        print("Login Successful")
    else:
        print("Login Unsuccessful, password and/or username wrong")
    
title = Label(root, text="Place Geometry Manager",
    font=(("Verdance"), 15))
name_txt = Label(root, text="Name :")
pass_txt = Label(root, text="Password :")
name_input = Entry(root, width=30)
pass_input = Entry(root, width=30)

#Create buttons
button = Button(root, text='Save', command = Save)
button2 = Button(root, bg = 'red', text='Click Me!', command = login)

#Use Geometry Manager to show our widgets
title.place(x=100, y=20) #x and y are in pixels - and that
# distance from the edges of the window
# Run your application to see the placement of the widget.

# placement of other widgets
name_txt.place(x=20, y=80)
name_input.place(x=100, y=80)
pass_txt.place(x=20, y=110)
pass_input.place(x=100, y=110)

#Placement of button
button.place(x=250, y=150)
button2.place(relx=0.5, rely=0.5, anchor='center')

root.geometry("450x450+650+350") #Here the 650+350 means 
#that we will locate our window on our screen. This means
#our tkinter window's x location is 650 and 
#y location is 350.
root.mainloop()
