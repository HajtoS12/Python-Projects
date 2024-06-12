import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car = CarManager()
screen.onkeypress(player.move_forward, "Up")
scoreboard = Scoreboard()

car.car_move()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.random_car()

    for cars in car.cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()


    if player.ycor() > 280:
        player.go_to_start()
        scoreboard.increase_score()
        car.new_move_speed()















screen.exitonclick()