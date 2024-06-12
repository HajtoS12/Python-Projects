from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = 5
        self.speed_increment = 5




    def new_car(self,position):
        car = Turtle("square")
        car.penup()
        car.shapesize(1,2)
        car.color(COLORS[random.randint(0,5)])
        car.goto(position)
        self.cars.append(car)

    def car_move(self):
        for car in self.cars:
            new_z = car.xcor() - self.speed
            car.goto(new_z, car.ycor())

    def random_car(self):
        self.car_move()
        if random.randint(1,6) == 1:
            self.new_car((300, random.randint(-250, 250)))


    def new_move_speed(self):
        self.speed += self.speed_increment

