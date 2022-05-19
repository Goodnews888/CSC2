from tkinter import *

class RedFrame(Frame):
    def __init__(self, the_window):
        super().__init__()
        self["height"] = 150
        self["width"] = 150
        self["relief"] = RAISED
        self["bd"] = 8
        self["bg"] = "red"
        print("hi")

my_window = Tk()
frame_a = RedFrame(my_window)
frame_a.grid(row = 0, column = 0) 
frame_b = RedFrame(my_window)
frame_b.grid(row = 0, column = 1)


my_window.mainloop()