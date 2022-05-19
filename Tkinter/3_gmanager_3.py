from tkinter import *

root = Tk()

width_of_window = 200
height_of_window = 100

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (width_of_window/2)
y = (screen_height/2) - (height_of_window/2)

root.geometry(f"{width_of_window}x{height_of_window}+{int(x)}+{int(y)}")

root.mainloop()