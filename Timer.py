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
timer_was_paused = False
"""global function_running
function_running = False"""
current_number_of_seconds_of_the_time = 0
current_number_of_hours = "00"
current_number_of_minutes = "00"
current_number_of_seconds = "00"

# functions
def timer():
    print("vvv")
    global seconds_of_the_time, current_number_of_hours, current_number_of_minutes, current_number_of_seconds, timer_is_paused, timer_was_paused
    print(timer_was_paused)
    """if timer_is_paused:
        seconds_of_the_time = current_number_of_seconds_of_the_time
        print("isisis")
        timer_is_paused = False
        timer_was_paused = True
        pause_the_timer_button.config(text="PAUSE")
        print(current_number_of_seconds)
        return
    else:
        if timer_was_paused == True:
            seconds_entry.config(text=current_number_of_seconds)
            minutes_entry.config(text=current_number_of_minutes)
            hours_entry.config(text=current_number_of_hours)
            timer_was_paused = False"""
    if timer_is_paused:
        seconds_entry.config(text=current_number_of_seconds)
        minutes_entry.config(text=current_number_of_minutes)
        hours_entry.config(text=current_number_of_hours)
        seconds_of_the_time = 0
        timer_is_paused = False
        timer_was_paused = True
        print(timer_was_paused)
        print(current_number_of_seconds_of_the_time)
        return

    else:
        seconds_of_the_time = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
        start_number_of_seconds_of_the_time = seconds_of_the_time
    while seconds_of_the_time > -1:
        if timer_was_paused:
            seconds_of_the_time = current_number_of_seconds_of_the_time
            timer_was_paused = False
            print("ww")
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
    timer_is_paused = True
    pause_the_timer_button.config(text="PAUSED")
    global current_number_of_seconds_of_the_time
    current_number_of_seconds_of_the_time = seconds_of_the_time
    seconds_of_the_time = 0
    current_number_of_hours = hours_entry.get()
    current_number_of_minutes = minutes_entry.get()
    current_number_of_seconds = seconds_entry.get()
    print("zzz" + str(current_number_of_seconds_of_the_time))

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

# Styles
style = ttk.Style()
style.configure("green.TSeparator", background="green")

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

#Buttons
start_the_timer_button = Button(main, text="START", font=20, command=timer)
pause_the_timer_button = Button(main, text="PAUSE", font=20, command=pause_the_timer)
reset_the_timer_button = Button(main, text="RESET", font=20, command=reset_the_timer)

#Placing
seconds_entry.place(relx=0.65, rely=0.35)
minutes_entry.place(relx=0.55, rely=0.35)
hours_entry.place(relx=0.45, rely=0.35)
start_the_timer_button.place(relx=0.6, rely=0.5)
pause_the_timer_button.place(relx=0.7, rely=0.5)
reset_the_timer_button.place(relx=0.8, rely=0.5)


main.mainloop()