from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)

snake=Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score() # updating score board

    # Detect collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset_snake()
    # Detect if collide with tail.i.e if head hit any segment of body, game over

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()
screen.exitonclick()
