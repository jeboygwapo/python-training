from turtle import Turtle, Screen
from random import randint, choice
karlu = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

# karlu.shape("turtle")
# karlu.color("green")

# Draw a square
# for _ in range(4):
#     karlu.forward(100)
#     karlu.right(90)

# Draw dashed lines
# for _ in range(20):
#     karlu.forward(5)
#     karlu.penup()
#     karlu.forward(5)
#     karlu.pendown()

# Drawing different shapes
# degrees = 360
# for x in range(3,100):
#     for _ in range(x):
#         karlu.forward(100)
#         karlu.right(degrees / x)
#     karlu.pencolor(random_color())

# Random walk
# directions = [0, 90, 180, 270]
# karlu.pensize(10)
# # Speed 1-10, where 10 is the fastest
# karlu.speed(10)
# while True:
#     karlu.pencolor(random_color())
#     karlu.setheading(choice(directions))
#     karlu.forward(20)

# Spirograph my answer
# space = 5
# degrees = 361
# karlu.speed(100)
# for _ in range(0,space+degrees,space):
#     karlu.pencolor(random_color())
#     karlu.circle(50)
#     karlu.right(space+degrees)

# Spirograph answer
def draw_spirograph(size_of_gap):
    karlu.speed("fastest")
    for _ in range (int(360 / size_of_gap)):
        karlu.color(random_color())
        karlu.circle(100)
        karlu.setheading(karlu.heading() + size_of_gap)
draw_spirograph(5)

screen.exitonclick()