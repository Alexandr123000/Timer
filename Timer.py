from tkinter import *
from tkinter import ttk
import time

# Main
main = Tk()
main.title("Timer")
main.configure(bg="skyblue")
main.resizable(False, False)
main.geometry("800x400")

# Variables
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
new_timer_toplevel = 0
counter_for_widgets = []
counter_to_count_widgets = 0
new_timer_seconds_of_the_time = 0
new_timer_description = StringVar()
new_timer_seconds = StringVar()
new_timer_minutes = StringVar()
new_timer_hours = StringVar()

# functions
def timer():
    global seconds_of_the_time, current_number_of_hours, current_number_of_minutes, current_number_of_seconds, timer_is_paused
    
    if timer_is_paused:
        seconds_of_the_time = current_number_of_seconds_of_the_time
        pause_the_timer_button.config(text="PAUSE")
        return
    else:
        if pause_the_timer_button.cget("text") == "PAUSED":
            pause_the_timer_button.config(text="PAUSE")
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
    if timer_is_paused:
        timer_is_paused = True
        return
    timer_is_paused = True
    pause_the_timer_button.config(text="PAUSED")
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

def delete_all_timers():
    global counter_for_widgets
    for widget in counter_for_widgets:
        if isinstance(widget, Frame):
            widget.destroy()
    counter_for_widgets.clear()

def delete_timer(description):
    global counter_for_widgets
    counter = 4
    for widget in counter_for_widgets:
        if isinstance(widget, ttk.Button):
            if widget.cget("text") == "DELETE":
                if counter_for_widgets[counter-2].cget("text") == description:
                    counter_for_widgets[counter-4].destroy()
                    del counter_for_widgets[(counter-4):(counter+1)]
                    break
                counter += 5

def select_timer(description):
    global hours, minutes, seconds
    counter_for_the_list = 3
    selected_hours = "00"
    selected_minutes ="00"
    selected_seconds = "00"
    counter_for_the_time = 0
    for widget in counter_for_widgets:
        if isinstance(widget, ttk.Button):
            if widget.cget("text") == "SELECT":
                if counter_for_widgets[counter_for_the_list-1].cget("text") == description:
                    selected_hours = ""
                    selected_minutes = ""
                    selected_seconds = ""
                    for hours_counter in counter_for_widgets[counter_for_the_list-2].cget("text"):
                        selected_hours += hours_counter
                        counter_for_the_time += 1
                        if hours_counter == ":":
                            break
                    the_rest_of_the_list = counter_for_widgets[counter_for_the_list-2].cget("text")[counter_for_the_time:]
                    for minutes_counter in the_rest_of_the_list:
                        selected_minutes += minutes_counter
                        counter_for_the_time += 1
                        if minutes_counter == ":":
                            break
                    the_rest_of_the_list = counter_for_widgets[counter_for_the_list-2].cget("text")[counter_for_the_time:]
                    for seconds_counter in the_rest_of_the_list:
                        selected_seconds += seconds_counter
                        counter_for_the_time += 1
                    break
                counter_for_the_list += 5
    hours.set(selected_hours)
    minutes.set(selected_minutes)
    seconds.set(selected_seconds)

