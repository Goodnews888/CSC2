"""This program is so we know where camps are overnight
Need to ensure that the quit subroutine is added along with the main function which
needs to be called.
Then create the labels and buttons"""


from tkinter import *
from tkinter import ttk

#quit subroutine
def quit():
    main_window.destroy()

#print details of all the camps
def print_camp_details ():
    global j_names, total_entries, name_count
    name_count = 0
    Label(frame, font='bold',text="Row").grid(column=0,row=7, columnspan = 1)
    Label(frame, font='bold',text="Leader").grid(column=1,row=7)
    Label(frame, font='bold',text="Location").grid(column=2,row=7, columnspan = 1)
    Label(frame, font='bold',text="Number of Campers").grid(column=3,row=7)
    Label(frame, font='bold',text="Weather").grid(column=4,row=7, columnspan =1)
    frame.grid(column =0, row = 7, columnspan = 4, rowspan = 10)

    while name_count < total_entries :
        Label(frame, text=name_count).grid(column=0,row=name_count+8) 
        Label(frame, text=(camp_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(frame, text=(camp_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(frame, text=(camp_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(frame, text=(camp_details[name_count][3])).grid(column=4,row=name_count+8)
        name_count +=  1

#add the next camper to the list
def append_name ():
    
    global camp_details, entry_leader,entry_location,entry_campers,entry_weather, total_entries, weather
    camp_details.append([entry_leader.get(),entry_location.get(),entry_campers.get(),entry_weather.get()])
    weather.set("")
    entry_leader.delete(0,'end')
    entry_location.delete(0,'end')
    entry_campers.delete(0,'end')
    entry_weather.delete(0,'end')
    total_entries +=  1

#delete a row from the list
def delete_row ():
    global camp_details, delete_item, total_entries, name_count
    Button(main_window, text="Delete",command=delete_row) .grid(column=2,row=6)
    Label(main_window, text="Row #") .grid(column=0,row=6)
    try:
        del camp_details[int(delete_item.get())]
        total_entries = total_entries - 1
        delete_item.delete(0,'end')

        for widget in frame.winfo_children():
            widget.destroy()
        frame.pack_forget()
        print_camp_details()
    except:
        Label(main_window, text="Row #", bg = "red") .grid(column=0,row=6)

#create the buttons and labels
def setup_buttons():
    global camp_details, entry_leader,entry_location,entry_campers,entry_weather, total_entries, delete_item, weather, frame2
    Button(main_window, text="Quit",command=quit) .grid(column=2, row=0, sticky = E)
    Button(main_window, text="Update",command=check_validity) .grid(column=1,row=1)
    Label(main_window, text="Leader") .grid(column=0,row=2)

    #Entry for Leader
    entry_leader = Entry(main_window)
    entry_leader.grid(column=1,row=2)
    Label(main_window, text="Location") .grid(column=0,row=3)
    
    #Title
    Label(main_window, text= "Sunshine Adventure", font =(('Aerial'), 12)).grid(column=0, row = 0)
    Label(main_window, text = "Camp", font = (('Aerial'), 12)).grid(column=0, row = 1)

    #Entry for Location
    entry_location = Entry(main_window)
    entry_location.grid(column=1,row=3)
    Label(main_window, text="Number of Campers") .grid(column=0,row=4)

    #Entry for Campers
    entry_campers = Entry(main_window)
    entry_campers.grid(column=1,row=4)
    Label(main_window, text="Weather") .grid(column=0,row=5)

    #Combobox for Weather
    weather = StringVar()
    entry_weather = ttk.Combobox(main_window, textvariable = weather, state = 'readonly',
    values = ('Sunny', 'Cloudy', 'Stormy', 'Rainy', 'Snowy', 'Misty'))
    entry_weather.grid(column=1,row=5)

    #Constructing the Row # & Delete button.
    Label(main_window, text="Row #") .grid(column=0,row=6)
    delete_item = Entry(main_window)
    delete_item.grid(column=1,row=6)
    Button(main_window, text="Delete",command=delete_row) .grid(column=2,row=6)

def check_validity ():
    Label(main_window, text = "Leader").grid(column = 0, row =2)
    Label(main_window, text = "Location").grid(column = 0, row = 3)
    Label(main_window, text = "Number of Campers").grid(column = 0, row = 4)
    Label(main_window, text = "Weather").grid(column = 0, row = 5)
    if len(entry_leader.get()) != 0 and entry_campers.get().isdigit() and len(entry_weather.get()) != 0 and len(entry_location.get()) != 0:
        if int(entry_campers.get()) >= 5 and int(entry_campers.get()) <= 10:
            append_name()
            print_camp_details()
        else:
            Label(main_window, text = "Number of Campers", bg = "red").grid(column = 0, row = 4 ) 
                
    else:
        if len(entry_leader.get()) == 0 : Label(main_window, text = "Leader", bg = "red") .grid(column = 0, row = 2)
        if len(entry_location.get()) == 0 : Label(main_window, text = "Location", bg = "red") .grid(column = 0, row = 3)
        if len(entry_weather.get()) == 0 : Label(main_window, text = "Weather", bg = "red") .grid(column = 0, row = 5)
        if entry_campers.get().isdigit():
            if len(entry_campers.get()) == 0 or int(entry_campers.get()) < 5 or int(entry_campers.get()) > 10: Label(main_window, text = "Number of Campers", bg = "red").grid(column = 0, row = 4 )
        else: Label(main_window, text = "Number of Campers", bg = "red").grid(column = 0, row = 4 ) 
        
#start the program running
def main():
    global main_window
    global camp_details, entry_name,entry_age,entry_gender, total_entries, frame
    camp_details = []
    total_entries = 0
    main_window =Tk()
    frame = Frame(main_window)
    setup_buttons()
    main_window.mainloop()
    
main()