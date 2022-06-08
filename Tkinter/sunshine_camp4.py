from tkinter import ttk
from tkinter import *

main_window = Tk()

# Quit function

def exit():
    main_window.destroy()

# Print details function

def print_info():
    global supreme_list, total_entries, name_count, y_increase
    name_count = 0
    Label(main_window, font='bold',text="Row").grid(column=0,row=7)
    Label(main_window, font='bold',text="Leader").grid(column=1,row=7)
    Label(main_window, font='bold',text="Location").grid(column=2,row=7)
    Label(main_window, font='bold',text="Number of Campers").grid(column=3,row=7)
    Label(main_window, font='bold',text="Weather").grid(column=4,row=7)

    while name_count < total_entries :
        Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
        Label(main_window, text=(supreme_list[name_count][0])).grid(column=1,row=name_count+8)
        Label(main_window, text=(supreme_list[name_count][1])).grid(column=2,row=name_count+8)
        Label(main_window, text=(supreme_list[name_count][2])).grid(column=3,row=name_count+8)
        Label(main_window, text=(supreme_list[name_count][3])).grid(column=4,row=name_count+8)
        name_count += 1

# Append detail function

def append_info():
    global supreme_list, Leader_entry, Location_entry, total_entries, campers, num_campers, weather, Weather_entry
    supreme_list.append([Leader_entry.get(), Location_entry.get(), weather.get(), campers.get()])
    Leader_entry.delete(0, 'end')
    Location_entry.delete(0, 'end')
    Weather_entry.delete(0, 'end')
    campers.set("") # Prints the new value each time
    weather.set("")
    #Weather_entry.delete(0, 'end')
    #Row_entry.delete(0, 'end')
    total_entries += 1


# Create the delete function

def delete():
    global supreme_list, Rows_entry, total_entries, name_count, y_increase, Rows_entry

    del supreme_list[int(Rows_entry.get())]
    total_entries = total_entries - 1
    Rows_entry.delete(0, 'end')
    Label(main_window, text="                                ").place(x=10, y=y_increase+50)
    Label(main_window, text="                                ").place(x=90, y=y_increase+50)
    Label(main_window, text="                                ").place(x=170, y=y_increase+50)
    Label(main_window, text="                                ").place(x=250, y=y_increase+50)
    Label(main_window, text="                                ").place(x=330, y=y_increase+50)
    print_info()

# Def setup buttons

def setup_buttons():
    global supreme_list, Leader_entry, Location_entry, Number_entry, Weather_entry, total_entries, campers, num_campers, weather, Rows_entry
    # Buttons
    quit_button = Button(main_window, text="Quit", command=exit).place(x=130, y=5)
    append_details = Button(main_window, text="Append details", command=append_info).place(x=10, y=35)
    print_details = Button(main_window, text="Print details", command=print_info).place(x=130, y=35)
    delete_details = Button(main_window, text="Delete", command=delete).place(x=300, y=145)

    # Labels
    Leader_label = Label(main_window, text="Leader: ").place(x=10, y=70)
    Location_label = Label(main_window, text="Location: ").place(x=10, y=90)
    Number_label = Label(main_window, text="Number of campers: ").place(x=10, y=110)
    Weather_label = Label(main_window, text="Weather: ").place(x=10, y=130)
    Row_label = Label(main_window, text="Row: ").place(x=10, y=150)

    # Entries
    Leader_entry = Entry(main_window)
    Leader_entry.place(x=150, y=70)
    Location_entry = Entry(main_window)
    Location_entry.place(x=150, y=90)
    #Row_entry = Entry(main_window)
    #Row_entry.place(x=150, y=150)

    # Create the spinbox for the number_of campers

    campers = StringVar()
    num_campers = Spinbox(main_window, from_=5, to=10, textvariable=campers, state='readonly').grid(column=1,row=4)

    # Create the combobox for weather
    weather = StringVar()
    Weather_entry = ttk.Combobox(main_window, textvariable=weather, state='readonly', 
    value = ('Sunny', 'Cloudy', 'Stormy', 'Rainy', 'Snowy', 'Misty')).place(x=150, y=130)

    # Create the combobox for the number of rows
    #Row = StringVar()
    #Rows = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    Rows_entry = Entry(main_window).place(x=344, y=150)

# Main function of the code

def main():
    global main_window
    global supreme_list, Leader_entry, Location_entry, Row_entry, total_entries, campers
    supreme_list = [] # List that would contain the other lists
    setup_buttons()
    total_entries = 0 # Total amount of entries, everytime you append a list to a list total list += 1
    main_window.geometry("500x500")
    main_window.mainloop()

main()
