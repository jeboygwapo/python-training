from turtle import Turtle

WIDTH = 1
HEIGHT = 1
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DEFAULT_BALL_POSITION = (0,0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.6

    def reset_position(self):
        self.goto(DEFAULT_BALL_POSITION)
        self.move_speed = 0.1
        self.bounce_x()








