from tkinter import *
from tkinter.ttk import *

count = 0
mode = "miles to km"

FONT = ('Helvetica', 10)

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=260)
window.config(padx=30, pady=30)


def convert_button_clicked():
    # Check if mode is in miles to km or km to miles
    global mode
    if mode == "miles to km":
        value = int(user_input.get())
        value *= 1.609
        value.__round__(3)
        answer_label.config(text=f"{value} Km")
    elif mode == "km to miles":
        value = int(user_input.get())
        value /= 1.609
        value.__round__(3)
        answer_label.config(text=f"{value} Miles")


def switch_button_clicked():
    global count
    count += 1
    if count % 2 == 0:  # If count is an even number
        global mode
        mode = "miles to km"
        title.config(text="Miles to Km")
        miles_label.config(text="Miles")
        answer_label.config(text="0 Km")
    else:
        mode = "km to miles"
        title.config(text="Km to Miles")
        miles_label.config(text="Km")
        answer_label.config(text="0 Miles")


# Title
title = Label(text="Miles to Km", font=("Lexend", 22, "bold"))
title.grid(row=0, column=1)
title.config(padding=10)

# Entry
user_input = Entry(width=20)
user_input.grid(row=1, column=1)

# Miles
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=1, column=2)
miles_label.config()

# Button
convert_button = Button(text="Convert", command=convert_button_clicked)
convert_button.grid(row=2, column=1)

# Switch Button
switch_button = Button(text="Switch", command=switch_button_clicked)
switch_button.grid(row=3, column=1)

# Result
answer_label = Label(text="0 Km", font=("Lexend", 16, "normal"))
answer_label.grid(row=4, column=1)
answer_label.config(padding=10)

window.mainloop()
