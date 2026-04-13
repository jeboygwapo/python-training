from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
POSITION = (-220, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(POSITION)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"LEVEL: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
