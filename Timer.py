from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN
from turtle import bgcolor, color

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
style.configure("green.TSeparator", background="green")

#Separators
ttk.Separator(
    master=main,
    orient=VERTICAL,
    style="green.TSeparator",
    class_= ttk.Separator,
    ).place(relx=0.3, rely=0, relwidth=0.01, relheight=1)

label = Label(main, text="mmm")
label.grid(row=4, column=7)
seconds = 20
timer()
main.mainloop()