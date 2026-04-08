from turtle import Turtle, Screen
from snake import Snake
import time

def initialize_screen():
    # Initialize Screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

def main():
    initialize_screen()
    snake = Snake()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()



if __name__ == "__main__":
    main()


screen.exitonclick()

