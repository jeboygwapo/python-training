from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# Color reference: https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_lbl.config(text="Timer")
    check_lbl.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_lbl.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_lbl.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_lbl.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global check
    count_min = count // 60
    count_sec = count % 60
    # Dynamic typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            mark += "✓"
        check_lbl.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

# Timer Text Label
title_lbl = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_lbl.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Start Button
start_btn = Button(text="Start", command=start_timer, font=(FONT_NAME, 10), bg=YELLOW, padx=10, pady=5)
start_btn.grid(column=0, row=2)

# Reset Button
reset_btn = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 10), bg=YELLOW, padx=10, pady=5)
reset_btn.grid(column=2, row=2)

# Check Label ✓
check_lbl = Label(font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)
check_lbl.grid(column=1, row=3)

window.mainloop()