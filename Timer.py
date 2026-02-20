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


# functions
def timer():
    seconds_of_the_time = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    start_number_of_seconds_of_the_time = seconds_of_the_time
    while seconds_of_the_time > -1:
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

def reset_the_timer():
    seconds_of_the_time = 0
    
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
pause_the_timer_button = Button(main, text="PAUSE", font=20, command=timer)
reset_the_timer_button = Button(main, text="RESET", font=20, command=reset_the_timer)


#Placing
seconds_entry.place(relx=0.65, rely=0.35)
minutes_entry.place(relx=0.55, rely=0.35)
hours_entry.place(relx=0.45, rely=0.35)
start_the_timer_button.place(relx=0.6, rely=0.5)
reset_the_timer_button.place(relx=0.7, rely=0.5)


main.mainloop()