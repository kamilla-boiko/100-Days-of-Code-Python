from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")
colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple", "pink"]


def draw_figure(side_count: int) -> None:
    angle = 360 / side_count
    for _ in range(side_count):
        timmy.forward(100)
        timmy.right(angle)


for shape_side in range(3, 11):
    timmy.color(random.choice(colors))
    draw_figure(shape_side)


screen = Screen()
screen.exitonclick()
