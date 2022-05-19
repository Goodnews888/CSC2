from tkinter import *

#Quit Button
def quit():
    main_window.destroy()

def print_names():
    global j_names, total_entries
    name_count = 0
    Label(main_window, font = 'bold', text = 'List').grid(column = 0, row = 5)
    Label(main_window, font = 'bold', text = 'Name').grid(column = 1, row = 5)
    Label(main_window, font = 'bold', text = 'Age').grid(column = 2, row = 5)
    Label(main_window, font = 'bold', text = 'Gender').grid(column = 3, row = 5, padx =40)
    while name_count < total_entries :
        Label(main_window, text = name_count + 1).grid(column = 0, row = name_count + 6)
        Label(main_window, text = (j_names[name_count][0])).grid(column = 1, row = name_count + 6)
        Label(main_window, text = (j_names[name_count][1])).grid(column = 2, row = name_count + 6)
        Label(main_window, text = (j_names[name_count][2])).grid(column = 3, row = name_count + 6)
        name_count += 1
def check_validity ():
    Label(main_window, text = "Name", bg = "white").grid(column = 0, row =2)
    Label(main_window, text = "Age", bg = "white").grid(column = 0, row = 3)
    Label(main_window, text = "Gender", bg = 'white').grid(column = 0, row = 4)
    if len(entry_name.get()) != 0 and entry_age.get().isdigit() and len(entry_gender.get()) != 0:
        if int(entry_age.get()) > 0 and int (entry_age.get()) < 120:
            if (entry_gender.get().lower()) == "m" or (entry_gender.get().lower()) == "f"\
            or (entry_gender.get().lower()) == "male" or (entry_gender.get().lower()) == "female":
                append_name()
    else:
        if len(entry_name.get()) == 0 : Label(main_window, text = "Name", bg = "red") .grid(column = 0, row = 2)
        if len(entry_age.get()) == 0 : Label(main_window, text = "Age", bg = "red") .grid(column = 0, row = 3)
        if len(entry_gender.get()) == 0 : Label(main_window, text = "Gender", bg = "red") .grid(column = 0, row = 4)
        

def append_name():
    global j_names, entry_name, entry_age, entry_gender, total_entries
    j_names.append([entry_name.get(), entry_age.get(), entry_gender.get()])
    entry_name.delete(0, 'end')
    entry_age.delete(0, 'end')
    entry_gender.delete(0, 'end')
    total_entries += 1
    print(j_names)

def setup_buttons():
    global j_names, entry_name, entry_age, entry_gender, total_entries
    Button(main_window, text = "Quit", width = 10, command = quit).grid(column = 3, row = 1, padx = 20)
    Button(main_window, text = "Append Details", command = check_validity).grid(column = 0, row = 1)
    Button(main_window, text = "Print Details", command = print_names).grid(column = 1, row = 1)
    Label(main_window, text = "Name").grid(column = 0, row = 2)
    entry_name = Entry(main_window, width = 20)
    entry_name.grid(column = 1, row = 2)
    Label(main_window, text = "Age").grid(column = 0, row = 3)
    entry_age = Entry(main_window, width = 20)
    entry_age.grid(column = 1, row = 3)
    Label(main_window, text = "Gender").grid(column = 0, row = 4)
    entry_gender = Entry(main_window, width = 20)
    entry_gender.grid(column = 1, row = 4)
    


def main():
    global main_window
    global j_names, entry_name, entry_age, entry_gender, total_entries
    j_names = []
    total_entries = 0
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()
main()
