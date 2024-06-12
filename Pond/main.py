import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(800,600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncy_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bouncy_x()

    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
