from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")
timmy.color("green")


for _ in range(15):
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()


screen = Screen()
screen.exitonclick()
