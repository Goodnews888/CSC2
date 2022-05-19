from tkinter import *
from tkinter import ttk
import random

#This is the subroutine to end the program
def quit():
    main_window.destroy()

#This subroutine creates two random numbers between 1 and 6 and check if they are both 6
def generate_random():
    #This updates the dictionary by 1 each loop
    count_items["count_dice"] +=1
    #Set the bg color to red. It will get changed to green if there are double 6's
    bg_colour ="red"
    #Set the constants for the variable. These can be changed to alter the program
    LOW_NUMBER = 1
    HIGH_NUMBER = 6
    DOUBLE_WANTED = 6
    #Generate the two random numbers between 1 and 6
    random_number1 = random.randint(LOW_NUMBER, HIGH_NUMBER)
    random_number2 = random.randint(LOW_NUMBER, HIGH_NUMBER)
    #If both are 6 change the bg color to green
    if random_number1 == DOUBLE_WANTED and random_number2 == DOUBLE_WANTED:
        bg_colour = "green"
        #print if you get a double 6 otherwise say you didn't
        print("We got a double 6")
    else:
        print("Sorry, no double 6 this time")

    #The labels put the outputs on the GUI using text and variables
    Label(main_window, text = random_number1, bg=bg_colour, width =12).grid(column=0, row =1, sticky =E)
    Label(main_window, text=random_number2, bg=bg_colour, width=12).grid(column=1, row = 1, sticky = E)
    Label(main_window, text="roll count =", width = 12).grid(column=0, row =2, sticky=E)
    Label(main_window, text=count_items["count_dice"], width=12).grid(column=1, row=2, sticky=W)

    #The main subroutine gets the GUI configured
def main():
    #Create the quit and random buttons
    Button(main_window, text="Quit", command=quit, width=12).grid(column=0, row=0, sticky=E)
    Button(main_window, text="Random", command=generate_random, width=12).grid(column=1, row =0, sticky=E)
    #Make empty labels as placeholders
    Label(main_window, text= "").grid(column=0,row=1,sticky=E)
    Label(main_window, text= "").grid(column=1, row=1, sticky=E)
    Label(main_window, text= "").grid(column=0, row =2, sticky=E)
    Label(main_window, text= "").grid(column=1, row=2, sticky=E)
    main_window.mainloop()

    #Creates the dictionary for the count and launch the GUI
count_items = {"count_dice":0}
main_window=Tk()
main()




