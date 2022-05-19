#Deck Planner Task 30/04/22

from tkinter import *
root = Tk()


#Labels
lbl_Length = Label(root, text = "Length")
lbl_Width = Label(root, text = "Width")
lbl_Height = Label(root, text = "Height")

lbl_Area = Label(root, text = "Area")
lbl_Posts = Label(root, text = "Posts")
lbl_PostLength = Label(root, text = "Post Length")
lbl_CementBags = Label(root, text = "Cement Bags")
lbl_Bearers = Label(root, text = "Bearers")
lbl_Joists = Label(root, text = "Joists")
lbl_Decking = Label(root, text = "Decking")


#Input Variables
Length = Entry(root)
Width = Entry(root)
Height = Entry(root)

#Functions (Quit, Calculate)
def Quit():
    root.destroy()

def Calculate():
    length = int(Length.get())
    width = int(Width.get())
    height = int(Height.get())
    Area = length * width
    Posts = (length + 1) * width
    if height <=1:
        Post_Length = 1.8
    else:
        Post_Length = 2.4
    Cement_Bags = Posts
    Bearers = Area * 2
    Joists = Area/.4
    Decking = Area * 11

    #Creating Labels to display Deck Planner Information to end-user
    Label(root, text = Area).grid(row = 4, column = 1)
    Label(root, text = Posts).grid(row = 5, column = 1)
    Label(root, text = Post_Length).grid(row = 6, column = 1)
    Label(root, text = Cement_Bags).grid(row = 7, column = 1)
    Label(root, text = Bearers).grid(row = 8, column = 1)
    Label(root, text = Joists).grid(row = 9, column = 1)
    Label(root, text = Decking).grid(row = 10, column = 1)


    



#Buttons
Quit = Button(root, text = "Quit", command = Quit)
Calculate = Button(root, text = "Calculate", command = Calculate )



#Grid Manager
Quit.grid(row = 0, column = 0)
Calculate.grid(row = 0, column = 1)

lbl_Length.grid(row = 1, column = 0, padx =10, pady =10)
Length.grid(row = 1, column = 1)

lbl_Width.grid(row = 2, column = 0)
Width.grid(row = 2, column = 1)

lbl_Height.grid(row = 3, column = 0, pady =10)
Height.grid(row = 3, column = 1)

lbl_Area.grid(row = 4, column = 0)

lbl_Posts.grid(row = 5, column = 0)

lbl_PostLength.grid(row = 6, column = 0)

lbl_CementBags.grid(row = 7, column = 0)

lbl_Bearers.grid(row = 8, column = 0)

lbl_Joists.grid(row = 9, column = 0)

lbl_Decking.grid(row = 10, column = 0)



root.geometry("350x400")



root.mainloop()