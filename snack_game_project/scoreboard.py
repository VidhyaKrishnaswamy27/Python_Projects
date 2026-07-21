from turtle import Turtle

class Scoreboard(Turtle):

    ALIGNMENT = "center"
    STYLE = "Courier", 24, "bold"
    def __init__(self):
        super().__init__()
        self.score=0
        with open(".\.venv\data.txt", mode="r") as file:
            self.highscore=int(file.read())


        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        # self.setposition(0,250)
        self.write(f"Score: {self.score}, High Score: {self.highscore} ", align = self.ALIGNMENT, font=(self.STYLE))

    def update_score(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align=self.ALIGNMENT, font=(self.STYLE))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER ", align=self.ALIGNMENT, font=(self.STYLE))

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(".\.venv\data.txt", mode="w") as file:
                file.write(f"{self.highscore}")

        self.score =0
        self.update_score()
