from tkinter import *

root = Tk()

#My Variables
click = 999
number = 1
upgrader1 = 100
upgrader2 = 250



# Once Upgrade
def clicked():
    global click
    global number
    click+=number
    clicker["text"]= click



def shop1():
    global click
    global number
    global upgrader1
    if click >= upgrader1:
        number+=1
        click -= upgrader1
        upgrader1 = round(upgrader1 * 1.06)
        shop1["text"] = "$" + str(upgrader1)
        clicker['text'] = click


def shop2():
    global click
    global number
    global upgrader2
    if click >= upgrader2:
        number+=4
        click -= upgrader2
        upgrader2 = round(upgrader2 * 1.2)
        shop2["text"] = "$" + str(upgrader2)
        clicker['text'] = click

def Achievement():
    global click
    o = Label(root, text ="RICH MAN")
    if clicker[click] >= 1000:
        o.pack()
    

#Build Buttons
clicker = Button(root, text =  str(click), font = "Helvetica", bg = "green", height = 6, width = 9, command = clicked)
shop1 = Button(root, text = "$" + str(upgrader1), font = "Aerial", bg = "yellow", height = 3, width = 6, command=shop1)
shop2 = Button(root, text = "$" + str(upgrader2), font = "Aerial", bg = "yellow", height = 3, width = 6, command=shop2)
#Grid manager
clicker.grid(row=0, column =0)
shop1.grid(row = 0, column = 1)
shop2.grid(row = 0, column = 2)

#DISABLE Buttons
def disable_shop1():
    shop1.config(state=DISABLED)


root.geometry("500x300")
root.mainloop()