from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as file:
            content = file.read()
            content = int(content)
        self.highscore = content

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.score += 1
        self.show_score()

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as f:
                write_f = f.write(str(self.score))
            self.highscore = self.score
        self.score = 0
        self.show_score()
