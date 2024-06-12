from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-200, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: : {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()


