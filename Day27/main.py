#import tkinter as tk
from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300

window = Tk()
window.title("My First GUI Program")
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(padx=50, pady=50)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Button
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry()
print(input.get())
input.grid(column=3, row=2)




window.mainloop()