import sys
import time
from turtle import Screen

from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

def initialize_screen():
    # Initialize Screen
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)
    return screen

def main():
    screen = initialize_screen()

    l_paddle = Paddle((-350,0))
    r_paddle = Paddle((350,0))

    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")
    screen.onkey(l_paddle.up, "w")
    screen.onkey(l_paddle.down, "s")


    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision in the wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            # needs to bounce
            ball.bounce_y()

        # Detect collision with paddles
        if ball.distance(r_paddle) < 50 and ball.xcor() > -320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # Detect r_paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.increase_left_score()

        # Detect l_paddle misses
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.increase_right_score()


    screen.exitonclick()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting gracefully...")
        sys.exit(0)