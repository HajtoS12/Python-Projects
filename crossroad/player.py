from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.player()


    def player(self):
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0,-280)

    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def go_to_start(self):
        self.goto(0, -280)