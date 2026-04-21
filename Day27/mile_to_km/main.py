from tkinter import *

# Constant for conversion
MILE_TO_KM = 1.60934

def calculate_km():
    try:
        # Get input and convert to float
        miles = float(user_input.get())
        km = miles * MILE_TO_KM
        # Update label with rounded result
        km_output_label.config(text=f"{km:.2f}", fg="black")
    except ValueError:
        # Handle cases where input is not a number
        km_output_label.config(text="Invalid Input", fg="red", font=("Arial", 10))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=30, pady=30)

user_input = Entry(width=10, font=("Arial", 12))
user_input.insert(0, "0") # Default value
user_input.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0, padx=10)

# Is equal to Label
is_equal_to_label = Label(text="is equal to", font=("Arial", 12))
is_equal_to_label.grid(column=0, row=1, pady=10)

# Km output Label
km_output_label = Label(text="0", font=("Arial", 12, "bold"))
km_output_label.grid(column=1, row=1)

# Km text Label
km_text_label = Label(text="Km", font=("Arial", 12))
km_text_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=calculate_km, font=("Arial", 10, "bold"))
button.grid(column=1, row=2, pady=10)

window.mainloop()
