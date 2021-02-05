from turtle import Turtle
FONT = ("Arial", 20, "bold")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=275)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """This function increases the score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        """This function updates the scoreboard"""
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
