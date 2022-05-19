#In this program we will look at doing a progress bar.


from tkinter import *
from tkinter import ttk

root = Tk()

progbar = ttk.Progressbar(root, orient=HORIZONTAL, length =200)
progbar.pack(pady=20)
progbar.config(mode='indeterminate')

# start of progress bar
progbar.start()
progbar.stop()
#say to go up to 50 and increase by 10
progbar.config(mode='determinate', maximum=50, value =10)
progbar.start()
progbar.stop()

scale = ttk.Scale(root, orient =HORIZONTAL, length=200)
scale.pack()


root.geometry("450x450+650+350")
root.mainloop()