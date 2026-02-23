import string
from tkinter import *
from tkinter import ttk
import time

# Main
main = Tk()
main.title("Timer")
main.configure(bg="skyblue")

#Variables
seconds = StringVar()
minutes = StringVar()
hours = StringVar()
seconds.set("00")
minutes.set("00")
hours.set("00")
neither_hours_nor_minutes = False
no_minutes = False
seconds_of_the_time = 0
timer_is_paused = False
current_number_of_seconds_of_the_time = 0
current_number_of_hours = "00"
current_number_of_minutes = "00"
current_number_of_seconds = "00"
timers = {}



new_timer_seconds_of_the_time = 0
new_timer_description = StringVar()
new_timer_seconds = StringVar()
new_timer_minutes = StringVar()
new_timer_hours = StringVar()

# functions
def timer():
    global seconds_of_the_time, current_number_of_hours, current_number_of_minutes, current_number_of_seconds, timer_is_paused
    if start_the_timer_button["relief"] == "sunken" and pause_the_timer_button["relief"] == "raised":
        start_the_timer_button.config(relief="raised")
    else:
        start_the_timer_button.config(relief="sunken")
    if timer_is_paused:
        seconds_of_the_time = current_number_of_seconds_of_the_time
        pause_the_timer_button.config(text="PAUSE", relief="raised")
        return
    else:
        if pause_the_timer_button.cget("text") == "PAUSED":
            pause_the_timer_button.config(text="PAUSE", relief="raised")
        seconds_of_the_time = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
        start_number_of_seconds_of_the_time = seconds_of_the_time
    while seconds_of_the_time > -1:
        if timer_is_paused:
            seconds_of_the_time = current_number_of_seconds_of_the_time
            timer_is_paused = False
            return
        number_of_minutes, number_of_seconds = (seconds_of_the_time // 60, seconds_of_the_time % 60)
        if number_of_minutes > 60 or number_of_minutes == 60:
            number_of_hours, number_of_minutes = (number_of_minutes // 60, number_of_minutes % 60)
        else:
            number_of_hours = "00"
            hours.set("00")
        if start_number_of_seconds_of_the_time < 60:
            if number_of_seconds < 10:
                seconds.set("0" + str(number_of_seconds))
                minutes.set("00")
                hours.set("00")
            else: 
                seconds.set(number_of_seconds)
                minutes.set("00")
                hours.set("00")
        elif number_of_minutes < 1:
            if number_of_seconds < 10:
                seconds.set("0" + str(number_of_seconds))
                minutes.set("00")
                hours.set("00")
            else: 
                seconds.set(number_of_seconds)
                minutes.set("00")
                hours.set("00")
        else:
            if number_of_seconds < 10:
                seconds.set("0" + str(number_of_seconds))
            else:
                seconds.set(number_of_seconds)
            if number_of_minutes < 10:
                minutes.set("0" + str(number_of_minutes))
            else:
                minutes.set(number_of_minutes)
            if int(number_of_hours) < 10 and start_number_of_seconds_of_the_time > 3599:
                hours.set("0" + str(number_of_hours))
            else:
                hours.set(number_of_hours)
        main.update()
        time.sleep(1)
        if seconds_of_the_time == 0:
            seconds.set("00")
            minutes.set("00")
            hours.set("00")
        seconds_of_the_time -= 1

def pause_the_timer():
    global timer_is_paused, current_number_of_seconds, current_number_of_minutes, current_number_of_seconds, timer_is_paused, seconds_of_the_time
    if start_the_timer_button["relief"] == "sunken":
        start_the_timer_button.config(relief="raised")
    if timer_is_paused:
        timer_is_paused = True
        return
    timer_is_paused = True
    pause_the_timer_button.config(text="PAUSED")
    pause_the_timer_button.config(relief="sunken")
    global current_number_of_seconds_of_the_time
    current_number_of_seconds_of_the_time = seconds_of_the_time
    current_number_of_hours = hours_entry.get()
    current_number_of_minutes = minutes_entry.get()
    current_number_of_seconds = seconds_entry.get()

def reset_the_timer():
    global seconds_of_the_time, current_number_of_seconds_of_the_time, neither_hours_nor_minutes, no_minutes, timer_is_paused
    seconds_of_the_time = 0
    current_number_of_seconds_of_the_time = 0
    neither_hours_nor_minutes = False
    no_minutes = False
    timer_is_paused = False
    seconds.set("00")
    minutes.set("00")
    hours.set("00")

def save_a_new_timer():
    global new_timer_seconds_of_the_time, new_timer_seconds, new_timer_minutes, new_timer_hours, new_timer_description, timers
    new_timer_seconds_of_the_time = int(new_timer_hours.get()) * 3600 + int(new_timer_minutes.get()) * 60 + int(new_timer_seconds.get())
    timers[str(new_timer_description)] = str(new_timer_seconds_of_the_time)
    print(timers)
    


def add_a_new_timer():
    new_timer_seconds.set("00")
    new_timer_minutes.set("00")
    new_timer_hours.set("00")

    new_timer_toplevel = Toplevel(main, width=300, height=200)
    new_timer_toplevel.title("Creating a new timer")

    hours_label = Label(new_timer_toplevel, text="Hours", font=20)
    minutes_label = Label(new_timer_toplevel, text="Minutes", font=20)
    seconds_label = Label(new_timer_toplevel, text="Seconds", font=20)
    description_label = Label(new_timer_toplevel, text="Seconds", font=20)

    timer_description_entry = Entry(new_timer_toplevel, textvariable=new_timer_description, width=10, font=10)
    seconds_entry = Entry(new_timer_toplevel, textvariable=new_timer_seconds, width=2, font=30)
    minutes_entry = Entry(new_timer_toplevel, textvariable=new_timer_minutes, width=2, font=30)
    hours_entry = Entry(new_timer_toplevel, textvariable=new_timer_hours, width=2, font=15)

    save_new_timer_button = Button(new_timer_toplevel, text="SAVE", command=save_a_new_timer)
    close_new_timer_button = Button(new_timer_toplevel, text="CLOSE")
    
    seconds_label.place(relx=0.5, rely=0.2)
    minutes_label.place(relx=0.3, rely=0.2)
    hours_label.place(relx=0.1, rely=0.2)
    seconds_entry.place(relx=0.1, rely=0.3)
    minutes_entry.place(relx=0.3, rely=0.3)
    hours_entry.place(relx=0.5, rely=0.3)
    timer_description_entry.place(relx=0.3, rely=0.4)
    save_new_timer_button.place(relx=0.2, rely=0.5)
    close_new_timer_button.place(relx=0.4, rely=0.5)



# Styles
style = ttk.Style()
style.configure("green.TSeparator", background="green")
#style.configure("red.TButton", bgcolor="red")

#Separators
ttk.Separator(
    master=main,
    orient=VERTICAL,
    style="green.TSeparator",
    class_= ttk.Separator,
    ).place(relx=0.3, rely=0, relwidth=0.01, relheight=1)

#Entries
seconds_entry = Entry(main, textvariable=seconds, width=10, font=15)
minutes_entry = Entry(main, textvariable=minutes, width=10, font=15)
hours_entry = Entry(main, textvariable=hours, width=10, font=15)

#Frames
placing_buttons_frame = Frame(main)
timers_frame = Frame(main, bg="red")

#Buttons
start_the_timer_button = Button(main, text="START", width=10, height=1, font=20, command=timer)
pause_the_timer_button = Button(main, text="PAUSE", width=10, height=1, font=20, command=pause_the_timer)
reset_the_timer_button = Button(main, text="RESET", width=10, height=1, font=20, command=reset_the_timer)
add_a_new_timer_button = Button(placing_buttons_frame, text="Add a timer", command=add_a_new_timer)
delete_a_timer_button = Button(placing_buttons_frame, text="Delete a timer", command=add_a_new_timer)
delete_all_timers_button = Button(placing_buttons_frame, text="Delete all timers", command=add_a_new_timer)

#Labels
#timer_settings_label = Label(timers_frame, )

#Placing
placing_buttons_frame.grid(row=0, column=2, columnspan=3)
timers_frame.grid(row=1, column=2, columnspan=3)
seconds_entry.place(relx=0.65, rely=0.35)
minutes_entry.place(relx=0.55, rely=0.35)
hours_entry.place(relx=0.45, rely=0.35)
start_the_timer_button.place(relx=0.6, rely=0.5)
pause_the_timer_button.place(relx=0.7, rely=0.5)
reset_the_timer_button.place(relx=0.8, rely=0.5)

add_a_new_timer_button.pack(side=LEFT)
delete_a_timer_button.pack(side=LEFT)
delete_all_timers_button.pack(side=LEFT)


"""add_a_new_timer_button.place()
delete_a_timer_button.place()
delete_all_timers_button.place()"""


main.mainloop()