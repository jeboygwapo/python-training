from turtle import Screen
from snake import Snake
import time

def initialize_screen():
    # Initialize Screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    return screen

def main():
    screen = initialize_screen()
    snake = Snake()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

    screen.exitonclick()

if __name__ == "__main__":
    main()
