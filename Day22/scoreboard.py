from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Garamond", 40, "normal")
GAME_OVER = ("Garamond", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 220)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        winner = "LEFT"
        if self.r_score > self.l_score:
            winner = "RIGHT"
        self.goto(0, 0)
        self.write(f"GAME OVER! {winner} PLAYER IS WINNER!", align=ALIGNMENT, font=GAME_OVER)