def save_a_new_timer():
    global new_timer_toplevel, counter_for_widgets, counter_to_count_widgets
    number_of_seconds = "00"
    number_of_minutes = "00"
    number_of_hours = "00"
    global new_timer_seconds_of_the_time, new_timer_seconds, new_timer_minutes, new_timer_hours, new_timer_description, timers
    new_timer_seconds_of_the_time = int(new_timer_hours.get()) * 3600 + int(new_timer_minutes.get()) * 60 + int(new_timer_seconds.get())
    timers[str(new_timer_description.get())] = str(new_timer_seconds_of_the_time)
    number_of_minutes, number_of_seconds = (new_timer_seconds_of_the_time // 60, new_timer_seconds_of_the_time % 60)
    if number_of_minutes > 60 or number_of_minutes == 60:
        number_of_hours, number_of_minutes = (number_of_minutes // 60, number_of_minutes % 60)
    else:
        number_of_hours = "00"
    if int(number_of_seconds) < 10 and int(number_of_seconds) != 0:
        number_of_seconds = "0" + str(number_of_seconds)
    if int(number_of_minutes) < 10 and int(number_of_minutes) != 0:
        number_of_minutes = "0" + str(number_of_minutes)
    if int(number_of_hours) < 10 and int(number_of_hours) != 0:
        number_of_hours = "0" + str(number_of_hours)
    if int(number_of_seconds) == 0:
        number_of_seconds = "00"
    if int(number_of_minutes) == 0:
        number_of_minutes = "00"
    if int(number_of_hours) == 0:
        number_of_hours = "00"
    timer_description = new_timer_description.get()
    new_timer_frame = Frame(timers_frame,bg="yellow")
    new_timer_label = ttk.Label(new_timer_frame, text=(str(number_of_hours) + ":" + str(number_of_minutes) + ":" + str(number_of_seconds)), style="ExistingTimerLabel.TLabel")
    new_timer_description_label = ttk.Label(new_timer_frame, text=new_timer_description.get(), style="ExistingTimerDescriptionLabel.TLabel")
    select_the_new_timer_button = ttk.Button(new_timer_frame, name="selectButton", text="SELECT", style="ExistingTimerButtons.TButton", width=6.2, command= lambda: select_timer(timer_description))
    delete_the_new_timer_button = ttk.Button(new_timer_frame, name="deleteButton", text="DELETE", style="ExistingTimerButtons.TButton", width=6.2, command= lambda: delete_timer(timer_description))
    counter_for_widgets.append(new_timer_frame) 
    counter_for_widgets.append(new_timer_label)
    counter_for_widgets.append(new_timer_description_label)
    counter_for_widgets.append(select_the_new_timer_button)
    counter_for_widgets.append(delete_the_new_timer_button)
    new_timer_frame.pack(side=TOP, fill=BOTH)
    new_timer_description_label.pack(side=LEFT)
    delete_the_new_timer_button.pack(side=RIGHT)
    select_the_new_timer_button.pack(side=RIGHT)
    new_timer_label.pack(side=RIGHT)
    counter_to_count_widgets += 1

def add_a_new_timer():
    global new_timer_toplevel
    new_timer_seconds.set("00")
    new_timer_minutes.set("00")
    new_timer_hours.set("00")
    new_timer_toplevel = Toplevel(main, width=300, height=250)
    new_timer_toplevel.title("Creating a new timer")
    new_timer_toplevel.resizable(False, False)
    hours_label = ttk.Label(new_timer_toplevel, text="Hours", style="TimeForNewTimerLabels.TLabel")
    minutes_label = ttk.Label(new_timer_toplevel, text="Minutes", style="TimeForNewTimerLabels.TLabel")
    seconds_label = ttk.Label(new_timer_toplevel, text="Seconds", style="TimeForNewTimerLabels.TLabel")
    description_label = ttk.Label(new_timer_toplevel, text="Description", style="DescriptionLabel.TLabel")
    timer_description_entry = ttk.Entry(new_timer_toplevel, textvariable=new_timer_description, width=22, style="TimerDescriptionEntry.TEntry", font=("", 12, ""))
    seconds_entry = ttk.Entry(new_timer_toplevel, textvariable=new_timer_seconds, width=2, style="TimeForNewTimerEntries.TEntry", font=("", 19, ""))
    minutes_entry = ttk.Entry(new_timer_toplevel, textvariable=new_timer_minutes, width=2, style="TimeForNewTimerEntries.TEntry", font=("", 19, ""))
    hours_entry = ttk.Entry(new_timer_toplevel, textvariable=new_timer_hours, width=2, style="TimeForNewTimerEntries.TEntry", font=("", 19, ""))
    save_new_timer_button = ttk.Button(new_timer_toplevel, text="SAVE", style="NewTimerButton.TButton", command=save_a_new_timer)
    seconds_label.place(relx=0.66, rely=0.17)
    minutes_label.place(relx=0.37, rely=0.17)
    hours_label.place(relx=0.1, rely=0.17)
    seconds_entry.place(relx=0.74, rely=0.3)
    minutes_entry.place(relx=0.44, rely=0.3)
    hours_entry.place(relx=0.14, rely=0.3)
    description_label.place(relx=0.33, rely=0.52)
    timer_description_entry.place(relx=0.16, rely=0.65)
    save_new_timer_button.place(relx=0.36, rely=0.81)

# Styles
style = ttk.Style()
style.configure("green.TSeparator", background="green")
style.configure("MainTimerButtons.TButton", width=10, height=1, font=("", 16, ""))
style.configure("AddNewTimerButton.TButton", width=24)
style.configure("DeleteAllTimersButton.TButton", width=14)
style.configure("TimeEntries.TEntry", foreground="red")
style.configure("TimeLabels.TLabel")
style.configure("TimeForNewTimerLabels.TLabel", font=("", 14, ""))
style.configure("TimeForNewTimerEntries.TEntry", foreground="red")
style.configure("NewTimerButton.TButton", font=("", 10, ""))
style.configure("DescriptionLabel.TLabel", font=("", 14, ""))
style.configure("TimerDescriptionEntry.TEntry")
style.configure("ExistingTimerButtons.TButton", font=("", 8, ""))
style.configure("ExistingTimerDescriptionLabel.TLabel", font=("", 10, ""))
style.configure("ExistingTimerLabel.TLabel", font=("", 10, ""))
style.configure("DividersLabels.TLabel", font=("", 10, ""))

# Separators
ttk.Separator(
    master=main,
    orient=VERTICAL,
    style="green.TSeparator",
    class_= ttk.Separator,
    ).place(relx=0.31, rely=0, width=3, height=400)

# Frames
placing_buttons_frame = Frame(main)
timers_frame = Frame(main, bg="red", width=250, height=400)
timers_frame.pack_propagate(0)

# Entries
seconds_entry = ttk.Entry(main, textvariable=seconds, style="TimeEntries.TEntry", width=2, font=("", 30, ""))
minutes_entry = ttk.Entry(main, textvariable=minutes, style="TimeEntries.TEntry", width=2, font=("", 30, ""))
hours_entry = ttk.Entry(main, textvariable=hours, style="TimeEntries.TEntry", width=2, font=("", 30, ""))

# Buttons
start_the_timer_button = ttk.Button(main, text="START", style="MainTimerButtons.TButton", command=timer)
pause_the_timer_button = ttk.Button(main, text="PAUSE", style="MainTimerButtons.TButton", command=pause_the_timer)
reset_the_timer_button = ttk.Button(main, text="RESET", style="MainTimerButtons.TButton", command=reset_the_timer)
add_a_new_timer_button = ttk.Button(placing_buttons_frame, text="Add a timer", style="AddNewTimerButton.TButton", command=add_a_new_timer)
delete_all_timers_button = ttk.Button(placing_buttons_frame, text="Delete all timers", style="DeleteAllTimersButton.TButton", command=delete_all_timers)

# Labels
hours_label = ttk.Label(main, text="Hours", font=("", 17, ""))
minutes_label = ttk.Label(main, text="Minutes", font=("", 17, ""))
seconds_label = ttk.Label(main, text="Seconds", font=("", 17, ""))
first_divider_label = ttk.Label(main, text=":", style="DividersLabels.TLabel", font=("", 25, ""))
seconds_divider_label = ttk.Label(main, text=":", style="DividersLabels.TLabel", font=("", 25, ""))

# Placing
placing_buttons_frame.grid(row=0, column=0)
timers_frame.grid(row=1, column=0)
hours_label.place(relx=0.494, rely=0.23)
minutes_label.place(relx=0.63, rely=0.23)
seconds_label.place(relx=0.778, rely=0.23)
seconds_entry.place(relx=0.8, rely=0.35)
first_divider_label.place(relx=0.75, rely=0.35)
minutes_entry.place(relx=0.65, rely=0.35)
seconds_divider_label.place(relx=0.6, rely=0.35)
hours_entry.place(relx=0.5, rely=0.35)
start_the_timer_button.place(relx=0.4, rely=0.6)
pause_the_timer_button.place(relx=0.6, rely=0.6)
reset_the_timer_button.place(relx=0.8, rely=0.6)
add_a_new_timer_button.pack(side=LEFT)
delete_all_timers_button.pack(side=LEFT)

main.mainloop()