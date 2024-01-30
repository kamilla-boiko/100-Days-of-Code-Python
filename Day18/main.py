import colorgram
import turtle as t
import random

colors = colorgram.extract('image.jpg', 26)

rgb = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
color_list = rgb[1:]


timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
timmy.goto(-200, -200)

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    y = timmy.pos()[1] + 50
    timmy.goto(-200, y)


screen = t.Screen()
screen.exitonclick()
