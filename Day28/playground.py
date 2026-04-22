WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
check = ""


work_sec = WORK_MIN * 60
short_break_sec = SHORT_BREAK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60

while REPS < 7:
    REPS += 1
    if REPS % 2 == 0:
        print("Short Break")
        print(check)
        check += "✓"

    else:
        print("Work")
print("Long Break")
