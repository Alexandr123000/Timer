from tkinter import *
from tkinter import ttk
from turtle import bgcolor

# functions
def timer(): # function with timer
    global seconds
    if seconds > 0:
        label.config(text=str(seconds))
        seconds -= 1
        main.after(1000, timer)
    else:
        label.config(text="time is up")

# Main
main = Tk()
main.title("Timer")
main.configure(bg="skyblue")

# Styles
style = ttk.Style()
style.configure("TSeparator", bgcolor="red")

#Separators
ttk.Separator(
    master=main,
    orient=VERTICAL,
    style="TSeparator",
    class_= ttk.Separator,
    )




l = Toplevel(main, bg="blue")
label = Label(main, text="mmm")
label.grid(row=4, column=7)
seconds = 20
timer()
main.mainloop()