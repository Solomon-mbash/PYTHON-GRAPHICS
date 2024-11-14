from turtle import Turtle

ALIGHNMENT = "center"
FONT = ("Aerial", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,230)
        self.write(f"Score: {self.score}", move=False, align= ALIGHNMENT , font= FONT)
        self.update_score()


    def update_score(self):
        self.write(f"Score: {self.score}",False, align=ALIGHNMENT , font= FONT)
    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}",False, align=ALIGHNMENT , font=FONT)
        self.clear()
        self.update_score()
    def game_over(self):

        self.goto(0,0)
        self.write("GAME OVER", False,align=ALIGHNMENT, font=FONT)

