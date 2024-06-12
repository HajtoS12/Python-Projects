from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_step = 10
        self.y_step = -10
        self.move_speed = 0.1
        self.new_ball()
        self.bouncy_y()



    def new_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()


    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x,new_y)


    def bouncy_y(self):
        self.y_step *= -1


    def bouncy_x(self):
        self.x_step *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.x_step *= -1
        self.move_speed = 0.1





