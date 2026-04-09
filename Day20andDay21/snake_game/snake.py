from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # Move segments from last to first
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move the head forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN: # Prevent turning down if going up
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP: # Prevent turning up if going down
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT: # Prevent turning right if going left
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT: # Prevent turning left if going right
            self.head.setheading(RIGHT)