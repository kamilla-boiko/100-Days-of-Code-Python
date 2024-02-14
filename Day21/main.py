from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard


def play():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("DarkOliveGreen1")
    screen.title("Snake Game")
    screen.tracer(0)

    scoreboard = Scoreboard()
    snake = Snake()
    food = Food()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Eat the food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Collision with wall
        if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
            scoreboard.reset()
            snake.reset()

        # Eat the tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()

        # Retry the game
        # if not game_is_on:
        #     answer = screen.textinput(
        #         title="GAME OVER",
        #         prompt=f"Your score is {scoreboard.score}!\nDo you want to restart? (y/n)"
        #     )
        #     if answer == "y":
        #         screen.clearscreen()
        #         play()

    screen.exitonclick()


if __name__ == "__main__":
    play()
