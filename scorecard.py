import turtle as t
class Scorecard(t.Turtle):
    def __init__(self,dist_x):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(dist_x,260)

    def update(self):
        self.write(self.score, move=False, align="center", font=("Courier", 24, "normal"))

    def increment(self):
        self.score+=1
        self.clear()
        self.update()

    def game_won(self,player):
        self.goto(0,0)
        self.write(f"Player {player} Won", move=False, align="center", font=("Courier", 48, "normal"))
