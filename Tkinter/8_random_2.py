from tkinter import *
from tkinter import ttk
import random

#Main Window
main_window = Tk()

#Entry
entry_number_guess = ttk.Entry(main_window)

#Quit Function
def quit():
    main_window.destroy() 



def number_guess():
    
    secret_number = numbers['secret_number']
    print(entry_number_guess.get())
    if int(entry_number_guess.get()) == secret_number:
        print("You've guessed correctly")
    else:
        print("You've guessed wrong")

#Label
lblname = Label(text="Your Guess: ")


#Quit Button
quit_button = Button(main_window, text = 'Quit', command = quit, width=10)



#Button that checks number_guess
check = Button(main_window, text = "Check", command = number_guess, width=12)


#Grid Manager
quit_button.grid(row=0,column=0)
check.grid(row=0, column = 1, sticky = E)
lblname.grid(row=1,column = 0)
entry_number_guess.grid(row=1, column =1)

#Create Dictionary
numbers = {"secret_number":random.randint(1, 10)}

#mainloop
main_window.mainloop()

