from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")
timmy.color("green")


for _ in range(4):
    timmy.forward(100)
    timmy.right(90)


screen = Screen()
screen.exitonclick()
