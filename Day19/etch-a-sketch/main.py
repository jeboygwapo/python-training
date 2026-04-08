from turtle import Turtle, Screen

karlu = Turtle()
screen = Screen()

def move_forwards():
    karlu.forward(10)

def move_backwards():
    karlu.backward(10)

def go_left():
    karlu.left(10)

def go_right():
    karlu.right(10)

def clear():
    karlu.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=go_right)
screen.onkey(key="a", fun=go_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()