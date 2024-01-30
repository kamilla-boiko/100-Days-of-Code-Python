import turtle as t
import random


timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def draw_spirograph(gap: int):
    for i in range(int(360 / gap)):
        timmy.color(random_color())
        timmy.setheading(timmy.heading() + gap)
        timmy.circle(100)


draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()
