from tkinter import *
root = Tk()

root.title("Frames")

#Create frame using frame constructor method
#To make frame visible - use background colour
frame = Frame(root, height=300, width=300, bg='red',
bd=7, relief=SUNKEN)


#To add widgets to our frame.
#We will add buttons but you need to remember that buttons
#need to be within the frame and not in the root because the button
#will be the child of the frame and the frame is the child of the top
#root level window.

#So we will use:
button1 = Button(frame, text="Button1")
button2 = Button(frame, text="Button2")
button1.pack(side=LEFT, padx=20, pady=50)
button2.pack(side=LEFT, padx=20, pady=50)

#Creating SearchBar Label
searchBar = LabelFrame(root,text='Search Box')
searchBar.pack(padx=20, pady=20)

Search = Label(searchBar, text ="Search")
Search.pack(side=LEFT, padx =10)

searchEntry = Entry(searchBar)
searchEntry.pack(side=LEFT, padx=10)

searchButton = Button(searchBar, text = "Search")
searchButton.pack(side=LEFT, padx=10)
#We get the window with the button only which is in front of the frame.
#To solve this problem we will use fill(X)
frame.pack(fill=X)


root.geometry("650x650+450+200")
root.mainloop()