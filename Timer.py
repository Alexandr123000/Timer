
from tkinter import *
from tkinter import ttk

def timer():
    global seconds
    if seconds > 0:
        label.config(text=str(seconds))
        seconds -= 1
        main.after(1000, timer)
    else:
        label.config(text="time is up")

main = Tk()

label = Label(main, text="mmm")
label.grid(row=4, column=7)

seconds = 20

timer()

main.mainloop()