from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"score is {self.score}", align="center",
                   font=("Arial", 18, "normal"))
        self.hideturtle()

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        print(self.score)

    def update_scoreboard(self):
        self.write(f"score is {self.score}", align="center",
                   font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over "
                   , align="center",
                   font=("Arial", 36, "normal"))
