from turtle import Turtle, Screen

karlu = Turtle()
screen = Screen()

def move_forwards():
    karlu.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()